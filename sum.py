class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def print_list(head):
    current = head
    while current:
        print(current.value, "-> ", end="")
        current = current.next
    print("NULL")

def push(head, data):
    node = Node(data)
    node.next = head
    return node

def reverse(head):
    out = None
    current = head

    while current:
        next_node = current.next
        current.next = out
        out = current
        current = next_node

    return out

def add(first, second):
    previous_node = None
    carry = 0

    while first or second:
        sum = 0
        if first:
            sum += first.value
            first = first.next
        if second:
            sum += second.value
            second = second.next
        sum += carry

        carry = sum // 10
        sum = sum % 10

        node = Node(sum)

        if not previous_node:
            previous_node = node
            head = node
        else:
            previous_node.next = node
            previous_node = node

    if carry != 0:
        node.next = Node(carry)

    return head

def create_num_list():
    head = None
    digits = input("Enter a number to add: ")
    numDigits = len(digits)
    val = 0

    for i in range(numDigits - 1, -1, -1):
        val = int(digits[i])

        head = push(head, val)

    return head

def print_ans(head):
    current = head
    while current:
        print(current.value, end="")
        current = current.next

if __name__ == "__main__":
    first = create_num_list()
    second = create_num_list()
    result = add(reverse(first), reverse(second))
    print_ans(reverse(result))