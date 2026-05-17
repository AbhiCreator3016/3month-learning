#include <iostream>
#include <list>

using namespace std;
template <typename T> // It allows one function/class to work with multiple data types.
void printList(const list<T>& list){
    for (auto value: list){
        cout << value << " -> ";
    }
    cout << "NULL" << endl;
}

int main() {
    list<int> my_list;

    // 1. Elements add karna
    cout<<"================= 1.Adding element in List ==================\n";
    cout<<"\nCreated my_list\n";
    my_list.push_back(20);  // List ke peeche daalo -> [20]
    my_list.push_back(30);  // List ke peeche daalo -> [20, 30]
    my_list.push_front(10); // List ke aage daalo  -> [10, 20, 30]

    cout << "\n=============== 2.Access List elements: =================\n";
    /* List mein index ([]) nahi chalta, 
     isliye range-based loop ya iterator chahiye */
    cout<<endl;
    for (int x : my_list) {
        cout << x << " -> ";
    }
    cout << "NULL" << endl; // Output: 10 -> 20 -> 30 -> NULL

    // 2. Elements remove karna
    cout << "\n=============== 2.Deleting elements: =================\n";
    cout<<"\nDeleted the front element: \n"<<endl;
    my_list.pop_front(); // Sabse pehla element (10) hat jayega -> [20, 30]
    printList(my_list);
    cout<<"\nDeleted the last element: \n"<<endl;
    my_list.pop_back();  // Sabse aakhri element (30) hat jayega -> [20]
    printList(my_list);


    return 0;
}