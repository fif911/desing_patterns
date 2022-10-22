import enum
import logging
import types
from abc import abstractmethod
from datetime import date
from typing import Callable, Dict, List, Tuple, Optional

import pandas as pd
from pydantic import ValidationError, BaseModel, validator, Field, EmailStr


class ImportInvalidTemplate(Exception):
    error_code = "import_invalid_template"
    status_code = 400
    detail = "Invalid import template"


class BaseProcessor:
    @staticmethod
    def _combine(x: pd.DataFrame, col_a: str, col_b: str, drop_col: str = "last") -> pd.DataFrame:
        # TODO: replace iterrows with faster mechanism
        for _, row in x.iterrows():
            if col_b != "":
                row[col_a] += row[col_b]

        if drop_col is not None:
            if str.lower(drop_col) == "both":
                x.drop([col_a, col_b], inplace=True, axis=1)

            elif str.lower(drop_col) == "first":
                x.drop(col_a, inplace=True, axis=1)

            elif str.lower(drop_col) == "last":
                x.drop(col_b, inplace=True, axis=1)

        return x

    @staticmethod
    def _coalesce(x: pd.DataFrame, cols: list, drop_col: str = None) -> pd.DataFrame:
        # TODO: replace iterrows with faster mechanism
        for _, row in x.iterrows():
            for col in cols:
                if row[col] != "":
                    row[cols[0]] = row[col]
                    break

        if drop_col is not None:
            if str.lower(drop_col) == "except_first":
                x.drop(cols[1:], inplace=True, axis=1)

            elif str.lower(drop_col) == "first":
                x.drop(cols[0], inplace=True, axis=1)

        return x

    @staticmethod
    def _rename_cols(x: pd.DataFrame, mapping: Dict[str, str]) -> pd.DataFrame:
        return x.rename(columns=mapping)

    @staticmethod
    def _drop_cols(x: pd.DataFrame, cols: list) -> pd.DataFrame:
        return x.drop(cols, axis=1)

    @staticmethod
    def _get_subset(x: pd.DataFrame, cols: list) -> pd.DataFrame:
        return x[cols]

    @staticmethod
    def _set_index(x: pd.DataFrame, col: str) -> pd.DataFrame:
        return x.set_index(col)

    @staticmethod
    def _drop_empty_rows(x: pd.DataFrame) -> pd.DataFrame:
        def find_empty_rows(x: pd.DataFrame) -> bool:
            check = "".join([col for col in x])
            if not check:
                return True
            return False

        y = x.fillna("").astype(str)
        y.loc[:, "is_empty"] = y.apply(find_empty_rows, axis=1)
        # pandas does not support "is" for boolean comparison
        return y.loc[y["is_empty"] == False, ~y.columns.isin(["is_empty"])]

    @abstractmethod
    def preprocess(self) -> List[dict]:
        """Standardize the pandas DataFrame (e.g., set index, drop & rename columns, apply mapping on values)"""
        pass

    @abstractmethod
    def process(self) -> Tuple[dict, dict]:
        """Coerce and validate each record"""
        pass

    @staticmethod
    def _validate_minimum_fields(self):
        """Check if the minimum fields are populated

        Should only be applied to the BaseDataProcessor
        """
        raise NotImplementedError


class Convertor:
    def __init__(self, steps: Callable = None, records: dict = None):
        self.errors = {}
        self.success = {}
        self.tmp_errors = []
        self.tmp_models = []
        self.records = records

        if steps:
            self.steps = types.MethodType(steps, self)

    @abstractmethod
    def steps(self):
        raise NotImplementedError

    def execute(self):
        """Generic processor for each Processor item"""
        for ix, row in self.records.items():
            self.steps(row)

            if not self.tmp_errors or any(self.tmp_errors) is False:
                self.success.update({ix: self.tmp_models})
            else:
                self.errors.update({ix: self.tmp_errors})

            self.tmp_errors, self.tmp_models = [], []


def _validator_dict(self, model=None, data: dict = None, append_on_success: bool = True):
    """Utility function to create sequences of validation processors"""
    try:
        if append_on_success:
            self.tmp_models.append(model(**data).dict())
    except ValidationError as e:
        self.tmp_errors.append(e)
    except Exception as e:
        self.tmp_errors.append(e)


