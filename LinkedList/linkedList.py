# Define your Node class below:
class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    def set_next_node(self, next_node):
        self.next_node = next_node

    def get_next_node(self):
        return self.next_node

    def get_value(self):
        return self.value


class LinkedList:
    def __init__(self, value=None):
        self.head_node = Node(value)

    def get_head_node(self):
        return self.head_node

    def insert_beginning(self, new_value):
        new_node = Node(new_value)
        new_node.next_node = self.head_node
        self.head_node = new_node

    def stringify_list(self):
        string_list = ''
        current_node = self.get_head_node()
        while current_node:
            string_list += str(current_node.get_value())+'\n'
            current_node = current_node.get_next_node()
        return string_list

    def remove_node(self, value_to_remove):
        current_node = self.head_node
        if current_node.get_value() == value_to_remove:
            self.head_node = current_node.get_next_node()
        else:
            while current_node:
                next_node = current_node.get_next_node()
                if next_node.get_value() == value_to_remove:
                    current_node.set_next_node(next_node.get_next_node())
                    current_node = None
                else:
                    current_node = next_node

    def swap_nodes(self, input_list, val1, val2):
        '''The worst case for time complexity in swap_nodes() 
        is if both while loops must iterate all the way through 
        to the end (either if there are no matching nodes, or if 
        the matching node is at the tail). This means that it 
        has a linear big O runtime of O(n), since each while loop 
        has a O(n) runtime, and constants are dropped.
        There are four new variables created in the function 
        regardless of the input, which means that it has a constant 
        space complexity of O(1).'''

        print(f'Swapping {val1} with {val2}')

        self.node1_prev = None
        self.node2_prev = None
        self.node1 = self.head_node
        self.node2 = self.head_node

        if val1 == val2:
            print("Elements are the same - no swap needed")
            return

        while self.node1 is not None:
            if self.node1.get_value() == val1:
                break
            self.node1_prev = self.node1
            self.node1 = self.node1.get_next_node()

        while self.node2 is not None:
            if self.node2.get_value() == val2:
                break
            self.node2_prev = self.node2
            self.node2 = self.node2.get_next_node()

        if (self.node1 is None or self.node2 is None):
            print("Swap not possible - one or more element is not in the list")
            return

        if self.node1_prev is None:
            input_list.head_node = self.node2
        else:
            self.node1_prev.set_next_node(self.node2)

        if self.node2_prev is None:
            input_list.head_node = self.node1
        else:
            self.node2_prev.set_next_node(self.node1)

        temp = self.node1.get_next_node()
        self.node1.set_next_node(self.node2.get_next_node())
        self.node2.set_next_node(temp)

    def nth_last_node(self, n):
        current = None
        tail_seeker = self.head_node
        count = 1
        while tail_seeker:
            tail_seeker = tail_seeker.get_next_node()
            count += 1
            if count >= n + 1:
                if current is None:
                    current = self.head_node
                else:
                    current = current.get_next_node()
        return current

    def find_middle(self):
        fast = self.head_node
        slow = self.head_node
        while fast:
            fast = fast.get_next_node()
            if fast:
                fast = fast.get_next_node()
                slow = slow.get_next_node()
        return slow

    def find_middle_alt(self):
        '''This function moves the fast pointer once with each loop 
        iteration but only slow pointer every other time'''
        count = 0
        fast = self.head_node
        slow = self.head_node
        while fast:
            fast = fast.get_next_node()
            if count % 2 != 0:
                slow = slow.get_next_node()
            count += 1
        return slow
# ll = LinkedList()
# for i in range(10):
#   ll.insert_beginning(i)

# print(ll.stringify_list())
# ll.swap_nodes(ll, 9, 5)
# print(ll.stringify_list())
