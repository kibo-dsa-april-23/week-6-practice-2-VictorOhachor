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
        print(self.__print_every_other(self.head, 0))
    
    def __print_every_other(self, node, idx):
        trav = node
        if trav is None:
            return ''

        if idx % 2:
            return self.__print_every_other(trav.next, idx + 1)
        else:
            return trav.val + self.__print_every_other(trav.next, idx + 1)

    def char_at(self, i):
        return self.__char_at(self.head, 0, i)
    
    def __char_at(self, node, current_idx, target_idx):
        if node is None:
            return None
        
        if current_idx == target_idx:
            return node.val
        return self.__char_at(node.next, current_idx + 1, target_idx)

    def concat(self, other_llstring):
        trav = other_llstring.head
        while trav is not None:
            self.append(trav.val)
            trav = trav.next
        return self.to_string()

    def reverse(self):
        self.__reverse(self.head, None)
        self.head, self.tail = self.tail, self.head
    
    def __reverse(self, current, previous):
        if current is None:
            return
        
        next_node = current.next
        current.next = previous

        self.__reverse(next_node, current)

    def index_of(self, c):
        return self.__index_of(self.head, c)
    
    def __index_of(self, node, c, idx=0):
        if node is None:
            return -1
        
        if node.val == c:
            return idx
        return self.__index_of(node.next, c, idx + 1)


if __name__ == "__main__":
    llstring = LLString('')
    print(llstring.index_of('i'))