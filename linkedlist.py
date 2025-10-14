class Student:
    def __init__(self, roll_no, name, marks):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_student(self, roll_no, name, marks):
        new_student = Student(roll_no, name, marks)
        if self.head is None:
            self.head = new_student
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_student
        print("Student added")

    def delete_student(self, roll_no):
        if not self.head:
            print("List is empty")
            return

        if self.head.roll_no == roll_no:
            self.head = self.head.next
            print("Student deleted")
            return

        prev = self.head
        curr = self.head.next

        while curr and curr.roll_no != roll_no:
            prev = curr
            curr = curr.next

        if not curr:
            print("Student not found")
            return

        prev.next = curr.next
        print("Student deleted")

    def update_student(self, roll_no):
        temp = self.head
        while temp and temp.roll_no != roll_no:
            temp = temp.next

        if not temp:
            print("Student not found")
            return

        name = input("Enter new name: ")
        marks = int(input("Enter new marks: "))
        temp.name = name
        temp.marks = marks
        print("Student updated")

    def search_student(self, roll_no):
        temp = self.head
        while temp and temp.roll_no != roll_no:
            temp = temp.next

        if not temp:
            print("Student not found")
        else:
            print(f"Roll No: {temp.roll_no}, Name: {temp.name}, Marks: {temp.marks}")

    def display(self):
        if not self.head:
            print("No records found")
            return

        print("RollNo\tName\tMarks")
        temp = self.head
        while temp:
            print(f"{temp.roll_no}\t{temp.name}\t{temp.marks}")
            temp = temp.next

def main():
    srm = LinkedList()

    while True:
        print("\n1. Add Student")
        print("2. Delete Student")
        print("3. Update Student")
        print("4. Search Student")
        print("5. Display Students")
        print("6. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            roll_no = int(input("Roll No: "))
            name = input("Name: ")
            marks = int(input("Marks: "))
            srm.add_student(roll_no, name, marks)

        elif choice == "2":
            roll_no = int(input("Enter Roll No to delete: "))
            srm.delete_student(roll_no)

        elif choice == "3":
            roll_no = int(input("Enter Roll No to update: "))
            srm.update_student(roll_no)

        elif choice == "4":
            roll_no = int(input("Enter Roll No to search: "))
            srm.search_student(roll_no)

        elif choice == "5":
            srm.display()

        elif choice == "6":
            print("Program exited.")
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
