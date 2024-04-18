class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

def insert_at_head(head, data):
  new_node = Node(data)
  new_node.next = head 
  return new_node

def print_linked_list(head):
  while head:
    print(head.data, end=" ")
    head = head.next
  print()

n = int(input("Enter the number of elements to be inserted at the head: "))
head = None

for _ in range(n):
  data = int(input("Enter the element to be inserted: "))
  head = insert_at_head(head, data)

print("Linked List after insertion: ", end="")
print_linked_list(head)
