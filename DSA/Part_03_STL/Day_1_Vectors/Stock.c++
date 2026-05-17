#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

int maxProfit(vector<int> stock){
    if (stock.size()<2) return 0;
    int minPrice = stock[0];
    int maxPro = 0;
    for(int i=1;i<stock.size();i++){
        if (stock[i]<minPrice){
            minPrice = stock[i];
        }
        else{
            int curPro = stock[i] - minPrice;
            maxPro = max(curPro,maxPro);

        }
    }
    return maxPro;
}

int main(){
    vector<int> stock = {11, 5, 9, 3, 6, 8};
    int max_profit = maxProfit(stock);
    cout <<"Max Profit: "<< max_profit <<endl;
    return 0;
}