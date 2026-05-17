#include <iostream>
#include <vector>
#include <algorithm> // Algorithms ke liye

using namespace std;

int main() {
    // 1. Container: Vector
    vector<int> numbers = {40, 10, 30, 20, 50};

    // 2. Algorithm: Sort
    sort(numbers.begin(), numbers.end());

    // 3. Iterator style loop (Modern C++)
    for(int x : numbers) {
        cout << x << " "; // Output: 10 20 30 40 50
    }

    // 4. Searching
    if(binary_search(numbers.begin(), numbers.end(), 30)) {
        cout << "\nFound 30!";
    }

    return 0;
}