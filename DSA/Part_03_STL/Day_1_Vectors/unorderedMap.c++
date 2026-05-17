#include<iostream>
#include<unordered_map>
#include<string>

using namespace std;

int main(){
    // Declare the map 
    unordered_map<string,int> marksMap;

    // Insert the data
    marksMap.insert({"Abhishek",91});
    marksMap.insert({"Babita",89});
    marksMap.insert({"Chirkut",90});
    marksMap.insert({"Dinesh",78});
    marksMap.insert({"Emily",88});
    marksMap.insert({"Fiona",85});

    // Accessing the element
    // cout<<"Dinesh : "<<marksMap["Dinesh"]<<endl;

    // searching the element
    // string key;
    // cout<<"Enter the student name:\n";
    // cin>> key;
    // if(marksMap.find(key)!=marksMap.end()){
    //     cout<<key<<" : "<<marksMap[key]<<endl;
    // }else{
    //     cout<<key<<" : "<<"NOt found"<<endl;
    // }

    // delete any element
    // marksMap.erase("Fiona");

    // Iterate all over the map 
    cout<<"\nComplete data:\n"<<endl;
    for(const auto& [name,marks]: marksMap){
        cout<< name <<" : "<< marks <<endl;
    }
    return 0;
}