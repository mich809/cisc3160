#include<iostream>
using namespace std;
int main ()
{
   int i, j,temp,pass=0;
   cout << "enter 10 numbers: " << endl;
   int numbers[10] ;

   for (int i = 0; i < 10; i++) {
    cin >> numbers[i];
    }
  

for(i = 0; i<10; i++) {
   for(j = i+1; j<10; j++)
   {
      if(numbers[j] < numbers[i]) {
         temp = numbers[i];
         numbers[i] = numbers[j];
         numbers[j] = temp;
      }
   }
pass++;
}

for(i = 0; i<10; i++) {
   cout <<numbers[i]<<"\t";
}

return 0;
}