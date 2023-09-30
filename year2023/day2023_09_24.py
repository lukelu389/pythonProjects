# class DoublyLinkedList():
#     class Node():
#         def __init__(self, data):
#             self.data = data
#             self.prev = None
#             self.next = None
#
#     def __init__(self):
#         self.head = self.Node(None)
#         self.tail = self.Node(None)
#         self.tail.prev = self.head
#         self.head.next = self.tail
#
#     # add value in the end
#     def append(self, data):
#         new_node = self.Node(data)
#         new_node.prev = self.tail.prev
#         new_node.next = self.tail
#         self.tail.prev.next = new_node
#         self.tail.prev = new_node
#class DoublyLinkedList():
#     class Node():
#         def __init__(self, data):
#             self.data = data
#             self.prev = None
#             self.next = None
#
#     def __init__(self):
#         self.head = self.Node(None)
#         self.tail = self.Node(None)
#         self.tail.prev = self.head
#         self.head.next = self.tail
#
#     # add value in the end
#     def append(self, data):
#         new_node = self.Node(data)
#         new_node.prev = self.tail.prev
#         new_node.next = self.tail
#         self.tail.prev.next = new_node
#         self.tail.prev = new_node
#
#     # add value in the beginning
#     def prepend(self, data):
#         new_node = self.Node(data)
#         new_node.prev = self.head
#         new_node.next = self.head.next
#         self.head.next.prev = new_node
#         self.head.next = new_node
#
#     def __str__(self):
#         result = ''
#         current = self.head
#         while current != None:
#             result += str(current.data) + "->"
#             current = current.next
#
#         return result
#
#     def delete(self, data):
#         current = self.head
#         while current != None:
#             if current.data == data:
#                 if current.prev != None:
#                     current.prev.next = current.next
#                 if current.next != None:
#                     current.next.prev = current.prev
#
#     def insert_before(self, node_data, data):
#         new_node = self.Node(data)
#         current = self.head
#
#         while current.next.data != node_data:
#             current = current.next
#
#         new_node.next = current.next
#         current.next = new_node
#         new_node.prev = current
#         new_node.next.prev = new_node
#
#
# l = DoublyLinkedList()
# l.append(1)
# l.append(2)
# l.prepend(3)
# l.insert_before(1, 5)
# print(l)
#     # add value in the beginning
#     def prepend(self, data):
#         new_node = self.Node(data)
#         new_node.prev = self.head
#         new_node.next = self.head.next
#         self.head.next.prev = new_node
#         self.head.next = new_node
#
#     def __str__(self):
#         result = ''
#         current = self.head
#         while current != None:
#             result += str(current.data) + "->"
#             current = current.next
#
#         return result
#
#     def delete(self, data):
#         current = self.head
#         while current != None:
#             if current.data == data:
#                 if current.prev != None:
#                     current.prev.next = current.next
#                 if current.next != None:
#                     current.next.prev = current.prev
#
#     def insert_before(self, node_data, data):
#         new_node = self.Node(data)
#         current = self.head
#
#         while current.next.data != node_data:
#             current = current.next
#
#         new_node.next = current.next
#         current.next = new_node
#         new_node.prev = current
#         new_node.next.prev = new_node
#
#
# l = DoublyLinkedList()
# l.append(1)
# l.append(2)
# l.prepend(3)
# l.insert_before(1, 5)
# print(l)



# def faulty_keyboard(sample):
#     output = ""
#     for i in sample:
#         if i != "i":
#             output += i
#
#         else:
#             output = output[::-1]
#
#     return output


# this question consists three inputs: starting number of transistors, starting year, and year gap
# my example is the way I used to tackle problems, your project might vary
# I will try my best to mimic the same output of the desired program of the demo

# inputs
transistors = int(input("Starting Number of transistors: "))
starting_year = int(input("Starting Year: "))
num_of_years = int(input("Total Number of Years: "))

# the question itself is not hard, but the way to achieve the desired output is quite hard
# the solution of the problem is essentially, an exponential function
unit = "FLOPS"
flops = transistors * 50.00 # the number of flops
full_number = flops # the last number of display
print("YEARS : TRANSISTORS : FLOPS :")
# start with a loop
for i in range(num_of_years//2 + 1):
# you only run the loop number of year times // 2, but also count the starting year.
    # the loop to determine the unit of the flops
    count = 0 # the prefix i.e. "kilo", "mega", "giga", etc.
    while flops / 1000 > 1:
        flops /= 1000
        count += 1

    if count == 1:
        unit = "kiloFLOPS"
    elif count == 2:
        unit = "megaFLOPS"
    elif count == 3:
        unit = "gigaFLOPS"
    elif count == 4:
        unit = "teraFLOPS"
    elif count == 5:
        unit = "petaFLOPS"
    elif count == 6:
        unit = "exaFLOPS"
    elif count == 7:
        unit = "zettaFLOPS"
    elif count == 8:
        unit = "yottaFLOPS"

    print(str(starting_year) + " " + f"{transistors:,}" + " " + f"{flops:.2f}" + " " + unit + " " + f"{int(full_number):,}")
    starting_year += 2
    transistors *= 2
    flops = full_number * 2
    full_number = flops



