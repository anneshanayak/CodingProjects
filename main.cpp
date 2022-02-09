#include <iostream>
#include <stdlib.h>

using namespace std;

int V[10], m=10, r=-1, f=-1;

void enqueue(int x) {
   if (r==m-1){
    cout << "OVERFLOW" << endl;
    exit(EXIT_SUCCESS);
   }
    else {
      if (f==-1)
      f=0;
      r=r+1;
      V[r] = x;
    }
}

void dequeue(int y) {
   if (f==-1) {
     cout << "QUEUE UNDERFLOW" << endl;
     exit(EXIT_SUCCESS);
   }
    else {
     y = V[f];
     cout << "The number that has been deleted from the queue is: " << y << endl;
     f=f+1;
   }

}

void display() {
     cout << "The elements in the queue are: " << endl;
     for (int i=f; i<=r; i++){
        cout << V[i] << " " << endl;
     }

     if (f==-1) {
        cout << "EMPTY QUEUE" << endl;
     }
}

int main()
{
   int x, y, number;

   cout << "You have the following options: " << endl;
   cout << "1) Enqueue" << endl;
   cout << "2) Dequeue" << endl;
   cout << "3) Display queue" << endl;
   cout << "4) Exit" << endl;

   do {
         cout << "Choose one and enter one number from the options" << endl;
         cin >> number;

         if (number==1){
            cout << "Enter the number you wish to enqueue: " << endl;
            cin >> x;
            enqueue(x);
         }
         else if (number==2) {
            dequeue(y);
            display();
         }
         else if (number==3) {
            display();
         }
         else if (number==4) {
            break;
         }
         else {
            cout << "You have entered an invalid number!" << endl;
         }
   } while (number<=4);

   return 0;
}

