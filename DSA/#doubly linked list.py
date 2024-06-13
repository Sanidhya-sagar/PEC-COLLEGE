#doubly linked list

i = 0
class node:
	def __init__(self, k=0, p=None, n=None):
		self.key = k
		self.prev = p
		self.next = n

head = None
first = None
temp = None
tail = None

def addnode(k: int):
	global i, head, first, tail
	ptr = node(k)

	if head == None:
		head = ptr
		first = head
		tail = head

	else:
		temp = ptr
		first.next = temp
		temp.prev = first
		first = temp
		tail = temp

	i += 1

def traverse():
	ptr = head

	while ptr != None:

		print(ptr.key, end=" ")
		ptr = ptr.next

	print()

def insertatbegin(k: int):
	global head, first, tail, i

	ptr = node(k)

	if head == None:
		first = ptr
		first = head
		tail = head

	else:
		temp = ptr
		temp.next = head
		head.prev = temp
		head = temp

	i += 1

def insertatend(k: int):
	global head, first, tail, i

	ptr = node(k)

	if head == None:
		first = ptr
		first = head
		tail = head

	else:
		temp = ptr
		temp.prev = tail
		tail.next = temp
		tail = temp

	i += 1

def insertatpos(k: int, pos: int):
	global i

	if pos < 1 or pos > i + 1:
		print("Please enter a" " valid position")

	elif pos == 1:
		insertatbegin(k)

	elif pos == i + 1:
		insertatend(k)

	else:
		src = head

		while pos:
			pos -= 1
			src = src.next

		ptr = node(k)

		ptr.next = src
		ptr.prev = src.prev
		src.prev.next = ptr
		src.prev = ptr
		i += 1

def delatbegin():
	
	global head, i
	head = head.next
	i -= 1

def delatend():
	
	global tail, i
	tail = tail.prev
	tail.next = None
	i -= 1

def delatpos(pos: int):
	global i
	
	if pos < 1 or pos > i + 1:
		print("Please enter a" " valid position")

	elif pos == 1:
		delatbegin()

	elif pos == i:
		delatend()

	else:
		src = head
		pos -= 1

		while pos:
			pos -= 1
			src = src.next
		src.prev.next = src.next
		src.next.prev = src.prev
		i -= 1



if __name__ == "__main__":
	# Adding node to the linked List
	addnode(2)
	addnode(4)
	addnode(9)
	addnode(1)
	addnode(21)
	addnode(22)

	# To print the linked List
	print("Linked List: ")
	traverse()

	print("\n")

	# To insert node at the beginning
	insertatbegin(1)
	print("Linked List after inserting 1 at beginning: ")
	traverse()

	# To insert at the end
	insertatend(0)
	print("Linked List after inserting 0 at end: ")
	traverse()

	# To insert Node with
	# value 44 after 3rd Node
	insertatpos(44, 3)
	print("Linked List after inserting 44 after 3rd Node: ")
	traverse()

	print("\n")

	# To delete node at the beginning
	delatbegin()
	print("Linked List after deleting node at beginning: ")
	traverse()

	# To delete at the end
	delatend()
	print("Linked List after deleting node at end: ")
	traverse()

	# To delete Node at position 5
	print("Linked List after deleting node at position 5: ")
	delatpos(5)
	traverse()