def _validator_list(self, model=None, data: List[dict] = None, extend: bool = False, append_on_success: bool = True):
    """Utility function to create sequences of validation processors

    Use param `extend = True`, if you want to return flat lists."""
    models = []
    errors = []
    for item in data:
        try:
            if append_on_success:
                models.append(model(**item).dict())
        except ValidationError as e:
            errors.append(e)
        except Exception as e:
            errors.append(e)

    if extend:
        self.tmp_models.extend(models)
        self.tmp_errors.extend(errors)
    else:
        self.tmp_models.append(models)
        self.tmp_errors.append(errors)


# see form path "GW1/Unterschrift/Mitwirkung"
MAPPING_PARTICIPATION = {
    "Vorname": "E7416001",
    "Name": "E7415901",
    "Straßenname": "E7416101",
    "Plz": "E7416201",
    "Telefonnummer": "E7416301"
}

# see form path "GW1/Empfangsv"
MAPPING_RECEIVER = {
    "Anredeschlüssel": "E7404610",
    "Titel/akademischer Grad": "E7404614",
    "Vorname / Firma (Zeile 1)": "E7404613",
    "Name / Firma (Zeile 2)": "E7404611",
    "Straßenname": "E7404624",
    "Hausnr.": "E7404625",
    "Zusatz": "E7404626",
    "Plz": "E7404640",
    "Ort": "E7404622",
    "Postfach": "E7404627",
    "Telefonnummer": "E7412201"
}

# see form path "GW1/Eigentuemer"
MAPPING_OWNER = {
    "Anrede": "E7404510",
    "Titel/akademischer Grad": "E7404514",
    "Vorname / Firma": "E7404513",
    "Nachname": "E7404511",
    "Zähler": "E7404570",
    "Nenner": "E7404571",
    "Straßenname": "E7404524",
    "Hausnr.": "E7404525",
    "Zusatz": "E7404526",
    "Plz": "E7404540",
    "Ort": "E7404522",
    "Postfach": "E7404527",
    "Telefonnummer": "E7414601",
    "Steuernummer": "E7404573",
    "Zuständiges Finanzamt": "E7404574",
}

# see form path "GW1/Gemarkungen/Einz"
MAPPING_PARCELS = {
    "Gemarkung": "E7401141",
    "Grundbuchblatt": "E7401142",
    "Flur": "E7401143",
    "Zähler_Flur": "E7401144",  # only valid after renaming ambiguous columns
    "Nenner_Flur": "E7401145",  # only valid after renaming ambiguous columns
    "Fläche in m²": "E7411001",
    "Zähler_Einheit": "E7410702",  # only valid after renaming ambiguous columns
    "Nenner_Einheit": "E7410703",  # only valid after renaming ambiguous columns
}

MAPPING_PARCELS_RENAME = {
    "Zähler": "Zähler_Flur",
    "Nenner": "Nenner_Flur",
    "Zähler.1": "Zähler_Einheit",
    "Nenner.1": "Nenner_Einheit",

    "Zähler.2": "Zähler_Flur.1",
    "Nenner.2": "Nenner_Flur.1",
    "Zähler.3": "Zähler_Einheit.1",
    "Nenner.3": "Nenner_Einheit.1",

    "Zähler.4": "Zähler_Flur.2",
    "Nenner.4": "Nenner_Flur.2",
    "Zähler.5": "Zähler_Einheit.2",
    "Nenner.5": "Nenner_Einheit.2",

    "Zähler.6": "Zähler_Flur.3",
    "Nenner.6": "Nenner_Flur.3",
    "Zähler.7": "Zähler_Einheit.3",
    "Nenner.7": "Nenner_Einheit.3",

    "Zähler.8": "Zähler_Flur.4",
    "Nenner.8": "Nenner_Flur.4",
    "Zähler.9": "Zähler_Einheit.4",
    "Nenner.9": "Nenner_Einheit.4",

    "Zähler.10": "Zähler_Flur.5",
    "Nenner.10": "Nenner_Flur.5",
    "Zähler.11": "Zähler_Einheit.5",
    "Nenner.11": "Nenner_Einheit.5",

    "Zähler.12": "Zähler_Flur.6",
    "Nenner.12": "Nenner_Flur.6",
    "Zähler.13": "Zähler_Einheit.6",
    "Nenner.13": "Nenner_Einheit.6",
}

