class LLString:
    class Node:
        def __init__(self, val, next):
            self.val = val
            self.next = next

    def __init__(self, s):
        self.head = None
        self.tail = None

        for char in s:
            self.append(char)

    def append(self, new_val):
        new_node = LLString.Node(new_val, None)

        if self.tail is not None:
            self.tail.next = new_node
        self.tail = new_node

        if self.head is None:
            self.head = new_node

    def print(self):
        trav = self.head
        while trav is not None:
            print(trav.val, end='')
            trav = trav.next
        print()

    def to_string(self):
        s = ''
        trav = self.head
        while trav is not None:
            s += trav.val
            trav = trav.next
        return s

    def print_every_other(self):
        pass

    def char_at(self, i):
        pass

    def concat(self, other_llstring):
        pass

    def reverse(self):
        pass

    def index_of(self, c):
        pass
