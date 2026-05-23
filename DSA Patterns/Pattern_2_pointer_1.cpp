#include<iostream>
#include<unordered_map>
#include<vector>
#include<algorithm>

using namespace std;

vector <int> twoSum(vector<int>& num, int target){
    sort(num.begin(),num.end());
    int i =0;
    int j =num.size()-1;

    while(i<j){
        if(num.at(i)+num.at(j)==target){
                return {i,j};
        }else if(num.at(i)+num.at(j)>target){
                    --j;
        }else if(num.at(i)+num.at(j)<target){
                    ++i;
        }
    }
    return {-1,-1};

}

int main(){

    vector <int> arr = {2,1,7,6,8};
    int target = 8;
    vector <int> ans = twoSum(arr, target);
    cout << "pair: " << ans.front() << " " << ans.back();

    return 0;
}