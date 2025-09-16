#include<bits/stdc++.h>
using namespace std;

struct Node{
    int data;
    Node * next;


};
int main(){
    Node*head = nullptr;
    Node*temp = nullptr;
    Node*tail = nullptr;

    int m;
    cout<<"Enter the nodes "<<endl;

    cin>>m;

    cout<<"Enter the num ";
    for (int i = 1; i < m; i++)
    {
        temp = new Node;
        int x;
        cin>>x;
        temp ->data = x;
        temp ->next = nullptr;


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
    Node*curr = head;
    while (curr!=nullptr)
    {
       cout<< curr->data<<" "; 
       curr = curr->next;
    }
    cout<<endl;

    return 0;
}