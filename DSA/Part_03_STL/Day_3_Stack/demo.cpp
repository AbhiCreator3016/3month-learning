#include <iostream>
#include <stack>

using namespace std;

/*
    STACK IN C++
    -------------------------
    -> Stack follows LIFO principle
       (Last In First Out)

    -> Insertion and deletion happen only from TOP.

    -> Random access is NOT possible.
       No iterators are supported.

    Time Complexities:
    -------------------------
    push()  -> O(1)
    pop()   -> O(1)
    top()   -> O(1)
    empty() -> O(1)
    size()  -> O(1)

    Real World Uses:
    -------------------------
    1. Undo / Redo
    2. Browser History
    3. Function Call Stack
    4. Expression Evaluation
    5. DFS Traversal
*/


// Generic function to print stack
// Passed by value intentionally
// so original stack remains unchanged
template <typename T>
void printStack(stack<T> s){

    cout << "\nTop\n";

    while(!s.empty()){

        cout << "| " << s.top() << " |\n";

        s.pop();
    }

    cout << "Bottom\n";
    cout << "-----------------------------\n";
}


int main(){

    cout << "========= STACK IMPLEMENTATION =========\n\n";

    // Creating stack
    stack<string> books;

    cout << "A stack named 'books' is created.\n";


    // ================= PUSH =================
    cout << "\n========= 1. PUSH OPERATION =========\n";

    cout << "Adding books using push()\n\n";

    books.push("The Secret");
    cout << "\"The Secret\" pushed into stack.\n";

    books.push("How to Win Friends");
    cout << "\"How to Win Friends\" pushed into stack.\n";

    books.push("Corporate Chanakya");
    cout << "\"Corporate Chanakya\" pushed into stack.\n";


    // Print stack
    printStack(books);


    // ================= TOP =================
    cout << "\n========= 2. TOP OPERATION =========\n";

    // top() returns top element
    // but does NOT remove it
    cout << "Current top book: ";
    cout << books.top() << endl;


    // ================= SIZE =================
    cout << "\n========= 3. SIZE OPERATION =========\n";

    cout << "Total books in stack: ";
    cout << books.size() << endl;


    // ================= POP =================
    cout << "\n========= 4. POP OPERATION =========\n";

    // Check stack before popping
    if(!books.empty()){

        cout << "Removing top book...\n";

        books.pop();
    }

    cout << "Stack after pop():\n";

    printStack(books);


    // ================= EMPTY =================
    cout << "\n========= 5. EMPTY OPERATION =========\n";

    if(books.empty()){

        cout << "Stack is empty.\n";
    }

    else{

        cout << "Stack is NOT empty.\n";
    }


    // ================= CLEAR STACK =================
    cout << "\n========= 6. CLEARING STACK =========\n";

    // Removing all elements
    while(!books.empty()){

        cout << "Removing: " << books.top() << endl;

        books.pop();
    }

    cout << "\nAll books removed.\n";


    // Check again
    if(books.empty()){

        cout << "Now stack is empty.\n";
    }


    // ================= IMPORTANT NOTES =================
    cout << "\n========= IMPORTANT NOTES =========\n";

    cout << "1. Stack follows LIFO.\n";
    cout << "2. Only top element is accessible.\n";
    cout << "3. Iterators are NOT supported.\n";
    cout << "4. Random access is NOT possible.\n";


    // ================= PRACTICE QUESTIONS =================
    cout << "\n========= PRACTICE IDEAS =========\n";

    cout << "1. Reverse a string using stack.\n";
    cout << "2. Check balanced parentheses.\n";
    cout << "3. Implement browser history.\n";
    cout << "4. Solve Next Greater Element problem.\n";


    return 0;
}