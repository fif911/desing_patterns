from typing import Iterator


class Node:
    def __init__(self, value: str, left=None, right=None):
        self.right: Node = right
        self.left: Node = left
        self.value: str = value

        self.parent = None

        if left:
            self.left.parent = self
        if right:
            self.right.parent = self

    def traverse_preorder_initial(self):
        res = []  # THIS IS BAD

        def traverse(current: Node):
            if current is None:
                return

            print(f"Current: {current.value}")
            res.append(current.value)

            if current.left:
                print(f"Current: {current}; Left to go: {current.left.value}")
                traverse(current.left)
            if current.right:
                print(f"Current: {current}; Left to go: {current.right.value}")
                traverse(current.right)

        traverse(self)

        for n in res:
            yield n

    def traverse_preorder_middle(self):

        def traverse(current: Node) -> Iterator[int]:
            if current is None:
                return  # this is how we exit generator if needed

            print(f"Current: {current.value}")
            yield current.value

            # if current.left:
            #     print(f"Current: {current}; Left to go: {current.left.value}")
            for n in traverse(current.left):
                yield n  # Work with the left-hand node

            # if current.right:
            #     print(f"Current: {current}; Left to go: {current.right.value}")
            for n in traverse(current.right):
                yield n

        for n in traverse(self):
            yield n

    def traverse_preorder(self):  # Ideal

        def traverse(current: Node) -> Iterator[str]:
            if current is None:
                return  # this is how we exit generator if needed

            print(f"Current: {current.value}")
            yield current.value  # This actually returns a node

            # for left_node in traverse(current.left):  # Work with the left-hand node
            #     yield left_node  # this returns the result that is returned by the iterator
            yield from traverse(current.left)

            # for right_node in traverse(current.right):  # Work with the right-hand node
            #     yield right_node
            yield from traverse(current.right)

        # for n in traverse(self):
        #     yield n.value
        yield from traverse(self)

    def traverse_preorder_reduced(self) -> Iterator[str]:
        print(f"Current: {self.value}")
        yield self.value  # This actually returns a node

        if self.left:
            yield from self.left.traverse_preorder_reduced()
        if self.right:
            yield from self.right.traverse_preorder_reduced()


if __name__ == '__main__':
    # F B A D C E G I H

    n_b = Node(
        "B",
        Node("A"),
        Node("D",
             Node("C"),
             Node("E"))
    )
    n_g = Node("G",
               None,
               Node("I", Node("H"), None)
               )

    root = Node("F", n_b, n_g)
    # print([x for x in root.traverse_preorder()])
    # for x in root.traverse_preorder():
    #     print(x)
    res = list(root.traverse_preorder())
    print(f"\nFinal result My Implementation: {res}\n")

    res = list(root.traverse_preorder_reduced())
    print(f"\nFinal result Exemplar Implementation: {res}")
