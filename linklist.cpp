#include <bits/stdc++.h>
using namespace std;

struct Node {
    int rollNo;
    string name;
    float marks;
    Node* next;
};

int main() {
    Node* head = nullptr;
    Node* temp = nullptr;
    Node* tail = nullptr;

    int m;
    cout << "Enter the number of students: ";
    cin >> m;

    for (int i = 0; i < m; i++) {
        temp = new Node;
        cout << "\nEnter details for student " << (i + 1) << ":\n";

        cout << "Roll No: ";
        cin >> temp->rollNo;

        cin.ignore();

        cout << "Name: ";
        getline(cin, temp->name);

        cout << "Marks: ";
        cin >> temp->marks;

        temp->next = nullptr;

        if (head == nullptr) {
            head = temp;
            tail = temp;
        } else {
            tail->next = temp;
            tail = temp;
        }
    }

    cout << "\nStudent List:\n";
    Node* curr = head;
    while (curr != nullptr) {
        cout << "Roll No: " << curr->rollNo 
             << ", Name: " << curr->name 
             << ", Marks: " << curr->marks << endl;
        curr = curr->next;
    }

    return 0;
}
