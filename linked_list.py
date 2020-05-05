# linked_list.py
# ===================================================
# Linked list exploration
# Part 1: implement the deque and bag ADT with a Linked List
# Part 2: implement the deque ADT with a CircularlyDoubly-
# Linked List
# ===================================================


'''
**********************************************************************************
Part1: Deque and Bag implemented with Linked List
**********************************************************************************
'''

class SLNode:
    def __init__(self):
        self.next = None
        self.data = None


class LinkedList:
    def __init__(self, start_list=None):
        """
        Initializes a linked list with a head and tail node with None data
        """
        self.head = SLNode()
        self.tail = SLNode()
        self.head.next = self.tail

        # populate list with initial set of nodes (if provided)
        if start_list is not None:
            for data in start_list:
                self.add_back(data)

    def __str__(self):
        """
        Returns a human readable string of the list content of the form
        [value1 -> value2 -> value3]

        An empty list should just return []

        Returns:
            The string of the human readable list representation
        """
        out = '['
        if self.head.next != self.tail:             
            cur = self.head.next.next
            out = out + str(self.head.next.data)
            while cur != self.tail:
                out = out + ' -> ' + str(cur.data)
                cur = cur.next
        out = out + ']'
        return out


    def add_link_before(self, data, index):
        """
        Adds a new link containing data and inserts it before the link at index.
        If index is 0, it inserts at the beginning of the list.

        Args:
            data: The data the new node will contain
            index: The index of the node that will immediately follow the newly added node
        """
        new_link = SLNode()  # initialize a new link
        new_link.data = data  # set new_link data

        # FIXED
        if index < 0:
            raise Exception("Index out of bounds")
        # find cur node, cur is index-1 node
        i = 0
        cur = self.head
        while i < index:
            if cur.next == self.tail:
                raise Exception("Index out of bounds")
            cur = cur.next
            i = i + 1
        # cur.next is not self.tail, already raise exception above
        new_link.next = cur.next
        cur.next = new_link

    def remove_link(self, index):
        """
        Removes the link at the location specified by index
        Args:
            Index: The index of the node that will be removed
        """

        # FIXED
        if index < 0:
            raise Exception("Index out of bounds")
        # find cur node, cur is index-1 node
        i = 0
        cur = self.head
        while i < index:
            if cur.next == self.tail:
                raise Exception("Index out of bounds")
            cur = cur.next
            i = i + 1
        #cur.next is not self.tail, already raise exception above
        cur.next = cur.next.next

    def add_front(self, data):
        """
        Adds a new node after the head that contains data

        Args:
            data: The data the new node will contain
        """
        new_link = SLNode()  # initialize a new link
        new_link.data = data  # set new_link data

        # FIXED
        new_link.next = self.head.next
        self.head.next = new_link

    def add_back(self, data):
        """
        Adds a new node before the tail that contains data

        Args:
            data: The data the new node will contain
        """
        new_link = SLNode()  # initialize a new link
        new_link.data = data  # set new_link data

        # FIXED
        # cur is back node, cur.next == self.tail
        cur = self.head
        while cur.next != self.tail:
            cur = cur.next
        new_link.next = self.tail
        cur.next = new_link

    def get_front(self):
        """
        Returns the data in the element at the front of the list. Will return
        None in an empty list.

        Returns:
            The data in the node at index 0 or None if there is no such node
        """

        # FIXED
        if self.head.next == self.tail:
            return None
        else:
            return self.head.next.data

    def get_back(self):
        """
        Returns the data in the element at the end of the list. Will return
        None in an empty list.

        Returns:
            The data in the node at last index of the list or None if there is no such node
        """

        # FIXED
        # cur is back node, cur.next == self.tail
        cur = self.head
        if cur.next == self.tail:
            return None
        else:
            while cur.next != self.tail:
                cur = cur.next
            return cur.data

    def remove_front(self):
        """
        Removes the first element of the list. Will not remove the tail.
        """

        # FIXED
        if self.head.next == self.tail:
            pass
        else:
            self.head.next = self.head.next.next

    def remove_back(self):
        """
        Removes the last element of the list. Will not remove the head.
        """

        # FIXED
        # cur is front node of back node, cur.next.next == self.tail
        cur = self.head
        if cur.next == self.tail:
            pass
        else:
            while cur.next.next != self.tail:
                cur = cur.next
            cur.next = self.tail

    def is_empty(self):
        """
        Checks if the list is empty

        Returns:
            True if the list has no data nodes, False otherwise
        """

        # FIXED
        if self.head.next == self.tail:
            return True
        else:
            return False

    def contains(self, value):
        """
        Checks if any node contains value

        Args:
            value: The value to look for

        Returns:
            True if value is in the list, False otherwise
        """

        # FIXED
        # cur is node to check, check until cur = tail
        cur = self.head.next
        while cur != self.tail:
            if cur.data == value:
                return True
            cur = cur.next
        return False

    def remove(self, value):
        """
        Removes the first instance of an element from the list

        Args:
            value: the value to remove
        """

        # FIXED
        # cur is front node of node to remove, cur.next == node_match_value
        cur = self.head
        if cur.next == self.tail:
            pass
        else:
            while cur.next.data != value and cur.next != self.tail:
                cur = cur.next
            if cur.next == self.tail:
                pass
            else:
                cur.next = cur.next.next

'''
**********************************************************************************
Part 2: Deque implemented with CircularlyDoublyLinked List
**********************************************************************************
'''

class DLNode:
    def __init__(self):
        self.next = None
        self.prev = None
        self.data = None

