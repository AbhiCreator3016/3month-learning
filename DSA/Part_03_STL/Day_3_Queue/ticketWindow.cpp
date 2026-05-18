#include<iostream>
#include<queue>

using namespace std;
template <typename T>
void printQueue(queue<T> q){
    if(q.empty()){
        cout<<"\nQueue is empty!!!\n";
    }
    cout<<"Front ->";
    while (!q.empty())
    {
        cout<<"["<<q.front()<<"]";
        q.pop();
    }

    cout<<"<- Rare\n";
    cout<<"------------------------------\n";
}

int main(){
        /*
    QUEUE IN C++
    -------------------------
    -> Queue follows FIFO principle
       (First In First Out)

    -> Insertion happens from REAR.
    -> Deletion happens from FRONT.

    -> Random access is NOT possible.
       No iterators are supported.

    Time Complexities:
    -------------------------
    push()  -> O(1)
    pop()   -> O(1)
    front() -> O(1)
    back()  -> O(1)
    empty() -> O(1)
    size()  -> O(1)

    Real World Uses:
    -------------------------
    1. Movie Ticket Line
    2. Printer Queue
    3. CPU Scheduling
    4. Call Center Systems
    5. BFS Traversal
*/


// Generic function to print queue
// Passed by value intentionally
// so original queue remains unchanged


    cout << "========= QUEUE IMPLEMENTATION =========\n\n";

    // creating a queue
    queue<string> movieLine;
    cout << "A queue named 'movieLine' is created.\n";


    // ================= PUSH =================
    cout << "\n========= 1. PUSH OPERATION =========\n";

    cout << "Customers joining movie ticket line:\n\n";
    movieLine.push("Abhishek");
    cout<<"Abhishek Joined the Queue.\n";
    movieLine.push("Rahul");
    cout<<"Rahul Joined the Queue.\n";
    movieLine.push("Devesh");
    cout<<"Devesh Joined the Queue.\n";
    movieLine.push("Kaviraj");
    cout<<"Kaviraj Joined the Queue.\n";

    // print the queue
    printQueue(movieLine);



    // ================= FRONT =================
    cout << "\n========= 2. FRONT OPERATION =========\n";
    // front() returns first element
    // but does NOT remove it
    cout<<"Customer at the front: ";
    cout<<movieLine.front()<<endl;

    // ================= BACK =================
    cout << "\n========= 3. BACK OPERATION =========\n";
    // back return the last element
    cout<<"Customer at the rare: ";
    cout<<movieLine.back()<<endl;

    // ================= SIZE =================
    cout << "\n========= 4. SIZE OPERATION =========\n";

    cout << "Total customers in queue: ";
    cout << movieLine.size() << endl;


    // ================= POP =================
    cout << "\n========= 5. POP OPERATION =========\n";

    // Check before popping
    if (!movieLine.empty()){
        cout<<movieLine.front();
        cout<<" got the movie ticket and Left the queue.\n";
        movieLine.pop();
    }

    cout<<"Queue after pop():\n";
    printQueue(movieLine);



    // ================= CLEAR QUEUE =================
    cout << "\n========= 6. CLEARING QUEUE =========\n";

    while (!movieLine.empty()){
        cout<<movieLine.front();
        cout<<" received the ticket and exited\n";
        movieLine.pop();
    }
        cout<<"\nAll Customers processed.\n";

    
     // ================= EMPTY =================
    cout << "\n========= 7. EMPTY OPERATION =========\n";

    if(movieLine.empty()){
        cout<<"\nAll transections processed:";
        cout << "Queue is empty.\n";
    }

    else{

        cout << "\nQueue is NOT empty.\n";
    }


    // ================= IMPORTANT NOTES =================
    cout << "\n========= IMPORTANT NOTES =========\n";

    cout << "1. Queue follows FIFO.\n";
    cout << "2. First inserted element leaves first.\n";
    cout << "3. Random access is NOT possible.\n";
    cout << "4. Iterators are NOT supported.\n";


    // ================= PRACTICE IDEAS =================
    cout << "\n========= PRACTICE IDEAS =========\n";

    cout << "1. Printer queue simulation.\n";
    cout << "2. Call center waiting system.\n";
    cout << "3. Implement BFS traversal.\n";
    cout << "4. CPU task scheduling simulation.\n";

    

    return 0;
}