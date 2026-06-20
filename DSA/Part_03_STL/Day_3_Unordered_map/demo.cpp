#include<iostream>
#include<unordered_map>

using namespace std;
template <typename J, typename K>

void printMap(const unordered_map<J,K>& hash){
    cout<<"\n------  Unordered Map Data  ------\n";
    cout<<"{\n";
    for(const auto &pair : hash){
        cout<<pair.first<<" : "<<pair.second<<"\n";
    }
    cout<<"{\n";
    cout<<"------  Unordered Map ------\n";
}

int main(){
    cout << "========= UNORDERED MAP IMPLEMENTATION =========\n\n";

    /*
        Example:
        Username -> Password
    */
   unordered_map<string, string> users;
   cout<<"An Unordered Map named 'users' is created.\n";

   // ================= INSERTION =================
    cout << "\n========= 1. INSERTION =========\n";
    cout<<"\n------> Inserting users with ([key] = value)\n";
    users["User_1"] = "Abhi22385";
    cout<<"\nUser_1 added to the users DB.\n";
    users["User_2"] = "Bhav22390";
    cout<<"\nUser_2 added to the users DB.\n";

    cout<<"\n------> Inserting using insert({})\n";
    users.insert({"User_3","Chavi22468"});
    cout<<"\nUser_3 added to the users DB.\n";
    users.insert({"User_4","Chavi23368"});
    cout<<"\nUser_4 added to the users DB.\n";

    // print map
    printMap(users);


     // ================= ACCESSING VALUES =================
    cout << "\n========= 2. ACCESSING VALUES =========\n";

    cout << "\nPassword of user_3: ";
    cout << users["User_3"] << endl;

    cout << "\nPassword of user_1: ";
    cout << users["User_1"]<<"\n";

    // ================= SIZE =================
    cout << "\n========= 3. SIZE =========\n";

    cout << "\nTotal users stored: \n";
    cout << users.size() << endl;

    // ================= FIND =================
    cout << "\n========= 4. FIND =========\n";
    cout<<"\n------> Searching user_4 in the map\n";
    auto it = users.find("User_4");
        if (it!=users.end())
        {
            cout<<"Found User_4\n";
            cout<<"Username : "<<it->first<<endl;
            cout<<"Password : "<<it->second;
        }
        else{
            cout<<"User_4 not found.\n";
        }
    
        // ================= COUNT =================
    cout << "\n========= 5. COUNT =========\n";

    /*
        count(key)
        -> returns 1 if key exists
        -> returns 0 if key does not exist
    */
   cout<<"\nSearching for user 'Abhishek' in map: \n";
   if(users.count("Abhishek")){
        cout<<"User is present in the Map!\n";
   }else{
        cout<<"User in not present in the Map.\n";
   }

   // ================= ERASE =================
    cout << "\n\n========= 6. ERASE =========\n";

    cout << "\n-> Removing user user_4...\n";
    users.erase("User_4");
    cout<<" Unordered Map after removing User_4:\n";
    printMap(users);


    // ================= EMPTY =================
    cout << "\n========= 7. EMPTY =========\n";

    if(users.empty()){

        cout << "unordered_map is empty.\n";
    }

    else{

        cout << "unordered_map is NOT empty.\n";
    }


    // ================= MAP vs UNORDERED_MAP =================
    cout << "\n========= MAP vs UNORDERED_MAP =========\n";

    cout << "map:\n";
    cout << "-> Sorted order\n";
    cout << "-> Uses Red-Black Tree\n";
    cout << "-> O(log n)\n\n";

    cout << "unordered_map:\n";
    cout << "-> Unsorted order\n";
    cout << "-> Uses Hash Table\n";
    cout << "-> O(1) average\n";


    // ================= IMPORTANT NOTES =================
    cout << "\n========= IMPORTANT NOTES =========\n";

    cout << "1. Keys are always unique.\n";

    cout << "2. Data is NOT sorted.\n";

    cout << "3. Faster lookup than map in most cases.\n";

    cout << "4. Uses hashing internally.\n";

    cout << "5. Iterators ARE supported.\n";


    // ================= PRACTICE IDEAS =================
    cout << "\n========= PRACTICE IDEAS =========\n";

    cout << "1. Word frequency counter.\n";

    cout << "2. Login authentication system.\n";

    cout << "3. Two Sum problem.\n";

    return 0;
}