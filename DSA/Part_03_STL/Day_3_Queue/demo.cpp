#include <iostream>
#include <queue>

using namespace std;

int main() {

    // Create an empty queue of integers
    queue<int> q;

    // Push elements into the queue
    q.push(10);   // inserted first
    q.push(20);   // inserted second
    q.push(30);   // inserted third

    /*
        Current Queue:

        FRONT -> 10 20 30 <- REAR
    */

    // Access the front element
    cout << "Front Element: " << q.front() << endl;

    // Access the rear element
    cout << "Rear Element: " << q.back() << endl;

    // Remove the front element (10)
    q.pop();

    /*
        Queue after pop():

        FRONT -> 20 30 <- REAR
    */

    // Print new front element
    cout << "After Pop Front: " << q.front() << endl;

    // Print total number of elements
    cout << "Queue Size: " << q.size() << endl;

    // Check if queue is empty
    if(q.empty()) {
        cout << "Queue is Empty" << endl;
    }
    else {
        cout << "Queue is NOT Empty" << endl;
    }

    // Queue cannot be printed directly
    // So we create a copy
    queue<int> temp = q;

    cout << "Printing Queue: ";

    // Print elements until queue becomes empty
    while(!temp.empty()) {

        // Print front element
        cout << temp.front() << " ";

        // Remove printed element
        temp.pop();
    }

    /*
        Output:
        20 30
    */

    return 0;
}