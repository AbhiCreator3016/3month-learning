#include<iostream>
#include<string>

using namespace std;

string welcome(string name){
    return "Hello, "+name+"\n";
}

int main(){
    string name;
    cout<<"Enter your name: ";
    cin>> name;
    cout << welcome(name);
    cout << "Welcome to the course.";
    return 0;
}