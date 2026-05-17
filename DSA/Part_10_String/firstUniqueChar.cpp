#include<iostream>
#include<string>
#include<unordered_map>

using namespace std;

int firstUnique(string s){
    if(s.length()<2) return 0;
    unordered_map<char, int> freq;
    
    for (char x : s){
        freq[x]++;
    }
    
    for (int i=0;i<s.length();i++){
        if (freq[s[i]]==1) return i;
    }
    return -1;
}

int main(){
    cout<<"LoveLeetcode"<<endl;
    string s = "LLeettd";
    cout<<"Unique char at index : "<<firstUnique(s);
    return 0;
}