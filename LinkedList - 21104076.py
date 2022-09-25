#Saksham Beniwal
#21104076
#EE

#Family Linked List Assignment

#----------Start----------#

print()

class Node: #class for creating node
    def __init__(self, previous_call, name, age, pointer, next_call):
        self.name = name
        self.age = age
        self.previous_call = previous_call
        self.pointer = pointer
        self.next_call = next_call
        self.next = None
        self.prev = None

class DoublyLinkedList: #class for creating doubly linked list
    def __init__(self):
        self.start_node = None
    
    def InsertToEmptyList(self, previous_call, name, age, pointer, next_call): #function to add a node to the empty linked list
        if self.start_node is None:
            new_node = Node(previous_call, name, age, pointer, next_call)
            self.start_node = new_node
        else:
            print("There is no list")

    def InsertToList(self, previous_call, name, age, pointer, next_call): #function to add more nodes
        
        if self.start_node is None:
            new_node = Node(previous_call, name, age, pointer, next_call)
            self.start_node = new_node
            return
        n = self.start_node
        
        while n.next is not None:
            n = n.next
        new_node = Node(previous_call, name, age, pointer, next_call)
        n.next = new_node
        new_node.prev = n

    def Display(self): #function to display the linked list
        if self.start_node is None:
            print("There is no list")
            return
        else:
            n = self.start_node
            while n is not None:
                print(n.pointer, "node", "==>", [n.previous_call, [n.name, n.age], n.next_call])
                n = n.next

FamilyLinkedList = DoublyLinkedList() #family double linked list
FamilyLinkedList.InsertToEmptyList("Null", "Subhash Chander", "50", "Father", "Son") #Father node
FamilyLinkedList.InsertToList("Father", "Saksham Beniwal", "19", "Son", "Mother") #Son node
FamilyLinkedList.InsertToList("Son", "Samesta", "44", "Mother", "Null") #Mother node
FamilyLinkedList.Display()

#How to read output:-
#LHS values are pointer address, the address are not actual values but a placeholder to explain double linked list that links family members
#RHS values are nodes in following format [call to previous node, [name of family member, age of family member], call to next node]

print()

#----------End----------#