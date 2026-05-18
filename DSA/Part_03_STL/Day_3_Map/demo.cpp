#include<iostream>
#include<map>
#include<string>

using namespace std;
template <typename J, typename K>

void printMap(const map<J,K>& students){
    cout<<"---------  Map Data  ---------\n";
    cout<<"{\n";
    for(const auto& pair: students){
        cout<<pair.first<<" : "<<pair.second<<"\n";
    }
        cout<<"}\n";
        cout<<"---------  Map Data  ---------\n";

}

int main(){

        cout << "========= MAP IMPLEMENTATION =========\n\n";

    /*
        Example:
        Student Roll Number -> Student Name
    */

    map<int, string> students;
    cout<<"A map named student is created.\n";

    // ================= INSERTION =================
    cout << "\n========= 1. INSERTION =========\n";
    // method 1: using []
    cout<<"------> Insertion using direct ( .[key]=value )\n";
    students[101] = "Abhishek";
    cout<<"Added: 101-> Abhishek\n";
    students[102] = "Bhavya";
    cout<<"Added: 102-> Bhavya\n";

    // method 2. using insert
    cout<<"\n------> Insertion using insert({key,value})\n";
    students.insert({103,"Divyansh"});
    cout<<"Added: 103-> Divyansh\n";
    students.insert({104,"Elly"});
    cout<<"Added: 104-> Elly\n";
    // print map
    printMap(students);

    // ================= ACCESSING VALUES =================
    cout << "\n========= 2. ACCESSING VALUES =========\n";

    cout << "\nStudent with roll 102: ";
    cout<<students[102]<<"\n";
    cout << "\nStudent with roll 104: ";
    cout<<students[104]<<"\n";

    // ================= SIZE =================
    cout << "\n========= 3. SIZE =========\n";

    cout << "\n  Total students stored: ";
    cout<<students.size()<<"\n";


    // ================= FIND =================
    cout << "\n========= 4. FIND =========\n";
    cout << "\n------> Find student with roll no. 103\n";
    int roll = 103;

    auto it = students.find(roll);

    if(it!=students.end()){
        cout<<"\nStudent Found !!!\n";
        cout<<"Student with Roll No. "<<roll<<" is "<<it->second<<"\n";
        // cout<<it->first<<" : "<<it->second<<"\n";
    }


    // ================= COUNT =================
    cout << "\n========= 5. COUNT =========\n";

    /*
        count(key)
        -> returns 1 if key exists
        -> returns 0 if key does not exist
    */

    if(students.count(103)){
        cout<<"\nRoll number 103 is present in Students Map.\n";
    }else{
        cout<<"Roll number 103 doesnt exist.\n";
    }



    // ================= ERASE =================
    cout << "\n========= 6. ERASE =========\n";

    cout << "\n Removing roll number 102...\n";
    if(students.count(102)){
        students.erase(102);
        cout<<"\nStudent 102 erased.\n";
        printMap(students);
    }
    else{
        cout<<"\nStudent 102 doesn't exist.\n";
    }

        // ================= EMPTY =================
    cout << "\n========= 7. EMPTY =========\n";

    if(students.empty()){

        cout << "\n Map is empty.\n";
    }

    else{

        cout << "Map is NOT empty.\n";
    }


    // ================= IMPORTANT NOTES =================
    cout << "\n========= IMPORTANT NOTES =========\n";

    cout << "1. Keys are always unique.\n";

    cout << "2. Data is automatically sorted by key.\n";

    cout << "3. Map uses key-value pair structure.\n";

    cout << "4. Duplicate keys are NOT allowed.\n";

    cout << "5. Iterators ARE supported in map.\n";


    // ================= PRACTICE IDEAS =================
    cout << "\n========= PRACTICE IDEAS =========\n";

    cout << "1. Phonebook system.\n";

    cout << "2. Word frequency counter.\n";

    cout << "3. Student database.\n";

    cout << "4. Product inventory system.\n";




    return 0;
}