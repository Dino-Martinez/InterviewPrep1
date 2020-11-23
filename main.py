from linkedlist import LinkedList
from stack import Stack
#1. Use your linked list code and add a method called reverse() that will reverse the linked list. You can start with making a reversed copy and build up to reversing the linked list "in place" as a strecth goal. For example if your linked list is 3->5->6 your function will return 6->5->3
ll = LinkedList()
ll.append(3)
ll.append(5)
ll.append(6)
print('Reversing a list:')
ll.print()
ll.reverse().print()

#2. Write a function called reverse_num() that will reverse an integer using a stack. For example if the integer is 123 your function will return 321, make sure to use a stack!
def reverse_num(num):
  # build the stack
  my_stack = Stack()
  for digit in str(num):
    my_stack.push(int(digit))
  
  # build the reversed integer by popping from the stack
  # this utilizes the stack's FILO nature
  reversed_int = 0
  while my_stack.size() > 0:
    reversed_int *= 10
    reversed_int += my_stack.pop()

  return reversed_int
print('Reversing an integer using a stack:')
print(reverse_num(12345))
print(reverse_num(573718901924))
    

#3. Write a recursive function called sum_num that will take in a list and return the sum of all the elements in the list starting. For example if the list is [5, 4, 1] your funtion will return 10. Be sure to use recursion!
def sum_num(digit, accumulator=0):
  accumulator += int(digit._data)
  if (digit._next is None):
    return accumulator
  digit = digit._next
  return sum_num(digit, accumulator)

print('Summing the integers in a list:')

# should be 3 + 5 + 6 = 14
print(sum_num(ll.head))

ll.append(12)
ll.append(8)

# should be 14+12+8=34
print(sum_num(ll.head))