# see form path "GW1/Ang_Feststellung"  and "GW1/Lage"
MAPPING_BASEDATA = {
    "Mandatsnr.*": "datev_client_id",
    "Bezeichnung / Titel*": "name",
    "Art der Einheit*": "property_type",
    "Bundesland*": "federal_state",
    "Straßenname": "E7401124",
    "Hausnr.": "E7401125",
    "Zusatz": "E7401131",
    "Plz": "E7401121",
    "Ort": "E7401122",
}


class PropertyTypeEnum(str, enum.Enum):
    detached_house = 'detached_house'  # Einfamilienhaus
    two_family_house = 'two_family_house'  # Zweifamilienhaus
    condominium = 'condominium'  # Wohnungseigentum
    mixed_use_property = 'mixed_use_property'  # gemischt genutztes Grundstück
    rental_residential_property = 'rental_residential_property'  # Mietwohngrundstück
    business_property = 'business_property'  # Geschäftsgrundstück
    part_ownership = 'part_ownership'  # Teileigentum
    other_built_up_property = 'other_built_up_property'  # sonstiges bebautes Grundstück
    unbuilt = 'unbuilt'  # unbebautes Grundstück
    agriculture = 'agriculture'  # Land- und Forstwirtschaft
    livestock = 'livestock'  # Land- und Forstwirtschaft Tierbestand
    land_value_model = 'land_value_model'  # Bodenwertmodell (BW)
    building_with_living_space = 'building_with_living_space'  # Gebäude mit Wohnflächen (BY, HE, HH, NI)
    building_without_living_space = 'building_without_living_space'  # Gebäude ohne Wohnflächen (BY, HE, HH, NI)


class PropertyFederalStateEnum(str, enum.Enum):
    baden_wurttemberg = "baden_wurttemberg"  # Baden-Württemberg
    bayern = "bayern"  # Bayern
    berlin = "berlin"  # Berlin
    brandenburg = "brandenburg"  # Brandenburg
    bremen = "bremen"  # Bremen
    hamburg = "hamburg"  # Hambuzrg
    hesse = "hesse"  # Hessen
    mecklenburg_vorpommern = "mecklenburg_vorpommern"  # Mecklenburg-Vorpommern
    lower_saxony = "lower_saxony"  # Niedersachsen
    north_rhine_westphalia = "north_rhine_westphalia"  # Nordrhein-Westfalen
    rhineland_palatinate = "rhineland_palatinate"  # Rheinland-Pfalz
    saarland = "saarland"  # Saarland
    saxony = "saxony"  # Sachsen
    saxony_anhalt = "saxony_anhalt"  # Sachsen-Anhalt
    schleswig_holstein = "schleswig_holstein"  # Schleswig-Holstein
    thuringia = "thuringia"  # Thüringen


MAPPING_FEDERAL_STATES = {
    "Berlin": PropertyFederalStateEnum.berlin,
    "Brandenburg": PropertyFederalStateEnum.brandenburg,
    "Bremen": PropertyFederalStateEnum.bremen,
    "Mecklenburg-Vorpommern": PropertyFederalStateEnum.mecklenburg_vorpommern,
    "Nordrhein-Westfalen": PropertyFederalStateEnum.north_rhine_westphalia,
    "Rheinland-Pfalz": PropertyFederalStateEnum.rhineland_palatinate,
    "Saarland": PropertyFederalStateEnum.saarland,
    "Sachsen": PropertyFederalStateEnum.saxony,
    "Sachsen-Anhalt": PropertyFederalStateEnum.saxony_anhalt,
    "Schleswig-Holstein": PropertyFederalStateEnum.schleswig_holstein,
    "Thüringen": PropertyFederalStateEnum.thuringia,
}

MAPPING_FEDERAL_STATES_REVERSE = {v: k for k, v in MAPPING_FEDERAL_STATES.items()}

MAPPING_SCENARIOS = {
    "Unbekannt": None,
    "Unbebautes Grundstück": PropertyTypeEnum.unbuilt,
    "Einfamilienhaus": PropertyTypeEnum.detached_house,
    "Mietwohngrundstück": PropertyTypeEnum.condominium,
    "Wohnungseigentum": PropertyTypeEnum.rental_residential_property,
    "Zweifamilienhaus": PropertyTypeEnum.two_family_house,
    "Gemischt genutztes Grundstück": PropertyTypeEnum.mixed_use_property,
    "Geschäftsgrundstück": PropertyTypeEnum.business_property,
    "Teileigentum": PropertyTypeEnum.part_ownership,
    "Sonstiges bebautes Grundstück": PropertyTypeEnum.other_built_up_property,
    "Betrieb der Land- und Forstwirtschaft": PropertyTypeEnum.agriculture,
    "Betrieb der Land- und Forstwirtschaft mit Viehbestand": PropertyTypeEnum.livestock
}

