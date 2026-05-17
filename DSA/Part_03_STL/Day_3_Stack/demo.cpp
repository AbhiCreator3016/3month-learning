#include <iostream>
#include <stack>

using namespace std;

int main() {

    // Create an empty stack of integers
    stack<int> st;

    // Push elements into the stack
    st.push(10);   // 10 added first
    st.push(20);   // 20 added on top of 10
    st.push(30);   // 30 added on top

    /*
        Current Stack:

        TOP
        30
        20
        10
    */

    // Access the top element
    cout << "Top Element: " << st.top() << endl;

    // Remove the top element (30)
    st.pop();

    /*
        Stack after pop():

        TOP
        20
        10
    */

    // Print new top element
    cout << "After Pop Top: " << st.top() << endl;

    // Print total number of elements
    cout << "Stack Size: " << st.size() << endl;

    // Check if stack is empty
    if(st.empty()) {
        cout << "Stack is Empty" << endl;
    }
    else {
        cout << "Stack is NOT Empty" << endl;
    }

    // Stack cannot be printed directly
    // So we create a copy
    stack<int> temp = st;

    cout << "Printing Stack: ";

    // Print elements until stack becomes empty
    while(!temp.empty()) {

        // Print top element
        cout << temp.top() << " ";

        // Remove printed element
        temp.pop();
    }

    return 0;
}