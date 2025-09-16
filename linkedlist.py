class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def main():
    head = None
    tail = None

    n = int(raw_input("Enter the number of nodes: "))
    print "Enter the elements: "
    
    # read all elements in one line and split
    elements = map(int, raw_input().split())

    for x in elements[:n]:   # take only n elements
        temp = Node(x)
        if head is None:
            head = temp
            tail = temp
        else:
            tail.next = temp
            tail = temp

    print "Elements of linked list are:",
    current = head
    while current is not None:
        print current.data,
        current = current.next
    print


if __name__ == "__main__":
    main()
