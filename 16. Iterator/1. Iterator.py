"""
Iterate binary tree

Using:
1) constructs like __iter__ (usually stateful iterators hard to do right)
2) generators
"""


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right: Node = right
        self.left: Node = left

        self.parent = None  # will be set for all children

        if left:
            self.left.parent = self
        if right:
            self.right.parent = self

    def __iter__(self):
        """Expose our iterator from current node
        __iter__ makes our object ITERABLE
        """
        print("Node __iter__")

        return InOrderIterator(self)


class InOrderIterator:
    """We do separate class in the sake of SPR

    This is stateful iterator"""
    root: Node  # The root node
    current: Node  # Current node we are iterating on

    def __init__(self, root):
        self.root = self.current = root
        self.yielded_start = False
        while self.current.left:  # while there is a left element we iterate
            self.current = self.current.left

    # def __iter__(self): # This will make InOrderIterator
    #     return self

    def __next__(self):
        if not self.yielded_start:
            self.yielded_start = True
            return self.current

        if self.current.right:
            self.current = self.current.right
            while self.current.left:
                self.current = self.current.left
            return self.current
        else:
            p: Node = self.current.parent
            while p and self.current == p.right:
                self.current = p
                p = p.parent
            self.current = p
            if self.current:
                return self.current
            else:
                raise StopIteration


def traverse_in_order(root):
    print("traverse_in_order happening")

    def traverse(current):
        if current.left:
            for left in traverse(current.left):
                yield left
        yield current
        if current.right:
            for right in traverse(current.right):
                yield right

    for node in traverse(root):
        yield node


class NodeYieldTraversal(Node):
    def __iter__(self):
        print("NodeYieldTraversal __iter__")
        return traverse_in_order(self)


if __name__ == '__main__':
    #   1
    #  / \
    # 2  3
    # Traversal types:
    # in-order: 213 (this one implemented)
    # preorder: 123
    # postorder: 231

    root = Node(1,
                Node(2, Node(4), Node(5)),
                Node(3))

    # print([x.value for x in InOrderIterator(root)])  # IS NOT AN ITERABLE

    print("InOrderIterator it = iter(root)")
    it = iter(root)  # Get iterable object on which we can call __next__
    print([next(it).value for x in range(5)])

    # print("InOrderIterator for x in root")
    # for x in root:  # next is called implicitly
    #     print(x.value)
    #     pass
    print([x.value for x in root])

    print("\n" + "-" * 30 + "def traverse_in_order")
    for y in traverse_in_order(root):
        print(y.value)

    root_trav = NodeYieldTraversal(1,
                                   Node(2, Node(4), Node(5)),
                                   Node(3))

    print("NodeYieldTraversal it = iter(root)")
    print([x.value for x in root_trav])
