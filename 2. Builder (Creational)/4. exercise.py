class CodeElement:
    indent_size = 2

    def __init__(self, name='', type=''):
        self.name = name
        self.type = type
        self.fields = []

    def __str(self, indent):
        lines = []
        i = ' ' * (indent * self.indent_size)
        # lines.append(f'{i}Class {self.name}:')  # opening
        lines.append('{}class {}:'.format(i, self.name))  # opening

        if not self.fields:
            lines.append('  pass')
        else:
            lines.append('{}def __init__(self):'.format(' ' * self.indent_size * 1))

            for elem in self.fields:
                lines.append('{}self.{} = {}'.format(' ' * self.indent_size * 2, elem.name, elem.type))

        return '\n'.join(lines)

    def __str__(self):
        return self.__str(0)  # 0 is indent size


class CodeBuilder:
    def __init__(self, root_name):
        self.root_name = root_name
        self.__root = CodeElement(name=root_name)

    def add_field(self, type, name):
        self.__root.fields.append(
            CodeElement(type, name)
        )
        return self

    def __str__(self):
        return str(self.__root)


builder = CodeBuilder('Foo')
builder.add_field('name', '""').add_field('age', 0)
print(builder)

builder = CodeBuilder('Bar')
# builder.add_field('name', '""').add_field('age', 0)
print(builder)

# TEACHERS:
from unittest import TestCase


class Field:
    def __init__(self, name, value):
        self.value = value
        self.name = name

    def __str__(self):
        return 'self.%s = %s' % (self.name, self.value)


class Class:
    def __init__(self, name):
        self.name = name
        self.fields = []

    def __str__(self):
        lines = ['class %s:' % self.name]
        if not self.fields:
            lines.append('  pass')
        else:
            lines.append('  def __init__(self):')
            for f in self.fields:
                lines.append('    %s' % f)
        return '\n'.join(lines)


class CodeBuilder:
    def __init__(self, root_name):
        self.__class = Class(root_name)

    def add_field(self, type, name):
        self.__class.fields.append(Field(type, name))
        return self

    def __str__(self):
        return self.__class.__str__()


class Evaluate(TestCase):
    @staticmethod
    def preprocess(s=''):
        return s.strip().replace('\r\n', '\n')

    def test_empty(self):
        cb = CodeBuilder('Foo')
        self.assertEqual(
            self.preprocess(str(cb)),
            'class Foo:\n  pass'
        )

    def test_person(self):
        cb = CodeBuilder('Person').add_field('name', '""') \
            .add_field('age', 0)
        self.assertEqual(self.preprocess(str(cb)),
                         """class Person:
  def __init__(self):
    self.name = \"\"
    self.age = 0""")
