#include<bits/stdc++.h>
using namespace std;
struct Node
{
    int rollNo;
    string name;
    float marks;
    Node*next;
};
int main(){
    Node*head = nullptr;
    Node*temp = nullptr;
    Node*tail = nullptr;

    int m;
    cout<<"Enter the num of students ";
    cin>>m;

    for (int i = 0; i < m; i++)
    {
        temp = new Node;
        cout<<"\nEnter detail of the students"<<(i+1)<<":\n";
        
        cout<<"Roll No.";
        cin>>temp->rollNo;
           
        cin.ignore();

        cout<<"Name ";
        getline(cin,temp->name);
        
        cout<<"Marks " ;
        cin>>temp->marks;

        temp->next = nullptr;
        if (head == nullptr)
        {
            head = temp;
            tail = temp;

        }
        else{
            tail->next = temp;
            tail = temp;
        
    }
    

}
return 0;
}