class CircularList:
    def __init__(self, start_list=None):
        """
        Initializes a linked list with a single sentinel node containing None data
        """
        self.sentinel = DLNode()
        self.sentinel.next = self.sentinel
        self.sentinel.prev = self.sentinel

        # populate list with initial set of nodes (if provided)
        if start_list is not None:
            for data in start_list:
                self.add_back(data)

    def __str__(self):
        """
        Returns a human readable string of the list content of the form
        [value1 <-> value2 <-> value3]

        An empty list should just print []

        Returns:
            The string of the human readable list representation
        """
        out = '['
        if self.sentinel.prev != self.sentinel:             
            cur = self.sentinel.next.next
            out = out + str(self.sentinel.next.data)
            while cur != self.sentinel:
                out = out + ' <-> ' + str(cur.data)
                cur = cur.next
        out = out + ']'
        return out

    def add_link_before(self, data, index):
        """
        Adds a new link containing data and inserts it before the link at index.
        If index is 0, it inserts at the beginning of the list.

        Args:
            data: The data the new node will contain
            index: The index of the node that will immediately follow the newly added node
        """
        new_link = DLNode()  # initialize a new link
        new_link.data = data  # set new_link data

        # FIXED
        if index < 0:
            raise Exception("Index out of bounds")
        # find cur node, cur is index-1 node
        i = 0
        cur = self.sentinel
        while i < index:
            if cur.next == self.sentinel:
                raise Exception("Index out of bounds")
            cur = cur.next
            i = i + 1
        # cur.next is not self.sentinel, already raise exception above
        new_link.prev = cur
        new_link.next = cur.next
        cur.next.prev = new_link
        cur.next = new_link


    def remove_link(self, index):
        """
        Removes the link at the location specified by index
        Args:
            Index: The index of the node that will be removed
        """

        # FIXED
        if index < 0:
            raise Exception("Index out of bounds")
        # find cur node, cur is index-1 node
        i = 0
        cur = self.sentinel
        while i < index:
            if cur.next == self.sentinel:
                raise Exception("Index out of bounds")
            cur = cur.next
            i = i + 1
        #cur.next is not self.sentinel, already raise exception above
        cur.next = cur.next.next
        cur.next.next.prev = cur

    def add_front(self, data):
        """
        Adds a new node at the beginning of the list that contains data

        Args:
            data: The data the new node will contain
        """
        new_link = DLNode()  # initialize a new link
        new_link.data = data  # set new_link data

        # FIXED
        new_link = SLNode()  # initialize a new link
        new_link.data = data  # set new_link data

        # FIXED
        new_link.next = self.sentinel.next
        new_link.prev = self.sentinel
        self.sentinel.next.prev = new_link
        self.sentinel.next = new_link

    def add_back(self, data):
        """
        Adds a new node at the end of the list that contains data

        Args:
            data: The data the new node will contain
        """
        new_link = DLNode()  # initialize a new link
        new_link.data = data  # set new_link data

        # FIXED
        new_link.next = self.sentinel
        new_link.prev = self.sentinel.prev
        self.sentinel.prev.next = new_link
        self.sentinel.prev = new_link

    def get_front(self):
        """
        Returns the data in the element at the front of the list. Will return
        None in an empty list.

        Returns:
            The data in the node at index 0 or None if there is no such node
        """

        # FIXED
        if self.sentinel.next == self.sentinel:
            return None
        else:
            return self.sentinel.next.data


    def get_back(self):
        """
        Returns the data in the element at the end of the list. Will return
        None in an empty list.

        Returns:
            The data in the node at last index of the list or None if there is no such node
        """

        # FIXED
        if self.sentinel.next == self.sentinel:
            return None
        else:
            return self.sentinel.prev.data


    def remove_front(self):
        """
        Removes the first element of the list. Will not remove the tail.
        """

        # FIXED
        if self.sentinel.next == self.sentinel:
            pass
        else:
            self.sentinel.next = self.sentinel.next.next
            self.sentinel.next.next.prev = self.sentinel


    def remove_back(self):
        """
        Removes the last element of the list. Will not remove the head.
        """

        # FIXED
        if self.sentinel.next == self.sentinel:
            pass
        else:
            self.sentinel.prev.prev.next = self.sentinel
            self.sentinel.prev = self.sentinel.prev.prev

    def is_empty(self):
        """
        Checks if the list is empty

        Returns:
            True if the list has no data nodes, False otherwise
        """

        # FIXED
        if self.sentinel.next == self.sentinel:
            return True
        else:
            return False


    def contains(self, value):
        """
        Checks if any node contains value

        Args:
            value: The value to look for

        Returns:
            True if value is in the list, False otherwise
        """

        # FIXED
        # cur is node to check, check until cur = sentinel
        cur = self.sentinel.next
        while cur != self.sentinel:
            if cur.data == value:
                return True
            cur = cur.next
        return False

    def remove(self, value):
        """
        Removes the first instance of an element from the list

        Args:
            value: the value to remove
        """

        # FIXED
        cur = self.sentinel
        if cur.next == self.sentinel:
            pass
        else:
            while cur.next.data != value and cur.next != self.sentinel:
                cur = cur.next
            if cur.next == self.sentinel:
                pass
            else:
                cur.next = cur.next.next
                cur.next.next.prev = cur

    def circularListReverse(self):
        """
        Reverses the order of the links. It must not create any additional new links to do so.
        (e.g. you cannot call DLNode()). If the list printed by following next was 0, 1, 2, 3,
        after the call it will be 3,2,1,0
        """

        # FIXED
        if self.sentinel.next == self.sentinel:
            return
        cur = self.sentinel
        prv = self.sentinel.prev
        temp = None
        while cur.next != self.sentinel:
            # save cur next node
            temp = cur.next
            # exchange direction
            cur.next = prv
            prv.prev = cur
            # move on
            prv = cur
            cur = temp
        cur.next = prv
        self.sentinel.next = cur


