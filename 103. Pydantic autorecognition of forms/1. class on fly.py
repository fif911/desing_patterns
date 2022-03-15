from typing import List, Union, Optional

from pydantic import BaseModel


class Foo(BaseModel):
    count: int
    size: float = None


class BBar(BaseModel):
    lemon: str


class AdvancedApple(BaseModel):
    weight: int
    size: str = "10cm"


class Bar(BaseModel):
    apple: AdvancedApple
    banana: Optional[str] = None


class Spam(BaseModel):
    foo: Foo
    bars: List[Union[Bar, BBar]]
    # bars: List[Bar]
    # sections: List[]


if __name__ == '__main__':
    # m = Spam(foo={'count': 4}, bars=[{'apple': 'x1'}, {'apple': 'x2'}])
    dicts = {
        "foo": {'count': 4},
        "bars": [
            {'apple': {
                "weight": 10
            }
            },  # Bar
            {'apple': {
                "weight": 6
            }
            },  # Bar
            {'lemon': 'x3'},  # BBar
        ]
    }
    m = Spam(**dicts)
    print(m)
