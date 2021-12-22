"""
Scenario: Scalar object can masquerade as a collection and what benefits this actually gives us

You can think of an Iterable as a marker interface that prevents you from trying to iterate something and then catching the exception if an object is not iterable.
"""
from abc import ABC
from collections.abc import Iterable


class Connectable(Iterable, ABC):
    def connect_to(self, other):
        if self == other:
            return  # we cant connect to self

        for s in self:
            for o in other:
                s.outputs.append(o)
                o.inputs.append(s)


class Neuron(Connectable):
    def __init__(self, name):
        self.name = name
        # but in addition neurons are characterized by their connections
        # so neurons connect to other neurons and thereby (тем самым) they keep the inputs and outputs list
        self.inputs = []
        self.outputs = []

    def __str__(self):
        return f'{self.name} , {len(self.inputs)}  inputs, {len(self.outputs)} outputs'

    def __iter__(self):
        # this is how we turn scalar value in a collection of one element
        yield self

    def connect_to(self, other):
        self.outputs.append(other)
        other.inputs.append(self)


# and so far so good
# this code will actually work
# and imagine you decide that having single neuron is a bit too cumbersome(громоздкий)
# and u want to make large groups of neurons

class NeuronLayer(list, Connectable):
    """List of Neurons"""

    def __init__(self, name, count):
        # name and number of neurons u want in this layer
        super(NeuronLayer, self).__init__()
        self.count = count
        self.name = name

        for x in range(0, count):
            self.append((Neuron(f'{name} - {x}')))

    def __str__(self):
        return f'{self.name} with {len(self)} neurons'


# lets write connective function
def connect_to(self, other):
    if self == other:
        return  # we cant connect to self

    for s in self:
        for o in other:
            s.outputs.append(o)
            o.inputs.append(s)


if __name__ == '__main__':
    # but now we have a very big problem
    # We want to be able to connect neurons and neuron layers
    # lets flash out the scenario we want to support
    neuron1 = Neuron('n1')
    neuron2 = Neuron('n2')
    layer1 = NeuronLayer("L1", 3)
    layer2 = NeuronLayer("L2", 4)
    print(neuron1, neuron2, layer1, layer2, sep=' |\n')

    # also we can take the entire definition of def connect_to(self, other):
    # and just imbue(вселить) it into both Neuron and NeuronLayer

    # Neuron.connect_to = connect_to # with Connectable class we  should get rid of this
    # NeuronLayer.connect_to = connect_to

    # this would actually function except there a bit of a problem
    # We cant connect neuron to the neuron cause of for s in self:
    # cause Neuron is not iterable
    # cause Neuron is just a scalar value
    # but its very easy to turn scalar value into collection
    # into something that actually iterable
    # after __iter__
    # everything works

    # you want to be able to say
    neuron1.connect_to(neuron2)  # but its already works
    # and what u also want to do
    # u want to be able to connect neuron to layer
    neuron1.connect_to(layer1)
    layer1.connect_to(neuron2)
    layer1.connect_to(layer2)
    # this might end up causing us to write 4 different methods
    # or functions. But we dont really want to do this
    # we want one function
    # we could write it. If we can iterate both neurons in the layer as well as
    # neuron in a neuron
    # and its possible to  do exactly that

    # __iter__ implemented

    print("\n", neuron1, neuron2, layer1, layer2, sep=' |\n')
    # and it works corectly
    # But there is a slight bit of inconvenience(неудобство) in that the connect to
    # function is kinna defined as a freestanding function
    # What if it were possible to just introduce some sort of base class
    # that connect_to would be directly tied to Neuron and NeuronLayer
    # and in fact its possible
    # implement class connectable
    # after implementing connect_to method is available through class method of both classes

