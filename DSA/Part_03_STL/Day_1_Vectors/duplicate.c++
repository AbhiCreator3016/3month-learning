#include<iostream>
#include<unordered_map>
#include<vector>

using namespace std;

string duplicate(vector<int>& arr){
    unordered_map<int,int> hashMap;

    for(int i=0;i<arr.size();i++){
        if(hashMap.find(arr[i])!=hashMap.end()){
            return "True";
        }else{
            hashMap.insert({arr[i],i});
        }
    }
    return "False";
}

int main(){
    // unordered_map<int
    vector<int> arr1 = {1,2,5,6,7,9,1};
    vector<int> arr2 = {1,2,3,4,5,6};
    cout<<duplicate(arr1)<<endl;
    cout<<duplicate(arr2)<<endl;

    return 0;
}