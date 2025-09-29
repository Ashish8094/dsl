# Node for the Linked List
class Node:
    def _init_(self, asc_num, bookname):
        self.asc_num = asc_num
        self.bookname = bookname
        self.next = None

class LinkedList:
    def _init_(self):
        self.head = None

    def insert(self, asc_num, bookname):
        n1 = Node(asc_num, bookname)
        if not self.head:
            self.head = n1
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = n1

    def search(self, asc_num):
        t = self.head
        while t:
            if t.asc_num == asc_num:
                return t.asc_num, t.bookname
            t = t.next
        return -1

    def delete(self, asc_num):
        temp = self.head
        prev = None
        while temp:
            if temp.asc_num == asc_num:
                if prev:
                    prev.next = temp.next
                else:
                    self.head = temp.next
                return True
            prev = temp
            temp = temp.next
        return False

    def _str_(self):
        result = []
        temp = self.head
        while temp:
            result.append(f"({temp.asc_num}, {temp.bookname})")
            temp = temp.next
        return " -> ".join(result) if result else "Empty"


class HashTable:
    def _init_(self):
        self.table = [LinkedList() for _ in range(10)]

    def hash(self, asc_num):
        return asc_num % 10

    def insert(self, asc_num, bookname):
        index = self.hash(asc_num)
        self.table[index].insert(asc_num, bookname)

    def search(self, asc_num):
        index = self.hash(asc_num)
        return self.table[index].search(asc_num)

    def delete(self, asc_num):
        index = self._hash(asc_num)
        return self.table[index].delete(asc_num)

    def display(self):
        for i, linked_list in enumerate(self.table):
            print(f"Index {i}: {linked_list}")


ht = HashTable()
while True:
    print("\nMenu:")
    print("1. Insert book")
    print("2. Search book")
    print("3. Delete book")
    print("4. Display hash table")
    print("5. Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        asc_num = int(input("Enter accession number: "))
        bookname = input("Enter book name: ")
        ht.insert(asc_num, bookname)
        print("Book inserted.")
    elif choice == '2':
        asc_num = int(input("Enter accession number to search: "))
        result = ht.search(asc_num)
        if result == -1:
            print("Book not found.")
        else:
            print(f"Book found: Accession Number: {result[0]}, Name: {result[1]}")
    elif choice == '3':
        asc_num = int(input("Enter accession number to delete: "))
        if ht.delete(asc_num):
            print("Book deleted.")
        else:
            print("Book not found.")
    elif choice == '4':
        ht.display()
    elif choice == '5':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")
