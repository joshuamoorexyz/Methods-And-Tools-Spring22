#Methods and tools Group assignment
#main menu program


from collections import UserDict
import mysql.connector
import sys
from getpass import getpass

#driver code
# # Connect to server
cnx = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="joshuamoorexyz",
    password="password1",
    db="methodsnew")

print(cnx)

# Get a cursor
cur = cnx.cursor()

#classes

class Account:

    def CreateAccount(Password, Name,Email,ShippingInfo,PaymentInfo):

        cur.execute('INSERT INTO account (Password, Name,Email,ShippingInfo,OrderHistory,PaymentInfo) VALUES (%s, %s, %s, %s, %s, %s)',(Password, Name,Email,ShippingInfo,0,PaymentInfo))
        cnx.commit() # # we commit(save) the records to the table

        #account =cur.execute('SELECT * FROM account WHERE Name = %s',("joeyflowey"))

  
        print(cur.rowcount, "record(s) inserted.")
        return True #return true if account created sucessful
      


    def EditAccount(Userid,Password,Name,Email,ShippingInfo,PaymentInfo):

        query = 'INSERT INTO account WHERE Userid = userid (Userid,Password, Name,Email,ShippingInfo,PaymentInfo) VALUES (%s, %s, %s, %s, %s, %s)'
        val = (Userid,Password,Name,Email,ShippingInfo,PaymentInfo)

        #push to database
        cur.execute(query,val)

        account =cur.fetchone()
        if account:
            cnx.commit() # # we commit(save) the records to the table
            print(cur.rowcount, "record(s) inserted.")
            return True #return true if account created sucessful
        else:
            return False


    def DeleteAccount(Userid):

        cur.execute('DELETE FROM account WHERE UserId = %s',(Userid,))
        cnx.commit() # # we commit(save) the records to the table


    def login(x,y):


        cur.execute('SELECT * FROM account WHERE UserID = %s AND Password = %s', (x, y,))
        # Fetch one record and return result
        account = cur.fetchone()
        if account:
            ID=x
            return True
            # Redirect to home page
        else:
            return False


            return False







    def EditShiipingInfo(Userid):


        #get new shipping info from the user
        print("\nNew Shipping Info: ")
        shipp=str(input())
        cur.execute('UPDATE account SET ShippingInfo = %s WHERE UserID=%s', (shipp,Userid))
        cnx.commit() # # we commit(save) the records to the table


    def EditPaymentInfo(Userid):


        #get new shipping info from the user
        print("\nNew Payment Info: ")
        payy=str(input())
        cur.execute('UPDATE account SET PaymentInfo = %s WHERE UserID=%s', (payy,Userid))
        cnx.commit() # # we commit(save) the records to the table


    def showaccountinfo():
        Userid=str(input())
        cur.execute('SELECT * FROM account WHERE UserID=%s', (Userid,))
        result = cur.fetchone()
        print(result)
        


    
class Inventory:
    def printinventoryelec():
        cur.execute('SELECT * FROM Inventory WHERE Category = 1')
        result = cur.fetchall()
  
# loop through the rows
        for row in result:
          print(row)
          print("\n")

    def printinventorygarden():
        cur.execute('SELECT * FROM Inventory WHERE Category = 2')
        result = cur.fetchall()
  
# loop through the rows
        for row in result:
          print(row)
          print("\n")


    def printinventoryhealth():
        cur.execute('SELECT * FROM Inventory WHERE Category = 3')
        result = cur.fetchall()
  
# loop through the rows
        for row in result:
          print(row)
          print("\n")          

class ShoppingCart:    
    def AddItem():
        itemid=str(input())
        cur.execute('INSERT INTO methodsnew.ShoppingCart (Itemid,Price,Category) SELECT Itemid,Price,Stock FROM methodsnew.Inventory WHERE Itemid= %s',(itemid,))
        cnx.commit() # # we commit(save) the records to the table

        # Fetch one record and return result
        #     account = cur.fetchone()
        #     if account:
        #         return True
        #     # Redirect to home page
          
        # else:
        #     return False
        #check that item has > 0 stock

        #if not then print a statement and dont add


        #add total to totalcart

    def printitems():
        cur.execute('SELECT * FROM ShoppingCart')
        result = cur.fetchall()
  
# loop through the rows
        print("\nItems in cart:")
        print("\n----------------------")
        print("\n\nItemID, Category, Price, Stock")

        for row in result:
          print(row)
          print("\n")          



    def gettotalforitemsincart():
        print(cur.execute('SELECT SUM(Price) FROM ShoppingCart'))


    def deleteitemfromcart():
        itemid=str(input())
        cur.execute('delete FROM ShoppingCart WHERE Itemid = %s',(itemid,))




    def deleteallitemsfromcart():
        cur.execute('delete FROM ShoppingCart')


    

    def checkoutitemsincart():
        print("\n---------------------------------------------")
        ShoppingCart.deleteallitemsfromcart() #delete items from the cart

#main loop for menu driven program