MAPPING_SCENARIOS_REVERSE = {v: k for k, v in MAPPING_SCENARIOS.items()}

MAPPING_SALUTATIONS = {
    'ohne Anrede': "01",
    'Herrn': "02",
    'Frau': "03",
    'Firma': "07",
    'Erbengemeinschaft': "08",
    'Arbeitsgemeinschaft': "09",
    'Grundstücksgemeinschaft': "10",
    'Gesellschaft bürgerlichen Rechts': "11",
    'Sozietät': "12",
    'Praxisgemeinschaft': "13",
    'Betriebsgemeinschaft': "14",
    'Wohnungseigentümergemeinschaft': "15",
    'Partnergesellschaft': "16",
    'Partenreederei': "17",
    "Insolvenzverwalter": "18",
    "Zwangsverwalter": "19"
}

validator_zip_code = Field(None, regex="^\d{5}$", description="regex=\"^\d{5}$\"", example="00123")
validator_post_office_box = Field(None, regex="^\d{1,6}$", description="regex=\"^\d{1,6}$\"", example="014243")
validator_phone_number = Field(None, regex="^\+\d+$", description="regex=\"^\+\d+$\"", example="+491522220022")
validator_string_25_char = Field(None, max_length=25)
validator_string_255_char = Field(None, max_length=255)
validator_string_150_char = Field(None, max_length=150)  # Auth0 constraint for the First- and Lastname
validator_string_310_char = Field(None,
                                  max_length=310)  # to make it possible to store 150 characters from the First- and Lastname plus space character
validator_tax_number = Field(None, regex="^((\d|\/|\ |\-){1,20}$)", description="^((\d|\/|\ |\-){1,20}$)",
                             example="12 345/67890")  # also can be a case xx xxx/xxxx
validator_tax_number_property = Field(None, regex="^((\d|\/|\ |\-){1,20}$)",
                                      description="^((\d|\/|\ |\-){1,20}$)",
                                      example="12 345 67890")  # xxx/xxx/xxxxx    xx/xxx/xxxxx    xx xxx xxxxx
validator_tax_id = Field(None, regex="^(([a-zA-Z0-9/-]|\ ){1,20}$)", description="^(([a-zA-Z0-9/-]|\ ){1,20}$)",
                         example="12345678901")
validator_house_number = Field(None, ge=1, le=9999)


class SalutationCodeEnum(str, enum.Enum):
    blank = 'blank'
    mister = 'mister'
    misses = 'misses'
    company = 'company'
    community_of_heirs = 'community_of_heirs'
    working_group = 'working_group'
    property_community = 'property_community'
    c_l_partnership = 'c_l_partnership'
    c_l_person = 'c_l_person'
    c_l_medical = 'c_l_medical'
    operating_consortium = 'operating_consortium'
    homeowners_association = 'homeowners_association'
    partnership_company = 'partnership_company'
    shipowning_partnership = 'shipowning_partnership'
    insolvency_administrator = 'insolvency_administrator'
    administrative_receiver = 'administrative_receiver'


class ClientCompanyTypeEnum(str, enum.Enum):
    private_person = 'private_person'  # just regular person
    entrepreneur = 'entrepreneur'  # single entrepreneur
    company = 'company'  # big company


class LRPrivatePersonOrCompanyEnum(str, enum.Enum):
    private_person = 'private_person'
    company = 'company'


