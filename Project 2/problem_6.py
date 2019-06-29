class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

def union(llist_1, llist_2):
    s1 = set()
    l1 = llist_1.head
    l2 = llist_2.head
    while (l1):
        s1.add(l1.value)
        l1=l1.next
    while (l2):
        s1.add(l2.value)
        l2=l2.next
    s3 = sorted(s1)
    newList = LinkedList()
    for val in s3:
        newList.append(val)
    return newList
    
def intersection(llist_1, llist_2):
    # Your Solution Here
    s1 = set()
    s2 = set()
    l1 = llist_1.head
    l2 = llist_2.head
    while (l1):
        s1.add(l1.value)
        l1=l1.next
    while (l2):
        s2.add(l2.value)
        l2=l2.next
    s3 = s1.intersection(s2)
    s3 = sorted(s3)
    newList = LinkedList()
    for val in s3:
        newList.append(val)
    return newList
    
# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2))  #1 -> 2 -> 3 -> 4 -> 6 -> 9 -> 11 -> 21 -> 32 -> 35 -> 65 -> 
print (intersection(linked_list_1,linked_list_2)) #4 -> 6 -> 21 -> 

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23] #1 -> 2 -> 3 -> 4 -> 6 -> 7 -> 8 -> 9 -> 11 -> 21 -> 23 -> 35 -> 65 -> 
element_2 = [1,7,8,9,11,21,4]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4))
print (intersection(linked_list_3,linked_list_4))

#Test case-3
linked_list_4 = LinkedList()
linked_list_5 = LinkedList()

element_1 = [1,2,4,5,5,66,7,9,10,74,81]
element_2 = []

for i in element_1:
    linked_list_4.append(i)

for i in element_2:
    linked_list_5.append(i)

print (union(linked_list_4,linked_list_5)) #1 -> 2 -> 4 -> 5 -> 7 -> 9 -> 10 -> 15 -> 17 -> 19 -> 23 -> 66 -> 74 -> 81 -> 
print (intersection(linked_list_4,linked_list_5)) #returns empty as all the elements in the list 2 is empty
