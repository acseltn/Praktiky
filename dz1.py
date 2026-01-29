class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

# Задание 1
print("1. Разворот списка:")
list1 = Node(1)
list1.next = Node(2)
list1.next.next = Node(3)

def reverse(head):
    prev = None
    curr = head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev

print("До:", list1.val, list1.next.val, list1.next.next.val)
new_head = reverse(list1)
print("После:", new_head.val, new_head.next.val, new_head.next.val)

# Задание 2
print("\n2. Кольцевой список:")
circle = Node(1)
circle.next = Node(2)
circle.next.next = Node(3)
circle.next.next.next = circle
print("Зациклено: 1 -> 2 -> 3 -> (возврат к 1)")

# Задание 3
print("\n3. Удаление хвоста в двусвязном списке:")
class DNode:
    def __init__(self, val):
        self.val = val
        self.prev = self.next = None

head = DNode(1)
mid = DNode(2)
tail = DNode(3)
head.next = mid
mid.prev = head
mid.next = tail
tail.prev = mid

tail = tail.prev
tail.next = None
print("После удаления: 1 <-> 2")
