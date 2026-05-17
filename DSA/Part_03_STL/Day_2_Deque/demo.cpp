#include <iostream>
#include <deque>

using namespace std;

int main() {

    deque<int> dq;

    dq.push_back(10);
    dq.push_back(20);

    dq.push_front(5);

    cout << "Deque: ";

    for(const auto& x : dq){
        cout << x << " ";
    }

    cout << "\nFront: " << dq.front();
    cout << "\nBack: " << dq.back();

    dq.pop_front();
    dq.pop_back();

    cout << "\nAfter popping: ";

    for(const auto& x : dq){
        cout << x << " ";
    }

    return 0;
}