class CountriesEnum(str, enum.Enum):
    germany = "germany"
    afghanistan = "afghanistan"
    egypt = "egypt"
    albania = "albania"
    algeria = "algeria"
    american_virgin_islands = "american_virgin_islands"
    american_samoa = "american_samoa"
    american_island = "american_island"
    andorra = "andorra"
    angola = "angola"
    anguilla = "anguilla"
    antarctic = "antarctic"
    antigua_and_barbuda = "antigua_and_barbuda"
    equatorial_guinea = "equatorial_guinea"
    argentina = "argentina"
    armenia = "armenia"
    aruba = "aruba"
    azerbaijan = "azerbaijan"
    ethiopia = "ethiopia"
    australia = "australia"
    australian_oceania = "australian_oceania"
    bahamas = "bahamas"
    bahrain = "bahrain"
    bangladesh = "bangladesh"
    barbados = "barbados"
    belgium = "belgium"
    belize = "belize"
    benin = "benin"
    bermuda = "bermuda"
    busy_palestinian_territories = "busy_palestinian_territories"
    bhutan = "bhutan"
    bolivia = "bolivia"
    bonaire = "bonaire"
    bosnia_and_herzegovina = "bosnia_and_herzegovina"
    botswana = "botswana"
    bouvet_islands = "bouvet_islands"
    brazil = "brazil"
    british_virgin_islands = "british_virgin_islands"
    brit_territory_in_ind_ocean = "brit_territory_in_ind_ocean"
    brunei_darussalam = "brunei_darussalam"
    bulgaria = "bulgaria"
    burkina_faso = "burkina_faso"
    burundi = "burundi"
    ceuta = "ceuta"
    chile = "chile"
    china_peoples_republic = "china_peoples_republic"
    cooking = "cooking"
    costa_rica = "costa_rica"
    cote_d_apos_ivoire = "cote_d_apos_ivoire"
    curacao = "curacao"
    denmark = "denmark"
    democratic_peoples_republic_of_korea = "democratic_peoples_republic_of_korea"
    dominica = "dominica"
    dominican_republic = "dominican_republic"
    djibouti = "djibouti"
    ecuador = "ecuador"
    el_salvador = "el_salvador"
    eritrea = "eritrea"
    estonia = "estonia"
    falkland_islands = "falkland_islands"
    faroe_islands = "faroe_islands"
    fiji = "fiji"
    finland = "finland"
    france_and_reunion = "france_and_reunion"
    french_southern_areas = "french_southern_areas"
    french_polynesia = "french_polynesia"
    gab = "gab"
    gambia = "gambia"
    georgia = "georgia"
    ghana = "ghana"
    gibraltar = "gibraltar"
    grenada = "grenada"
    greece = "greece"
    greenland = "greenland"
    guam = "guam"
    guatemala = "guatemala"
    guernsey = "guernsey"
    guinea = "guinea"
    guinea_bissau = "guinea_bissau"
    guyana = "guyana"
    haiti = "haiti"
    heard_and_mcdonald_islands = "heard_and_mcdonald_islands"
    honduras = "honduras"
    hong_kong = "hong_kong"
    india = "india"
    indonesia = "indonesia"
    island_man = "island_man"
    iraq = "iraq"
    ireland = "ireland"
    islamic_republic_of_iran = "islamic_republic_of_iran"
    iceland = "iceland"
    israel = "israel"
    italy = "italy"
    jamaica = "jamaica"
    japan = "japan"
    yemen = "yemen"
    jersey = "jersey"
    jordan = "jordan"
    caiman_islands = "caiman_islands"
    cambodia = "cambodia"
    cameroon = "cameroon"
    canada = "canada"
    cape_verde = "cape_verde"
    kazakhstan = "kazakhstan"
    qatar = "qatar"
    kenya = "kenya"
    kyrgyzstan = "kyrgyzstan"
    kiribati = "kiribati"
    coconut_islands = "coconut_islands"
    colombia = "colombia"
    comoros = "comoros"
    congo = "congo"
    congo_democratic_republic = "congo_democratic_republic"
    kosovo = "kosovo"
    croatia = "croatia"
    cuba = "cuba"
    kuwait = "kuwait"
    laos_democratic_peoples_republic = "laos_democratic_peoples_republic"
    lesotho = "lesotho"
    latvia = "latvia"
    lebanon = "lebanon"
    liberia = "liberia"
    libya = "libya"
    liechtenstein = "liechtenstein"
    lithuania = "lithuania"
    luxembourg = "luxembourg"
    macau = "macau"
    madagascar = "madagascar"
    macedonia = "macedonia"
    malawi = "malawi"
    malaysia = "malaysia"
    maldives = "maldives"
    mali = "mali"
    malta = "malta"
    morocco = "morocco"
    marshall_islands = "marshall_islands"
    mauritania = "mauritania"
    mauritius = "mauritius"
    mayotte = "mayotte"
    melilla = "melilla"
    mexico = "mexico"
    micronesia = "micronesia"
    monaco = "monaco"
    mongolia = "mongolia"
    montenegro = "montenegro"
    montserrat = "montserrat"
    mozambique = "mozambique"
    myanmar = "myanmar"
    namibia = "namibia"
    nauru = "nauru"
    nepal = "nepal"
    new_caledonia = "new_caledonia"
    new_zealand = "new_zealand"
    new_zealand_oceania = "new_zealand_oceania"
    nicaragua = "nicaragua"
    netherlands = "netherlands"
    netherlands_antilles = "netherlands_antilles"
    niger = "niger"
    nigeria = "nigeria"
    niue_island = "niue_island"
    northern_marianas = "northern_marianas"
    norfolk_island = "norfolk_island"
    norway = "norway"
    oman = "oman"
    austria = "austria"
    pakistan = "pakistan"
    palau = "palau"
    panama = "panama"
    papua_new_guinea = "papua_new_guinea"
    paraguay = "paraguay"
    peru = "peru"
    philippines = "philippines"
    pitcairn = "pitcairn"
    polar_areas = "polar_areas"
    poland = "poland"
    portugal = "portugal"
    republic_of_korea_south_korea = "republic_of_korea_south_korea"
    republic_of_moldova = "republic_of_moldova"
    rwanda = "rwanda"
    romania = "romania"
    russian_federation = "russian_federation"
    saba = "saba"
    solomon_islands = "solomon_islands"
    zambia = "zambia"
    samoa = "samoa"
    san_marino = "san_marino"
    sao_tome_and_principe = "sao_tome_and_principe"
    saudi_arabia = "saudi_arabia"
    sweden = "sweden"
    switzerland = "switzerland"
    senegal = "senegal"
    serbia = "serbia"
    serbia_and_montenegro = "serbia_and_montenegro"
    seychelles = "seychelles"
    sierra_leone = "sierra_leone"
    zimbabwe = "zimbabwe"
    singapore = "singapore"
    sint_eustatius = "sint_eustatius"
    sint_maarten = "sint_maarten"
    slovakia = "slovakia"
    slovenia = "slovenia"
    somalia = "somalia"
    other_countries_and_territories = "other_countries_and_territories"
    spain = "spain"
    sri_lanka = "sri_lanka"
    st_helena = "st_helena"
    st_kitts_and_nevis = "st_kitts_and_nevis"
    st_lucia = "st_lucia"
    st_pierre_and_miquelon = "st_pierre_and_miquelon"
    st_vincent_and_the_grenadines = "st_vincent_and_the_grenadines"
    south_africa = "south_africa"
    sudan = "sudan"
    south_georgien_u_southern_sandwich_islands = "south_georgien_u_southern_sandwich_islands"
    south_sudan = "south_sudan"
    suriname = "suriname"
    swaziland = "swaziland"
    syria_arab_republic = "syria_arab_republic"
    tajikistan = "tajikistan"
    taiwan = "taiwan"
    tanzania_united_republic = "tanzania_united_republic"
    thailand = "thailand"
    timor_leste = "timor_leste"
    togo = "togo"
    tokelau_islands = "tokelau_islands"
    tonga = "tonga"
    trinidad_and_tobago = "trinidad_and_tobago"
    chad = "chad"
    czech_republic = "czech_republic"
    tunisia = "tunisia"
    turkey = "turkey"
    turkmenistan = "turkmenistan"
    turks_and_caicos_islands = "turks_and_caicos_islands"
    tuvalu = "tuvalu"
    uganda = "uganda"
    ukraine = "ukraine"
    hungary = "hungary"
    uruguay = "uruguay"
    usa = "usa"
    uzbekistan = "uzbekistan"
    vanuatu = "vanuatu"
    vatican_city = "vatican_city"
    venezuela = "venezuela"
    united_arab_emirates = "united_arab_emirates"
    united_kingdom_great_britain_and_northern_ireland = "united_kingdom_great_britain_and_northern_ireland"
    vietnam = "vietnam"
    valais_and_futuna = "valais_and_futuna"
    christmas_island_ind_ocean = "christmas_island_ind_ocean"
    belarus = "belarus"
    central_african_republic = "central_african_republic"
    cyprus = "cyprus"


