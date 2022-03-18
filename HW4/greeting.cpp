#include "greeting.h"
#include <string>
Greeting::Greeting()
{

}

// setter
void Greeting::setName(string name)
{
    this->name = name;
}

// getter
string Greeting::getName()
{
    return name;
}

