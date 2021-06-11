# Builder - component which provides an API for constructing an object step-by-step
# !!!!
# When piecewise object construction is complicated, provide an API for doing it succinctly(лаконично)
# !!!!
# Some objects are simple Some object require a lot of ceremony to create
# Having an object with 10 initializers arguments is not productive
# Instead opt for piecewise construction


# construct the html p
text = 'hello'
parts = ['<p>', text, '</p>']
print(''.join(parts))

words = ['hello', 'world']
parts = ['<ul>']

for w in words:
    parts.append(f'  <li>{w}</li>')
parts.append('</ul>')
print('\n'.join(parts))


# but if somebody will forget to close some html tag or anything. We want to outsource the process
# of constructing different HTML to a Builder
# And if would be really easier so work with OOP( if each of the HTML elements will be a class of some kind)

class HtmlElement:
    indent_size = 2

    def __init__(self, name='', text=''):
        self.text = text
        self.name = name
        self.elements = []  # can have any number of children

    def __str(self, indent):
        lines = []
        i = ' ' * (indent * self.indent_size)
        lines.append(f'{i}<{self.name}>')  # opening tag

        if self.text:
            i1 = ' ' * ((indent + 1) * self.indent_size)
            lines.append(f'{i1}{self.text}')

        for e in self.elements:
            lines.append(e.__str(indent + 1))

        lines.append(f'{i}</{self.name}>')  # closing tag
        return '\n'.join(lines)

    def __str__(self):
        return self.__str(0)

    @staticmethod
    def create(name):
        """Create function. Breaks Open closed P a bit but as they are already realted as it's builder
        it not problem to have such method"""
        return HtmlBuilder(name)


class HtmlBuilder:
    """
    dedicated component to build different HTML elements
    Takes the HTML element and builds it up using API"""

    def __init__(self, root_name):
        self.root_name = root_name
        self.__root = HtmlElement(name=root_name)  # element we will build up

    def add_child(self, child_name, child_text):
        """
        Appends the child element object to root HtmlElement object's elements list
        """
        self.__root.elements.append(
            HtmlElement(child_name, child_text)
        )

    # adding fluent interface by implementing chained calls support
    def add_child_fluent(self, child_name, child_text):
        """
        Appends the child element object to root HtmlElement object's elements list AND
        Allows to chain the calls: builder.add_child_fluent.add_child_fluent
        """
        self.__root.elements.append(
            HtmlElement(child_name, child_text)
        )
        return self

    # def get_child(self, pos):
    #     return self.__root.elements[pos]

    def __str__(self):
        return str(self.__root)  # expose the html by calling str method of build HtmlElement


# builder = HtmlBuilder('ul')
builder = HtmlElement.create('ul')
# builder.add_child('li', 'hello')
# builder.add_child('li', 'world')

# chain calls support
builder.add_child_fluent('li', 'helloooo').add_child_fluent('li', 'world')
# builder.get_child(0).add_child('a') # will not work
print('Ordinary builder')
print(builder)
