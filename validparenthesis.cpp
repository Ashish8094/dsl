#include<bits/stdc++.h>
using namespace std;

bool g(string s,int n){
    stack<char>st;
    for(int i=0;i<n;i++){
        if(s[i]=='(' || s[i]=='[' || s[i]=='{') st.push(s[i]);
        else if(s[i]==')' || s[i]=='}' || s[i]==']'){
            if(st.empty()) return false;
          
         char x=st.top();
         if ((x == '(' && s[i] == ')') ||
                (x == '[' && s[i] == ']') ||
                (x == '{' && s[i] == '}')) {
                st.pop();
            }

            else return false;
        }
    }
    return st.empty();
    }
  

int main(){
    string s;   cin>>s;
    int n=s.length();
    if(g(s,n)){
        cout<<"CORRECT";
    }my name 
    else cout<<"NOT CORRECT";

}