loggedin=False
while(True):
    while(loggedin==False):
        print("--------------------------------------------------------")
        print("\nCLI SHOPPING\n")
        print("\n1. Login")
        print("\n2. Create Account")
        print("\n3. Exit Program")

        print("\n\n Enter Choice:")
        choice=int(input())

        print("--------------------------------------------------------")

        #check to see if choice between 1 and 3
        if(choice<1 or choice>3):
            print("Invalid Input")
            exit()
        # if (choice == string):
       
            
        #user login page
        if(choice==1):
            print("--------------------------------------------------------")
        # try = 3;
        #     while(try >3):
        #         try = try-1
            username = input("Enter your UserID: ")
                #print("User Login")
                #print("\n\n Enter UserID:")
                #username=input()

                #check input
            userpassword = getpass("Enter the password: ")
                #print("\n\n password")
                #userpassword=input()

                #check input

                #check database to see if username and password are a match
            result=Account.login(username,userpassword)
            if(result==True):
                print("\nLogged in ..")
                loggedin=True

            if(result==False):
                print("\n UserID Or Pwd incorrect ...")
            #         print("You have %d valid attempts left" %(try))
            #         loggedin=False
            #  while(try=0):
                exit()


#create account page
        if(choice==2):
            print("--------------------------------------------------------")

            print("\nCreate Account Page")
            

            #check input

            print("\n\nPassword")
            newpassword=input()

            #check input

            print("\nName")
            firstname=input()
            #check input

            print("\nEmail")
            email=input()
            #checkinput


            print("\nShiping Info")
            shipinfo=input()
            #check input

            print("\nPayment Info")
            payment=input()



            #call create account function with these inputs to store in the database
            result=Account.CreateAccount(newpassword, firstname,email,shipinfo,payment)

            if(result==True):
                print("\nAccount creation sucess")

            if(result==False):
                print("\n Account creation failed")

    #exit program choice

        if(choice==3):
            print("--------------------------------------------------------")

            print("\nExiting ...")
            sys.exit(1)   




            #after login has succeeded
    while(loggedin==True):
        print("--------------------------------------------------------")

        print("\nCLI SHOPPING")
        print("\n1. Categories")
        print("\n2. Cart Information")
        print("\n3. Account")  
        print("\n4. Exit Program")    


        print("\n\nEnter Choice:")
        choice=int(input())

        print("--------------------------------------------------------")


        #check input
        if(choice<1 or choice>4):
            print("Invalid Input")
            exit() 

        if(choice==1):
            print("--------------------------------------------------------")

            print("\nCategories")
            print("\n\n1. Electronics")
            print("\n2. Garden")
            print("\n3. Health")


            print("\n\nEnter Choice:")
            choice1=int(input())
            print("--------------------------------------------------------")


                 #check input
            if(choice1<1 or choice1>3):
                print("Invalid Input")
                exit()     


        #category 1
            if(choice1==1):
                print("--------------------------------------------------------")

                print("\nElectronics")

            #print all items in category Electronics (1)
                Inventory.printinventoryelec()





            if(choice1==2):
                print("--------------------------------------------------------")

                print("\nGarden")
                Inventory.printinventorygarden()





            if(choice1==3):
                print("--------------------------------------------------------")

                print("\nHealth")


                print("\n\nEnter Choice:")
                Inventory.printinventoryhealth()

            #cartinformation

        if(choice==2):
            print("\nCart Information")
            print("\n\n1. Add items to Cart")
            print("\n\n2. Items in Cart")
            print("\n3. Total for items in Cart")
            print("\n4. Remove Item")
            print("\n5. Checkout Items in Cart")

            print("\n\nEnter Choice:")
            choice1=int(input())


            #check input
            if(choice1<1 or choice1>5):
                print("Invalid Input")
                exit()   


      
            if(choice1==1):
                print("--------------------------------------------------------")
                #call add item function
                print("\nEnter item ID")
                # item=int(input())
                # iteminfo=Inventory.GetItem(item)
                # for x in iteminfo:
                #     print(x)
                print("\nWhich item ID to add:")

          

                ShoppingCart.AddItem()

                
            if(choice1==2):
                print("--------------------------------------------------------")
                #call show items function


                print("\mAll items are currently in cart:")

                print("\n")

                #call print items function for ShoppingCart

                ShoppingCart.printitems()




            if(choice1==4):
                print("--------------------------------------------------------")
                #call checkout items function
                total=ShoppingCart.gettotalforitemsincart()
                print(total)


            if(choice1==4):
                print("--------------------------------------------------------")
                #call remove item function
                print("Which itemID do you want to remove?")
                ShoppingCart.deleteitemfromcart()

            if(choice1==5):
                print("--------------------------------------------------------")
                #call checkout items function
                ShoppingCart.checkoutitemsincart()


            #account
        if(choice==3):
            print("\n Account Information")
            print("\n1. Show account Info")
            print("\n2. Update Shipping Info")
            print("\n3. Update Payment Info")
            print("\n4. Delete Account")

            print("\n\nEnter Choice:")
            choice1=int(input())


            #check input
            if(choice1<1 or choice1>4):
                print("Invalid Input")
                exit()   

            if(choice1==1):
                print("--------------------------------------------------------")
                #call update shipping info function
                Account.showaccountinfo()


            if(choice1==2):
                print("--------------------------------------------------------")
                #call update shipping info function
                Account.EditShiipingInfo(username)


            if(choice1==3):
                print("--------------------------------------------------------")
                #call update shipping info function
                Account.EditShiipingInfo(username)

            if(choice1==4):
                print("--------------------------------------------------------")
                #call update payment info function
                Account.EditPaymentInfo(username)



            if(choice1==5):
                print("--------------------------------------------------------")
                #call delete account function
                Account.DeleteAccount(username)



        if(choice==4):
            print("--------------------------------------------------------")

            print("\nExiting ...")
            cnx.close() # Close connection
            sys.exit(1)  
            


    

