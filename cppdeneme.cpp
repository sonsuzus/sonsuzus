#include <iostream>
using namespace std;
int main()
{
    int sayi;
    cout << "Bir sayi giriniz: ";
    cin >> sayi;
 
    for (int sayac=1; sayac<sayi; sayac++)
    {
        int asal, test;
        test = sayac;
        asal = 1;
        while (test--> 2)
            if ((sayac % test) == 0)
                asal = 0;
        if (asal == 1)
            cout<< sayac << " bir asal sayidir!\n";
    }
    return 0;
}
 