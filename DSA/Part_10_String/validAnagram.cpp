#include<iostream>
#include<string>
#include<unordered_map>

using namespace std;

string validAnagram(string str1, string str2){
    if (str1.length() != str2.length()) return "false";

    unordered_map<char, int> hashMap;

    // for(int i=0;i<str1.length();i++){
    //     if(hashMap.find(str1[i])!=hashMap.end()){
    //         hashMap.insert({str1[i],++i});
    //     }
    //     else{
    //         hashMap.insert({str1[i],i});
    //     }
    // }
    // for(int j=str2.length()-1;j>=0;--j){
    //     if(hashMap.find(str2[j])!=hashMap.end()){
    //         hashMap.insert({str2[j],--j});
    //     }
    // }

    for (char x: str1){
        hashMap[x]++;
    }
    for(char x: str2){
        hashMap[x]--;
        if (hashMap[x]<0) return "false";
    }

    for(const auto&[ch,fq]: hashMap){
        cout<<ch<<" : "<<fq<<endl;
    }

    return "true";
}

int main(){
    cout<<"Valind Anagrm Programm."<<endl;
    cout << "Test 1 (anagram): " << validAnagram("anagram", "nagaram") << endl;
    cout << "Test 2 (length): " << validAnagram("abc", "ab") << endl;
    cout << "Test 3 (frequency): " << validAnagram("aabb", "abab") << endl;
    cout << "Test 4 (different chars): " << validAnagram("rat", "car") << endl;
    return 0;
}