#include <iostream>


int main(int argc, char const *argv[])
{
bool loggedin=false;
	//logged in bool
	/* code */
//start menu
while(1){


	

while (!loggedin){
std::cout<<"\nCLI Shopping\n";
//before login
std::cout<<"\n1. Login";
std::cout<<"\n2. Create Account";
std::cout<<"\n3. Exit Program";

std::cout<<"\n\n Enter choice: ";
int choice;
std::cin>>choice;

//check to see if choice between 1 and 3
if(choice<1 || choice>3){
	std::cout<<"Invalid input";
	exit(EXIT_FAILURE);
}

//user login page
if(choice==1){
std::cout<<"\n User Login";
std::cout<<"\n\n UserID";
//std::string username=std::cin>>(username);

//check input


std::cout<<"\n\n Password";
//std::string password=std::cin>>(username);


//check input







//check to see if userID and password match 



}
//Create account Page
if(choice==2){

std::cout<<"\n Create Account Page";
std::cout<<"\n\n UserID";
//std::string username=std::cin>>(username);


//check input

std::cout<<"\n\n Password";
//std::string username=std::cin>>(username);


//check input


std::cout<<"\n\n Name";
//std::string username=std::cin>>(username);


//check input

std::cout<<"\n\n Email";
//std::string username=std::cin>>(username);


//check input

std::cout<<"\n\n Shipping Info <address>";
//std::string username=std::cin>>(username);


//check input

std::cout<<"\n\n Payment Info <card number";
//std::string username=std::cin>>(username);


//check input



//call class object with create account function to create account




}

//just exit program
if(choice==3){
std::cout<<"\n Exiting ..";
exit(EXIT_SUCCESS);


}

}

while(loggedin==true){
//after login

std::cout<<"\nCLI Shopping\n";
//before login
std::cout<<"\n1. Categories";
std::cout<<"\n2. Cart Information";
std::cout<<"\n3. Account";
std::cout<<"\n4. Exit Program";


std::cout<<"\n\n Enter choice: ";
int choice;
std::cin>>choice;


//check to see if choice between 1 and 3
if(choice<1 || choice>4){
	std::cout<<"Invalid input";
	exit(EXIT_FAILURE);
}




if(choice==1){
std::cout<<"\n Categories";
std::cout<<"\n\n1. Electronics";
std::cout<<"\n2. Garden";
std::cout<<"\n3. Health";

std::cout<<"\n\n Enter choice: ";
int choice1;
std::cin>>choice1;


//check to see if choice between 1 and 3
if(choice1<1 || choice1>3){
	std::cout<<"Invalid input";
	exit(EXIT_FAILURE);
}

//category 1
if(choice1==1){

std::cout<<"\n Electronics";
std::cout<<"\n\n1. Items";
std::cout<<"\n2. Price";
std::cout<<"\n3. Stock";


std::cout<<"\n\n Enter choice: ";
int choice2;
std::cin>>choice2;

//all items in electronics

if(choice2==1){

//get all item names from the database and print them here

}
//all prices in electronics

if(choice2==2){

//get all prices from the database and print them here


}
//all stock in electronics
if(choice2==3){

//get all stock from the database and print them here


}

}

//category 2
if(choice1==2){


std::cout<<"\n Garden";
std::cout<<"\n\n1. Electronics";
std::cout<<"\n2. Garden";
std::cout<<"\n3. Health";




}

//category 3
if(choice1==3){


std::cout<<"\n Health";
std::cout<<"\n\n1. Electronics";
std::cout<<"\n2. Garden";
std::cout<<"\n3. Health";




}












}
//CartInformation
if(choice==2){
std::cout<<"\n Cart Information";
std::cout<<"\n\n1. Items in Cart";
std::cout<<"\n2. Remove Item";
std::cout<<"\n3. Checkout Items in Cart";

std::cout<<"\n\n Enter choice: ";
int choice1;
std::cin>>choice1;


//check to see if choice between 1 and 3
if(choice1<1 || choice1>3){
	std::cout<<"Invalid input";
	exit(EXIT_FAILURE);
}


















}
//Account
if(choice==3){
std::cout<<"\n Account Information";
std::cout<<"\n\n1. Update Shipping Info";
std::cout<<"\n2. Update Payment Info";
std::cout<<"\n3. Edit Account";
std::cout<<"\n4. Delete Account";


std::cout<<"\n\n Enter choice: ";
int choice1;
std::cin>>choice1;


//check to see if choice between 1 and 3
if(choice1<1 || choice1>4){
	std::cout<<"Invalid input";
	exit(EXIT_FAILURE);

}










}







}

//main loop
}
	return 0;


}