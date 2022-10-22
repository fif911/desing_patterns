from typing import List, Any


class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def __repr__(self):
        return str(self.value)


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, node_value):
        # add node in the end
        self.length += 1

        if self.head is None:
            # if it's first node add node and make head and tail the same node
            # self.head = self.tail = Node(node_value, None)
            self.tail = Node(node_value, None)
            self.head = self.tail
        else:
            # if some Node are already in the list - add to tail new node
            # self.tail.next_node = self.tail = Node(node_value, None)
            new_node = Node(node_value, None)
            self.tail.next_node = new_node  # link current last node to new node
            self.tail = new_node  # set new node as a last node

    def push(self, node_value):
        # inserts a new node at the beginning
        new_node = Node(node_value)
        new_node.next_node = self.head
        self.head = new_node

    def insert_after(self, prev_node, node_value):
        # insert node after specific node

        # 1. check if the given prev_node exists
        if prev_node is None:
            print("The given previous node must be in LinkedList.")
            return

        new_node = Node(node_value)
        new_node.next = prev_node.next  # Make next of new Node as next of prev_node
        prev_node.next = new_node  # make next of prev_node as new_node

    def remove_node_by_value(self, node_value):
        # remove node by value in it
        pass

    def remove_node_by_index(self, node_index):
        # remove node by index number (starting from 0)
        pass

    def reverse(self):
        # reverse linked list
        previous_node = None
        current_node: Node = self.head
        next_node: Node = current_node.next_node
        self.tail = current_node

        while next_node is not None:
            current_node.next_node = previous_node  # the only thing that changes smth in our nodes. Others are needed for proper aceessing(memorization) nodes
            previous_node = current_node
            current_node = next_node
            next_node = current_node.next_node

        current_node.next_node = previous_node
        self.head = current_node

        pass

    def __repr__(self):
        node: Node = self.head
        nodes = []
        while node is not None:
            nodes.append(str(node.value))
            node = node.next_node

        nodes.append("None")
        return " -> ".join(nodes)

    def __iter__(self):
        #  Traverse a Linked List
        #  Traversing means going through every single node, starting with the head of the linked list and ending on
        #  the node that has a next value of None.
        node = self.head
        while node is not None:
            yield node
            node = node.next_node

    def __str__(self):
        return f"Linked list: {self.__repr__()}"


def reverse(data_set):
    # 4234
    # 4231
    # next loop
    # 4331
    # 4321
    # End loop. Cause  range(0,2) = [0,1]  and  (int(1.9) = 1)
    length = len(data_set)

    for i in range(0, int(length / 2)):
        length = length - 1
        hold = data_set[i]
        data_set[i] = data_set[length]
        data_set[length] = hold
    return data_set


if __name__ == '__main__':
    list = LinkedList()
    list.append("1")
    list.append("2")
    list.append(3)
    list.append(9)
    list.push(0)
    print(repr(list))
    list.reverse()
    print(repr(list))

    all_nodes = []
    for i in list:
        all_nodes.append(str(i))
    all_nodes.append('None')
    print('->'.join(all_nodes))
    del all_nodes

    print(f"Head: {list.head}")
    print(f"tail: {list.tail}")
    print(f"tail next node: {list.tail.next_node}")

    print("\nGetting list with generator:")
    for node in list:
        print(node, end=' ')
    print()

    list_to_reverse_ = [1, 2, 1000, 3, 4, 5, 6, 7, 10]
    reverse(list_to_reverse_)
    print(list_to_reverse_)