class AddressTypeEnum(str, enum.Enum):
    """Points whether client wants to receive letter via address or postbox"""
    postbox = 'postbox'
    address = 'address'


def lowercase_value(cls, value: str) -> str:
    if value:
        return value.lower()


# Shared properties while calling from API on create and update
class ClientCompanyBase(BaseModel):
    name: Optional[str] = Field(max_length=300)  # for PP it could be 301, for others - same as short name
    short_name: Optional[str] = Field(max_length=255)

    # Base company info
    company_type: Optional[ClientCompanyTypeEnum]  # Should be ENUM here with 3 types allowed only
    company_email: Optional[EmailStr]
    mobile_phone_number: Optional[str] = validator_phone_number
    land_line_phone_number: Optional[str] = validator_phone_number

    # Legal person info
    lr_exists: Optional[bool]
    lr_salutation_code: Optional[SalutationCodeEnum]
    lr_title_owner: Optional[str] = Field(max_length=15)
    lr_type: Optional[LRPrivatePersonOrCompanyEnum]
    lr_first_name: Optional[str] = Field(max_length=255)
    lr_last_name: Optional[str] = Field(max_length=255)
    lr_birth_date: Optional[date]  # Geburtsdatum
    lr_tax_id: Optional[str] = validator_tax_id  # Steueridentifikationsnummer only for PP person

    # Tax info
    tax_number: Optional[str] = validator_tax_number

    # only for company type = private_person
    pp_salutation_code: Optional[SalutationCodeEnum]
    pp_title_owner: Optional[str] = Field(max_length=15)
    pp_first_name: Optional[str] = Field(max_length=149)  # due to limitations of Auth0
    pp_last_name: Optional[str] = Field(max_length=150)  # due to limitations of Auth0
    pp_birth_date: Optional[date]
    pp_tax_id: Optional[str] = validator_tax_id

    # only for company type = company
    company_names: Optional[str]
    legal_form: Optional[str]

    # Address common for any type of company
    address_type: Optional[AddressTypeEnum]
    street: Optional[str] = Field(max_length=255)  # Straße
    house_number: Optional[str] = Field(max_length=255)  # Hausnummer
    house_number_addition: Optional[str] = Field(max_length=10)
    city: Optional[str] = Field(max_length=255)  # Ort
    zip_code: Optional[str] = Field(max_length=16)  # Postleitzahl
    country: Optional[CountriesEnum]
    federal_state: Optional[PropertyFederalStateEnum]  # Land the same as state in front-end
    post_office_box: Optional[str] = validator_post_office_box
    address_appendix: Optional[str] = Field(max_length=999)
    additional_shipping_information: Optional[str] = Field(max_length=999)

    datev_client_id: Optional[int] = Field(ge=0, le=999999999)  # Zentrale Mandanten Nummer from Datev

    _lower_case = validator('company_email', allow_reuse=True)(lowercase_value)


