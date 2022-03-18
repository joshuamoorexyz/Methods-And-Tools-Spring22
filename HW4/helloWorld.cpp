// library includes
#include <iostream>
#include <string>

using namespace std;

int main()
{
  cout << "Hello World" << endl << endl;

  string name;
  cout << "What's your name? ";
  getline(cin, name);

  cout << "Hello, " << name << endl;

  return 0;
}
