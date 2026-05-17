#include <iostream>
#include<list>
#include<string>

using namespace std;

void getNames(list<string>& names, int num){
    string name;
    for(int i=1;i<=num;i++){
        names.push_back((cin>>name, name));
    }
    return;
}
void printList(list<string>& Names){
    for(string name:Names){
        cout<<name<<endl;
    }
    return;
}


int main(){

    list<int> Nums = {10, 20, 30, 40, 50};
    list<string> Names;
    int num;
    cout<<"Enter the number of Names you want to add:\n";
    cin>>num;
    getNames(Names,num);
    printList(Names);

    return 0;
}