class PropertyTaxTypeEnum(str, enum.Enum):
    unbuilt = 'unbuilt'
    built = 'built'
    agriculture = 'agriculture'


class PropertyBase(BaseModel):
    name: Optional[str] = validator_string_255_char

    tax_type: Optional[PropertyTaxTypeEnum] = None
    property_type: Optional[PropertyTypeEnum] = None
    file_number_assessed_value: Optional[str] = Field(
        None,
        regex=r"^\d{10,17}$",
        description=r"regex=\"^\d{10,17}$\"",
        example="12345678901234")
    federal_state: Optional[PropertyFederalStateEnum] = None


class MinimumFieldRequirements(BaseModel):
    datev_client_id: int = Field(ge=0, le=999999999)
    name: str = validator_string_255_char
    property_type: Optional[PropertyTypeEnum] = None
    federal_state: PropertyFederalStateEnum = None


class GW1_Lage_fields(BaseModel):
    class Config:
        orm_mode = True
        smart_union = True

    E7401124: Optional[str] = Field(None, description='Straße/Lagebezeichnung', min_length=1, max_length=25,
                                    regex=r'^.{1,25}$')
    E7401125: Optional[str] = Field(None, description='Hausnummer', min_length=1, max_length=4,
                                    regex=r'^(?=.{1,4}$)^[0-9]+$')
    E7401126: Optional[str] = Field(None, description='Hausnummerzusatz', min_length=1, max_length=10,
                                    regex=r'^.{1,10}$')
    E7401131: Optional[str] = Field(None, description='Zusatzangaben', min_length=1, max_length=25, regex=r'^.{1,25}$')
    E7401121: Optional[str] = Field(None, description='Postleitzahl', min_length=5, max_length=5,
                                    regex=r'^(?=.{5,5}$)^\d+$')
    E7401122: Optional[str] = Field(None, description='Ort', min_length=1, max_length=25, regex=r'^.{1,25}$')


