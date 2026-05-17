#include<iostream>
#include<deque>


using namespace std;
template <typename T>
void ShowTabs(const deque<T>& tabs){
    if(tabs.empty()){
        cout<<"No tabs open!"<<endl;
        return;
    }
    cout<<"Current Tabs (Oldest to newest): \n";
    for (const auto& tab:tabs){
        cout<<"["<<tab<<"]";
    }
    cout<< "\n Total Tabs Open: "<< tabs.size()<<endl;
    cout<<"---------------------------------------"<<endl;
}

int main(){
    cout<<"1.Deque is a double-ended queue. Pronounce as 'deck'\n";
    cout<<"2.It contain the qualities of Vector and List\n";
    cout<<"3.We can access the elements by index\n";

    deque<int> temp = {10,20,30};
    deque<string> browserHistory;

    cout<<"\n===============  1.Insertion of data  =====================\n";
    cout << "\n------> Opening New Tabs (.push_back(x)) ---" << endl;
    browserHistory.push_back("google.com"); // (O(1)time)
    browserHistory.push_back("github.com");
    browserHistory.push_back("youtube.com");
    ShowTabs(browserHistory);

    cout << "\n------> Opening New Tabs (.push_front(x)) ---\n";
    browserHistory.push_front("chatGPT.com");
    ShowTabs(browserHistory);

    cout << "\n------> Opening New Tabs (.insert(iterator,x))  ---\n";
    browserHistory.insert(browserHistory.begin()+2,"gemini.com");
    ShowTabs(browserHistory);

    cout<<"\n\n===============  2.Access of data  =====================\n";
    cout<<"\n------> First opened tab (.front())  -------\n";
    cout<<browserHistory.front()<<endl;
    cout<<"\n------> Recent opened tab (.back())  -------\n";
    cout<<browserHistory.back()<<endl;
    cout<<"\n------> Tab at index 2 (.at())  -------\n";
    cout<<browserHistory.at(2)<<endl;

    cout << "\n\n=============  3.Max Limit Reached! Handling New Tab..." << endl;
    if (browserHistory.size()>=5){
        cout<<"\n[System Notification] Limit Full! Removing the oldest tab:\n";
        browserHistory.pop_front();
    }
    browserHistory.push_back("claudeCode.com");
    ShowTabs(browserHistory);

    cout<<"\n\n===============  4. Delete specific ======================\n";
    cout<<"\n------> Delete tab at index 2 using (.erase)\n";
    browserHistory.erase(browserHistory.begin()+2);
    ShowTabs(browserHistory);

    cout<<"\n\n===============  5.Deletion of data  =====================\n";
    cout<<"\n------> Closing all tab using (.clear & .empty) ------\n";
    browserHistory.clear();
    ShowTabs(browserHistory);
    if(browserHistory.empty()){
        cout<<"\nAll the tabs are closed successfully!\n";
    }
    return 0;
}