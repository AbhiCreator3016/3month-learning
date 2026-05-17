#include<iostream>
#include<vector>
#include<unordered_map>


using namespace std;

vector<int> twoSum(vector<int>& arr, int target){
    unordered_map<int, int> hashmap; 

    for(int i=0;i<arr.size();i++){
        int complement = target - arr[i];

        if(hashmap.find(complement)!=hashmap.end()){
            return {hashmap[complement],i};
        }
        hashmap[arr[i]] = i;
    }
    return {};
}

int main(){
    vector<int> arr = {2, 7, 11, 15};
    int target = 18; 
    vector<int> result = twoSum(arr, target);
    
    // Printing result to verify
    // for(int x : result) cout << x << " ";
    cout<< result[0]<<" + "<<result[1];

    return 0;
}