def _validator_dict(self, model=None, data: dict = None, append_on_success: bool = True):
    """Utility function to create sequences of validation processors"""
    try:
        if append_on_success:
            self.tmp_models.append(model(**data).dict())
    except ValidationError as e:
        self.tmp_errors.append(e)
    except Exception as e:
        self.tmp_errors.append(e)


# actual code

class BaseDataProcessor(BaseProcessor):
    """Process sheet `Stammdaten`"""

    def __init__(self):
        self._column_mapping: Dict[str, str] = MAPPING_BASEDATA
        self._federal_state_mapping: Dict[str, str] = MAPPING_FEDERAL_STATES
        self._scenario_mapping: Dict[str, str] = MAPPING_SCENARIOS

    def preprocess(self, df: pd.DataFrame) -> Tuple[Dict[int, tuple], Dict[int, list]]:
        df = self._set_index(df, "Lfd.-Nr.")
        df = self._drop_empty_rows(df)
        df = self._rename_cols(df, self._column_mapping)

        df["federal_state"] = df["federal_state"].map(self._federal_state_mapping)
        df["property_type"] = df["property_type"].map(self._scenario_mapping)

        records = df.to_dict(orient="index")
        return records

    def process(self, records: Dict[str, dict]) -> Tuple[dict, dict]:
        def basedata_validator(self, row):
            _validator_dict(self, ClientCompanyBase, {"datev_client_id": row.get("datev_client_id")})
            _validator_dict(self, PropertyBase, {"name": row.get("name"),
                                                 "property_type": row.get("property_type"),
                                                 "federal_state": row.get("federal_state")})
            _validator_dict(self, GW1_Lage_fields, row)

            # Check, if the minimum fields have been populated
            # TODO: Duplicate errors should not be provided - implement flag in _validator_dict / validator_list
            _validator_dict(self, MinimumFieldRequirements, {"datev_client_id": row.get("datev_client_id"),
                                                             "name": row.get("name"),
                                                             "property_type": row.get("property_type"),
                                                             "federal_state": row.get("federal_state")},
                            append_on_success=False)

        s = Convertor(basedata_validator, records=records)
        s.execute()

        return (s.success, s.errors)


class BWModelImportProcessor:
    @staticmethod
    def _read(file) -> Dict[str, pd.DataFrame]:
        settings = {
            'header_row': 2,
            'sheet_name': None,
            'skiprows': None
        }

        sheets = [
            "Stammdaten BW",
            "Gemarkungen und Flurstücke BW",
            "Eigentümer BW",
            "Empfangsvollmacht BW",
            "Mitwirkung BW"
        ]

        dfs = {}
        for sheet in sheets:
            try:
                df = pd.read_excel(file,
                                   sheet_name=sheet,
                                   engine="openpyxl",
                                   # xlrd for xls, openpyxl for xlsx, however, comments are only readable via xlrd
                                   header=settings.get("header_row"),
                                   skiprows=settings.get("skiprows"),
                                   dtype="string",
                                   keep_default_na=False)
                dfs.update({sheet: df})
            except ValueError:
                logging.exception(f"Template not supported")
                raise ImportInvalidTemplate
            except Exception as e:
                logging.exception(f"Unexpected error occurred during file reading")
                raise e
        return dfs

    @classmethod
    def execute(self, file) -> Dict[str, List[dict]]:
        dfs = self._read(file)
        print(dfs)

        base = BaseDataProcessor()
        # parcel = ParcelProcessor()
        # owner = OwnerProcessor()
        # participant = ParticipantProcessor()
        # receiver = ReceiverProcessor()

        base_records = base.preprocess(dfs["Stammdaten BM"])
        base_success, base_failure = base.process(base_records)

        ids_valid, ids_failure = self._get_ids(
            base_failure,
            # parcel_failure,
            # owner_failure,
            # participant_failure,
            # receiver_failure,
            base_success,
            # parcel_success,
            # owner_success,
            # participant_success,
            # receiver_success
        )

        models, error_ids = self._build_model(
            ids_valid,
            base_success,
            # parcel_success,
            # owner_success,
            # participant_success,
            # receiver_success
        )

        error_ids = error_ids | ids_failure

        results = self._convert_result(base_records, models, error_ids)


if __name__ == '__main__':
    # Mapping Import-BW-Juni-2022.xlsx
    file = 'C:/Users/ozakotianskyi/PycharmProjects/desing_patterns/property-tax-api/Mapping Import-BW-Juni-2022.xlsx'

    r = BWModelImportProcessor().execute(file)
