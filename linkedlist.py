class Node:
    def __init__(self, roll_no, name, marks):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks
        self.next = None

def main():
    head = None
    tail = None

    m = int(input("Enter the number of students: "))

    for i in range(m):
        print(f"\nEnter details for student {i + 1}:")
        roll_no = int(input("Roll No: "))
        name = input("Name: ")
        marks = float(input("Marks: "))

        temp = Node(roll_no, name, marks)

        if head is None:
            head = temp
            tail = temp
        else:
            tail.next = temp
            tail = temp

    print("\nStudent List:")
    curr = head
    while curr:
        print(f"Roll No: {curr.roll_no}, Name: {curr.name}, Marks: {curr.marks}")
        curr = curr.next

if __name__ == "__main__":
    main()
