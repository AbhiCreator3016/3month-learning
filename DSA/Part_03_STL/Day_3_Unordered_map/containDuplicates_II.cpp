#include<iostream>
#include<unordered_map>
#include<vector>

using namespace std;
// template <typename J, typename K>

// void printMap(const unordered_map<J,K>& hashMap){           
//             for (const auto &pair: hashMap){
//                 cout<<"{"<<pair.first<<" : "<<pair.second<<"}\n";
//             }
//             cout<<endl;
// }

// unordered_map<int, int> vector_to_map(vector<int>& nums, unordered_map<int,int>& hashMap){      
//                 // int i=0;
//                 // while (i<nums.size()){
//                 //     if (hashMap.find(nums[i])==hashMap.end()){
//                 //         hashMap[nums[i]] = 1;
//                 //     }else{
//                 //         hashMap[nums[i]]++;
//                 //     }
//                 //     i++;
//                 // }
//                 for(int num:nums){
//                     hashMap[num]++;
//                 }
//                 printMap(hashMap);
//                 return hashMap;                
// }

bool containDuplicates(vector<int>& nums, int k){
    
    unordered_map<int,int> hashMap;
    for(int i=0;i<nums.size();i++){
        // if number already exist
        if (hashMap.find(nums[i])!=hashMap.end()){
            
            if(i - hashMap[nums[i]]<=k){
                return true;
            }
            
        }
            hashMap[nums[i]] = i;
        

    }
    return false;
}

int main(){
    vector<int> nums = {1,2,3,1,2,3};
    int k = 2;
    cout<<containDuplicates(nums, k);
    return 0;
}
