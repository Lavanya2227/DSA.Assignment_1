#1.Delete the elements in an linked list whose sum is equal to zero


class Node():
    def __init__(self,value):
        self.value=value
        self.nextnode=None
class LinkedList():
    def __init__(self):
        self.head=None
    
    def add_element(self,value):
        node=Node(value)
        if self.head is None:
            self.head=node
            return
        crnt_node=self.head
        while True:
            if crnt_node.nextnode is None:
                crnt_node.nextnode=node
                break
            crnt_node=crnt_node.nextnode

    def print_llist(self):
        crnt_node=self.head     
        v_llist=[]
        while True:
            print(crnt_node.value,end='->')
            v_llist.append(crnt_node.value) 
            if crnt_node.nextnode is None:              
                break
            crnt_node=crnt_node.nextnode
        print('None')
        return v_llist
    def  print_modified_llist(self):
        p_add=0
        v_llist=self.print_llist()
       
        for i in range(len(v_llist)-1):
            p_add=p_add+v_llist[i]
        if v_llist[-1]>0 and p_add>0:
            print(p_add,v_llist[-1])
        elif v_llist[-1]<0 and p_add>0:
            print(p_add+v_llist[-1])
        elif v_llist[-1]<0 and p_add<0:
            print(v_llist[-1],p_add)
            

sll=LinkedList()
sll.add_element(2)
sll.print_llist()
sll.add_element(4)
sll.print_llist()
sll.add_element(6)
sll.print_llist()
sll.add_element(8)
sll.print_llist()
sll.add_element(10)
sll.print_llist()
sll.add_element(12)
sll.print_llist()
sll.add_element(-15)
sll.print_llist()
sll.add_element(17)
sll.print_llist()
sll.add_element(20)
sll.print_llist()
sll.add_element(-18)
sll.print_llist()
sll.print_modified_llist() 

#2.Reverse a linked list in groups of given size

class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
def reverse(head, k):

	if not head or k == 1:
		return head
	dummy = Node(-1) 
	dummy.next = head
	
	prev = dummy
	curr = dummy
	next = dummy
	count = 0
	toLoop = 0
	i = 0
	while curr:
		curr = curr.next
		count += 1
	while next:
		curr = prev.next 
		next = curr.next 
		toLoop = count > k and k or count - 1
		for i in range(1, toLoop):
				
			curr.next = next.next
			next.next = prev.next
			prev.next = next
			next = curr.next
		prev = curr
		count -= k

	
	return dummy.next
def printList(node):
	while node is not None:
		print(node.data, end=" ")
		node = node.next
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)
head.next.next.next.next.next.next = Node(7)
head.next.next.next.next.next.next.next = Node(8)
head.next.next.next.next.next.next.next.next = Node(9)
head.next.next.next.next.next.next.next.next.next= Node(10)
print("Given linked list")
printList(head)
head = reverse(head, 5)
print("\nReversed Linked list")
printList(head)

#3.Merge a linked list into another linked list at alternate positions.

class Node(object):
	def __init__(self, data:int):
		self.data = data
		self.next = None
class LinkedList(object):
	def __init__(self):
		self.head = None
		
	def push(self, new_data:int):
		new_node = Node(new_data)
		new_node.next = self.head
		
		self.head = new_node
		
	def printList(self):
		temp = self.head
		while temp != None:
			print(temp.data)
			temp = temp.next
			
	def merge(self, p, q):
		p_curr = p.head
		q_curr = q.head
		while p_curr != None and q_curr != None:


			p_next = p_curr.next
			q_next = q_curr.next
			q_curr.next = p_next 
			p_curr.next = q_curr 

			p_curr = p_next
			q_curr = q_next
			q.head = q_curr

llist1 = LinkedList()
llist2 = LinkedList()
llist1.push(1)
llist1.push(2)
llist1.push(3)
llist1.push(4)

for i in range(8, 3, -1):
	llist2.push(i)
print("First Linked List:")
llist1.printList()
print("Second Linked List:")
llist2.printList()
llist1.merge(p=llist1, q=llist2)
print("Modified first linked list:")
llist1.printList()
print("Modified second linked list:")
llist2.printList() 

#4.In an array, Count Pairs with given sum

def getPairsCount(arr, n, sum):

	count = 0
	for i in range(0, n):
		for j in range(i + 1, n):
			if arr[i] + arr[j] == sum:
				count += 1

	return count

arr = [1, 5, 8, 6, 1]
n = len(arr)
sum = 2
print("Count of pairs is",
	getPairsCount(arr, n, sum))

#5.Find duplicates in an array

numRay = [0,1,2,3,5,6,7,2,3,5,8,5,9,5]
arr_size = len(numRay)
for i in range(arr_size):

	x = numRay[i] % arr_size
	numRay[x] = numRay[x] + arr_size

print("The repeating elements are : ")
for i in range(arr_size):
	if (numRay[i] >= arr_size*2):
		print(i, " ")
		
#6.Find the Kth largest and Kth smallest number in an array

def kthSmallest(arr, j, K):
	arr.sort()
	return arr[K-1]
if __name__ == '__main__':
	arr = [15,13,9,19,2,5,7,17]
	j = len(arr)
	K = 4
	print("K'th smallest element is",
		kthSmallest(arr, j, K))
	
#7.Move all the negative elements to one side of the array

def move(arr):
  arr.sort()
 
arr = [ 1,-2,4,6,8,19,-13,-45]
move(arr)
for i in arr:
    print(i , end = " ")    

#8.Reverse a string using a stack data structure

def createStack():
	stack = []
	return stack
def size(stack):
	return len(stack)
def isEmpty(stack):
	if size(stack) == 0:
		return True
def push(stack, item):
	stack.append(item)
def pop(stack):
	if isEmpty(stack):
		return
	return stack.pop()

def reverse(string):
	n = len(string)
	stack = createStack()


	for i in range(0, n, 1):
		push(stack, string[i])
		
	string = ""

	for i in range(0, n, 1):
		string += pop(stack)

	return string
string = "LavanyaRamya"
string = reverse(string)
print("Reversed string is " + string)

#9.Evaluate a postfix expression using stack

class Evaluate:
	
	def __init__(self, capacity):
		self.top = -1
		self.capacity = capacity
		self.array = []
	
	def isEmpty(self):
		return True if self.top == -1 else False

	def peek(self):
		return self.array[-1]
	
	def pop(self):
		if not self.isEmpty():
			self.top -= 1
			return self.array.pop()
		else:
			return "$"
	
	def push(self, op):
		self.top += 1
		self.array.append(op)

	def evaluatePostfix(self, exp):
		
		for i in exp:
			
			if i.isdigit():
				self.push(i)

			else:
				val1 = self.pop()
				val2 = self.pop()
				self.push(str(eval(val2 + i + val1)))
				return int(self.pop())
				
exp = "475*+15-"
obj = Evaluate(len(exp))
print ("postfix evaluation: %d"%(obj.evaluatePostfix(exp)))

#10.Implement a queue using the stack data structure

class Queue:
    def __init__(self):
        self.in_stack = []    
        self.out_stack = []  

    def enqueue(self, item):
        self.in_stack.append(item)

    def dequeue(self):
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        if not self.out_stack:
            return None  
        return self.out_stack.pop()

    def is_empty(self):
        return not self.in_stack and not self.out_stack

    def size(self):
        return len(self.in_stack) + len(self.out_stack)
q = Queue()
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
q.enqueue(6)
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())    
print(q.dequeue())    

   
            


        
