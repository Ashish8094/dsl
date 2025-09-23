#include <bits/stdc++.h>
using namespace std;

class Student {
public:
    int rollNo;
    string name;
    int marks;
    Student* next;

    Student(){
        this->next = NULL;
    }

    Student(int r, string n, int m) {
        this->rollNo = r;
        this->name = n;
        this->marks = m;
        this->next = nullptr;
    }
};

class linkedlist {
    Student* head;

public:
    linkedlist() {
        head = NULL;
    }

    void addStudent(int rollNo, string name, int marks) {
        Student* newStudent = new Student(rollNo, name, marks);
        if (head == nullptr) {
            head = newStudent;
        } else {
            Student* temp = head;
            while (temp->next != nullptr)
                temp = temp->next;
                temp->next = newStudent;
        }
        cout << "Student added"<< endl;
    }

 void deleteStudent(int rollNo) {
    if (!head) {
        cout << "List is empty"<<endl;
        return;
    }

    if (head->rollNo == rollNo) {
        Student* toDelete = head;
        head = head->next;
        delete toDelete;
        cout <<"Student deleted"<<endl;
        return;
    }

    Student* prev = head;
    Student* curr = head->next;

    while (curr && curr->rollNo != rollNo) {
        prev = curr;
        curr = curr->next;
    }

    if (!curr) {
        cout << "Student not found"<<endl;
        return;
    }

    prev->next = curr->next;
    delete curr;
    cout << "Student deleted"<<endl;
}


    void updateStudent(int rollNo) {
        Student* temp = head;
        while (temp != nullptr && temp->rollNo != rollNo)
            temp = temp->next;

        if (temp == nullptr) {
            cout << "Student not found.\n";
            return;
        }
        cout << "Enter new name: ";
        cin.ignore();
        getline(cin, temp->name);
        cout << "Enter new marks: ";
        cin >> temp->marks;
        cout << "Student updated.\n";
    }

    void searchStudent(int rollNo) {
        Student* temp = head;
        while (temp != nullptr && temp->rollNo != rollNo)
            temp = temp->next;

        if (temp == nullptr) {
            cout << "Student not found.\n";
        } else {
            cout << "Roll No: " << temp->rollNo << ", Name: " << temp->name << ", Marks: " << temp->marks << "\n";
        }
    }

    void display() {
        if (head == nullptr) {
            cout << "No records found"<< endl;
            return;
        }
        cout << "RollNo\tName\tMarks\n";
        Student* temp = head;
        while (temp != nullptr) {
            cout << temp->rollNo << "\t" << temp->name << "\t" << temp->marks << "\n";
            temp = temp->next;
        }
    }


};

int main() {
    linkedlist srm;
    int choice;

    do {
        cout << "\n1. Add Student\n2. Delete Student\n3. Update Student\n4. Search Student\n5. Display Students\n6. Exit\n";
        cout << "Enter choice: ";
        cin >> choice;

        if (choice == 1) {
            int r, m;
            string n;
            cout << "Roll No: ";
            cin >> r;
            cout << "Name: ";
            cin.ignore();
            getline(cin, n);
            cout << "Marks: ";
            cin >> m;
            srm.addStudent(r, n, m);
        } 
        else if (choice == 2) {
            int r;
            cout << "Enter Roll No to delete: ";
            cin >> r;
            srm.deleteStudent(r);
        }
        else if (choice == 3) {
            int r;
            cout << "Enter Roll No to update: ";
            cin >> r;
            srm.updateStudent(r);
        }
        else if (choice == 4) {
            int r;
            cout << "Enter Roll No to search: ";
            cin >> r;
            srm.searchStudent(r);
        }
        else if (choice == 5) {
            srm.display();
        }
       
        else if (choice != 0) {
            cout << "Invalid choice.\n";
        }

    } while (choice != 0);

    cout << "Program exited.\n";
    return 0;
}
