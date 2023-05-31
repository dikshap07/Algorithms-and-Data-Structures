# Implementing Stack using a list


class listStack:
    def __init__(self):
        self._liststack = []

    def push(self, new_element):
        """To add new element to the stack"""

        self._liststack.append(new_element)

        return self.liststack

    def pop(self):
        """To remove and remove the next item in LIFO order"""

        self._liststack.pop()

    def peek(self):
        """To return the next item in LIFO order"""

        return self._liststack[-1]

    def size(self):
        """To get the size of the stack"""
        return len(self._liststack)

    def isempty(self):
        return len(self._liststack) == 0
