'''
ADT: Abstract Datastructure
defines the property and operation of data struture,
instead of giving the concrete implementation

Linked List (python implements it as list)
- singly linked list
- doubly linked list


singly linked list
keep elements inside a node in a certain order
node: it's an object that holds the element
'''

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
#     def __str__(self):
#         return str(self.data)
#
#
# class LinkedList:
#     def __init__(self):
#         self.head = None
#         self.size = 0
#
#     def add_first(self, node):
#         self.size += 1
#         if self.head is None:
#             self.head = node
#         else:
#             node.next = self.head
#             self.head = node
#
#     def remove_first(self):
#         first = self.head
#         self.head = self.head.next
#         first.next = None
#         self.size -= 1
#
#     def print_list(self):
#         current = self.head
#         while current is not None:
#             print(current)
#             current = current.next
#
#     def add_last(self, node):
#         self.size += 1
#         if self.head is None:
#             self.head = node
#             return
#         current = self.head
#         while current.next is not None:
#             current = current.next
#         current.next = node
#
#     def remove_last(self):
#         if self.head.next is None:
#             self.head = None
#         current = self.head
#         while current.next.next is not None:
#             current = current.next
#         current.next = None
#         self.size -= 1
#
#     # return true if list contains target, return false otherwise
#     def find(self, target):
#         current = self.head
#         while current.next is not None:
#             if current.data == target:
#                 return True
#             current = current.next
#         return False
#
#     # return number of nodes in list
#     def size(self):
#         return self.size
#
#
# linked_list = LinkedList()
# linked_list.add_first(Node(1))
# linked_list.add_first(Node(2))
# linked_list.add_first(Node(3))
# linked_list.add_first(Node(4))
# print(linked_list.size())

'''
How to use LinkedList class to behave like a stack
if only use add_first and remove_first, this class performs stack operation

if only use add_first and remove_last, this class performs as queue

circularly linked list

'''


# def array_sum(sample, k):
#     count = len(sample)
#     i = 0
#     s = 0
#     for j in range(len(sample)):
#         s += sample[j]
#         while s > k:
#             count = min(count, j - i + 1)
#             s -= sample[i]
#             i += 1
#
#     return count
#
#
# print(array_sum([2, 1, 5, 2, 3, 2], 7))


# l= {1, 2, 3, 4, 5, 6}
# s = {4, 5, 6, 7, 8, 9}
x = 7.0001
print(round(x, 2))
