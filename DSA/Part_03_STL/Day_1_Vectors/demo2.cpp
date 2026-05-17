#include<iostream>
#include<vector>

using namespace std;

void printVector(const vector<int>& vec){
    // "const" restrict any change in vector data, only allow read-only 
    // "&"  pass referecne of the vector, no new copy of the vetor formed

    if(vec.empty()){
        cout<< "Vector is empty!!"<<endl;
        return ;
    }
    for (auto &itr: vec){
        cout<<itr<<" ";
    }
    cout<<endl;
}

int main(){
    //=================================================
    //1. Initilization of the vector
    //=================================================

    cout<<"==========Vator Initilization==============="<<endl;

    vector<int> num1; // empty vector (size = 0)
    vector<int> num2 = {1,2,3,4,5}; // with initial values
    vector<int> num3(10,-1); // create 10 element with -1

    cout <<"Numbers vector 2 \n";
    printVector(num2);

    cout <<"Number vector 3 \n";
    printVector(num3);



    // =====================================================
    // 2. Insertion in vector
    // =====================================================
    cout <<"\n=========== 2. Insertion in vector===========\n";
    // push_back(): add element at the end of the vector
    num1.push_back(10);
    num1.push_back(20);
    num1.push_back(30);
    num1.push_back(40);
    // num1.push_back(50);
    cout<<"Numbers 1 vector after push_back \n";
    printVector(num1);

    // --------------embrace_back()------------------//   
    num1.emplace_back(50);
    cout<<"Number 1 vector with 'embrace_back':\n";
    printVector(num1);

    // *.begin() this points/brings the first element of vector//
    // -------------insert(positionm, value)-------------------------//
    num2.insert(num2.begin()+1,100);
    cout<<"Inserted 100 at 1 index using .insert(pos,value) in Numbers2: \n";
    printVector(num2);


    //===============================================================//
    // 3. Accessing elements 
    //==============================================================//

    cout<<"\n=============== 3. Accessing Elements ================\n";
    cout<<"\nElement at index 2 of Num 1: (using[] ):\n"<< num1[2]<<endl;
    cout<<"Element at index 3 of Num 2: (using at())\n:"<< num2.at(2)<<endl;
    cout<<"Accessing first element of Num 3 using .front():\n"<<num3.front()<<endl;
    cout<<"Accessing last element of Num 3 usign .back():\n"<< num3.back()<<endl;

    // =============================================================//
    // 4. Deletion 
    // =============================================================//
    cout<<"\n=======================Deletion=========================\n";

    // .pop+back(): remove the last element 
    cout << "\nRemoved the last element from Nums 1 using .pop_back():\n";
    num1.pop_back();
    printVector(num1);

    // erase(): remove element from any specific index, 
    // it expect an iterator not just index value
    cout<<"Removing 100 from Num 2 using .erase(*.begin()+index):\n";
    num2.erase(num2.begin()+1);
    printVector(num2);

    // erase(): can remove with range too
    // .erase(start_iterator, end_iterator) 
    // -> end_iterator is not include
    cout<<"Erase element from range 1 to 3 Num 2\n";
    num2.erase(num2.begin()+1,num2.begin()+4);
    printVector(num2);


    // ========================================================//
    // 5. Size and Capacity (Memory Management)
    // ========================================================//

    cout<<"\n============Size and Capacity====================\n";
    cout<<"\nCreated and new empty vector\n";
    vector<int> demo;
    cout << "Initial - Size: " << demo.size() << "\nCapacity: " << demo.capacity() << endl;


    // ----------How capacity change while adding element--------//
    cout<<"------How capacity change while adding element--------\n";
    for(int i = 1; i <= 5; i++) {
        demo.push_back(i);
        cout << "Added " << i << " \nSize: " << demo.size() << ", Capacity: " << demo.capacity() << endl;
    }

    // .reserve(): reserve fixed memory in advance to avoid resize
    cout<<"We can use .reserve(size) to reserver size in Adv.\n";
    demo.reserve(20);
    cout << "using .reserve(20) in demo vector\nSize: " << demo.size() << "\nCapacity: " << demo.capacity() << endl;

    // shrink_to_fit(): Faltu ki capacity ko release karke size ke barabar karne ke liye
    cout << "After using .shrink_to_fit()\nSize: " << demo.size() << "\nCapacity: " << demo.capacity() << endl;
    demo.shrink_to_fit();

    // ==============================================================//
    // 6. Iterators 
    // ==============================================================//

    cout<<"\n===================6. Iterator============================\n";
    cout<<"\nForward iteratior: \n";
    for(auto it = num1.begin(); it!=num1.end();++it){
        cout<<*it<<" ";// dereferencing (pull out the value from index)
    }
    cout<<endl;
    cout<<"\nBack-ward iteratior: \n";
    for(auto it = num1.rbegin();it!=num1.rend();++it){
        cout<<*it<<" ";
    }
    cout<< endl;

    // ==================================================================
    // 7. CLEAR & EMPTY 
    // ==================================================================
    cout<<"\n================ 7. Clear & Empty ===============" << endl;

    cout<<"Nums is empty?: " << (num1.empty() ? "Yes" : "No") << endl;

    // clear(): remove all the element 
    num1.clear();
    cout << "Using clear() with Num 1:\n" <<"Size: "<< num1.size() << endl;
    cout<<"Nums is empty?: " << (num1.empty() ? "Yes" : "No") << endl;
    return 0;
}