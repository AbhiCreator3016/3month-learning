#include<iostream>

using namespace std;

void pattern_1(int size){
    for(int i=1;i<=size;i++){
        for (int j=1;j<=size;j++){
            cout<<"* ";
        }
        cout<<endl;
    }
}

void pattern_2(int size){
    for(int i=1;i<=size;i++){
        for(int j=1;j<=i;j++){
            cout<<"* ";
        }
        cout<<"\n";
    }
}

void pattern_3(int size){
    for (int i=1;i<=size;i++){
        for (int j = 1; j<=i; j++){
            cout<<j<<" ";
        }
        cout<<endl; 
    }
}

void pattern_4(int size){
    for (int i=1;i<=size;i++){
        for(int j=1;j<=i;j++){
            cout<<i<<" ";
        }
        cout<<endl;
    }
}

void pattern_5(int size){
    for(int i=0;i<size;i++){
        for(int j=size-i;j>=1;j--){
            cout<<"* ";
        }
        cout<<endl;
    }
}

void pattern_6(int size){
    for(int i=0;i<size;i++){
        for(int j=1;j<=size-i;j++){
            cout<<j<<" ";
        }
        cout<<endl;
    }
}

void pattern_7(int size){
    for(int i=1;i<=size;i++){
        for(int j=size-i;j>0;--j){
            cout<<"  ";    
        }
        int limit = (i*2)-1;
        for(int k=1;k<=limit;k++){
            cout<<"* ";
        }
        cout<<endl;
    }
}

void pattern_8(int size){
    int star = size*2 - 1;
    int space = 0;

    for (int i=1;i<=size;i++){
        for (int j=0;j<space;j++){
            cout<<"  ";
        }
        for (int k=1;k<=star;k++){
            cout<< "* ";
        }
        cout<<endl;
        ++space;
        star-=2;
    }
}

void pattern_9(int size){
    for( int i=1;i<=size;i++){
        for(int j=1;j<=size-i;j++){
            cout<<"  ";
        }
        for(int k=1;k<=(i*2)-1;k++){
            cout<<"* ";
        }
        cout<<endl;
    }

    int star = (size*2)-1;
    for(int i=1;i<=size;i++){
        for( int k=1;k<i;k++){
            cout<<"  ";
        }
        for( int j=1;j<=star;j++){
            cout<<"* ";
        }
        cout<<endl;
        star-=2;
    }
}

void pattern_10(int size){

    for(int j=1;j<=size;j++){
        for(int i=1;i<=j;i++){
            cout<<"* ";
        }
        cout<<endl;
    }
    for(int i=0;i<size-1;i++){
        for(int j=size-1-i;j>0;--j){
            cout<<"* ";
        }
        cout<<endl;
    }
}

void pattern_11(int size){
    for (int i=1;i<=size;i++){
        int num = (i%2==0)?0:1;
        for(int j=1;j<=i;j++){
            cout<<num<<" ";
            num = !num;
        }
        cout<<endl;
    }
}

void pattern_12(int size){
    size = 4;
    for(int i=1;i<=size;i++){
        int j;
        for(j=1;j<=i;j++){
            cout<<j<<" ";
        }
        for(int k=1;k<=(size-i)*2;k++){
            cout<<"  ";
        }
        for(j=j-1;j>=1;j--){
            cout<<j<<" ";
        }
            
        cout<<endl;
    }
}

void pattern_13(int size){
    int count = 1;
    for (int i=1;i<=size;i++){
        for(int j=1;j<=i;j++){
            cout<<count<<" ";
            count++;
        }
        cout<<endl;
    }
}

int main(){
    cout<<"You are exploring patterns:\n";
    int size;
    cin>>size;
    cout<<"-------Pattern_1-------------"<<endl;
    pattern_1(size);
    cout<<"-------Pattern_2-------------"<<endl;
    pattern_2(size);
    cout<<"-------Pattern_3-------------"<<endl;
    pattern_3(size);
    cout<<"-------Pattern_4-------------"<<endl;
    pattern_4(size);
    cout<<"-------Pattern_5-------------"<<endl;
    pattern_5(size);
    cout<<"-------Pattern_6-------------"<<endl;
    pattern_6(size);
    cout<<"-------Pattern_7-------------"<<endl;
    pattern_7(size);
    cout<<"-------Pattern_8-------------"<<endl;
    pattern_8(size);
    cout<<"-------Pattern_9-------------"<<endl;
    pattern_9(size);
    cout<<"-------Pattern_10-------------"<<endl;
    pattern_10(size);
    cout<<"-------Pattern_11-------------"<<endl;
    pattern_11(size);
    cout<<"-------Pattern_12-------------"<<endl;
    pattern_12(size);
    cout<<"-------Pattern_13-------------"<<endl;
    pattern_13(size);
    return 0;
}