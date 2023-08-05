class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def multiply(num1, num2):
    n1 = len(num1)
    n2 = len(num2)
    num1 = num1[::-1]
    num2 = num2[::-1]
    result = [0] * (n1 + n2)

    for i in range(n1):
        for j in range(n2):
            digit1 = int(num1[i])
            digit2 = int(num2[j])
            product = digit1 * digit2

            result[i + j] += product

    carry = 0
    for i in range(len(result)):
        temp = result[i] + carry
        result[i] = temp % 10
        carry = temp // 10
        
    result.reverse()
    result_str = "".join(str(digit) for digit in result)
    
    if result_str[0] == "0" and result_str[1] == "0":
        return "0"
    elif result_str[0] == "0":
        return result_str[1:]
    
    return result_str

def add(head1, head2):
    carry = 0
    dummy = Node(0)
    tail = dummy

    while head1 or head2:
        val1 = head1.value if head1 else 0
        val2 = head2.value if head2 else 0

        sum = val1 + val2 + carry
        carry = sum // 10
        digit = sum % 10

        tail.next = Node(digit)
        tail = tail.next

        if head1:
            head1 = head1.next
        if head2:
            head2 = head2.next

    if carry > 0:
        tail.next = Node(carry)

    return dummy.next

def linked_list_to_string(head):
    result = ""
    current = head
    while current:
        result = str(current.value) + result
        current = current.next

    return result

if __name__ == "__main__":
    ans = multiply(input("Enter the first number: "), input("Enter the second number: "))
    print("Ans: ", ans)
    print("Number of digits: ", len(ans))