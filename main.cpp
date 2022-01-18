#include <iostream>

using namespace std;

template <typename T>

T* concat(T a[], int sizea, T b[], int sizeb) {
    int size = sizea+sizeb;
    T* c = new T[size];
    for (int i = 0; i < sizea; i++) {
        c[i] = a[i];
    }
    for (int j = sizea; j < size; j++) {
        c[j] = b[j-sizea];
    }
    return c;
}

int main() {
    cout << "두 개의 정수 배열을 합칩니다." << endl;
    
    int x[] = {1, 2, 3};
    int y[] = {6,7,8,9};
    int* p = concat(x, 3, y, 4);
    for (int i = 0; i < 7; i++) {
        cout << p[i] << ' ';
    }
    cout << endl;
    delete[] p;
    
    cout << "두 개의 문자 배열을 합칩니다. " << endl;
    char m[] = "LOVE";
    char n[] = "C**";
    char* q = concat(m, 4, n, 3);
    for (int j = 0; j < 7; j++) {
        cout << q[j] << ' ';
    }
    cout << endl;
    delete[] q;
}

