#Methods and tools Group assignment
#main menu program


from collections import UserDict
import mysql.connector
import sys




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

# Execute a query
# cur.execute("SELECT * FROM Item")
# rows=cur.fetchall()
# for r in rows:
#     print(r)











#classes

class Account:

    def CreateAccount(Userid,Password,Name,Email,ShippingInfo,PaymentInfo):

        query = 'INSERT INTO Account (UserId,Password, Name,Email,ShippingInfo,PaymentInfo) VALUES (%s, %s, %s, %s, %s, %s)'
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


    def EditAccount(Userid,Password,Name,Email,ShippingInfo,PaymentInfo):

        query = 'INSERT INTO Account WHERE Userid = userid (Userid,Password, Name,Email,ShippingInfo,PaymentInfo) VALUES (%s, %s, %s, %s, %s, %s)'
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


    def DeleteAccount(Userid,Password,Name,Email,ShippingInfo,PaymentInfo):

        query = 'INSERT INTO Account WHERE Userid = userid (Userid,Password, Name,Email,ShippingInfo,PaymentInfo) VALUES (%s, %s, %s, %s, %s, %s)'
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




    def login(x,y):


        cur.execute('SELECT * FROM account WHERE UserID = %s AND Password = %s', (x, y,))
        # Fetch one record and return result
        account = cur.fetchone()
        if account:
            return True
            # Redirect to home page
        else:
            return False


    def logout(x,y):


        query = 'INSERT INTO Account (Userid,Password, Name,Email,ShippingInfo,PaymentInfo) VALUES (%s, %s, %s, %s, %s, %s)'
        val = (Userid,Password,Name,Email,ShippingInfo,PaymentInfo)
        cur.execute('SELECT * FROM Account WHERE UserID = %s AND Password = %s', (x, y,))
        # Fetch one record and return result
        account = cur.fetchone()
        if account:
            return True
            # Redirect to home page
        else:
            return False


    def AddOrderHistory():
        query = 'INSERT INTO Account (Userid,Password, Name,Email,ShippingInfo,PaymentInfo) VALUES (%s, %s, %s, %s, %s, %s)'
        val = (Userid,Password,Name,Email,ShippingInfo,PaymentInfo)
        cur.execute('SELECT * FROM Account WHERE UserID = %s AND Password = %s', (x, y,))
        # Fetch one record and return result
        account = cur.fetchone()
        if account:
            return True
            # Redirect to home page
        else:
            return False


    def ViewOrderHistory():
        query = 'INSERT INTO Account (Userid,Password, Name,Email,ShippingInfo,PaymentInfo) VALUES (%s, %s, %s, %s, %s, %s)'
        val = (Userid,Password,Name,Email,ShippingInfo,PaymentInfo)
        cur.execute('SELECT * FROM Account WHERE UserID = %s AND Password = %s', (x, y,))
        # Fetch one record and return result
        account = cur.fetchone()
        if account:
            return True
            # Redirect to home page
        else:
            return False

    def EditShiipingInfo():
        query = 'INSERT INTO Account (Userid,Password, Name,Email,ShippingInfo,PaymentInfo) VALUES (%s, %s, %s, %s, %s, %s)'
        val = (Userid,Password,Name,Email,ShippingInfo,PaymentInfo)
        cur.execute('SELECT * FROM Account WHERE UserID = %s AND Password = %s', (x, y,))
        # Fetch one record and return result
        account = cur.fetchone()
        if account:
            return True
            # Redirect to home page
        else:
            return False

    def EditPaymentInfo():
        query = 'INSERT INTO Account (Userid,Password, Name,Email,ShippingInfo,PaymentInfo) VALUES (%s, %s, %s, %s, %s, %s)'
        val = (Userid,Password,Name,Email,ShippingInfo,PaymentInfo)
        cur.execute('SELECT * FROM Account WHERE UserID = %s AND Password = %s', (x, y,))
        # Fetch one record and return result
        account = cur.fetchone()
        if account:
            return True
            # Redirect to home page
        else:
            return False


 
    
# class Inventory:
#     item = 0
#     Category = ""
#     Price = 0.00
#     Stock = 0

#     def AddItem(item, Category, Price, Stock):

#     def delete_item():

#     def check_price():
    
#     def edit_stock():

#     def check_stock():
    
#     def set_category():
        










    
#     def additem(a,b,c,d):
#         Item=a
#         Category=b
#         Price=c
#         Stock=d

#     #delete item


#     #check price


#     #edit stock


#     #check stock


#     #set category


# class ShoppingCart:
    
#     total=0.0


# # class Categories:
#     # Electronics()
#     # Garden()
#     # Health()
















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
            
        #user login page
        if(choice==1):
            print("--------------------------------------------------------")

            print("User Login")
            print("\n\n Enter UserID:")
            username=input()

            #check input

            print("\n\n password")
            userpassword=input()

            #check input

            #check database to see if username and password are a match
            result=Account.login(username,userpassword)
            if(result==True):
                print("\nLogged in ..")
                loggedin=True

            if(result==False):
                print("\n UserID Or Pwd incorrect ...")
                loggedin=False



            

#create account page
        if(choice==2):
            print("--------------------------------------------------------")

            print("\nCreate Account Page")
            

            #check input

            print("\n\nPassword")
            newpassword=input()

            #check input

            print("\nFirst Name")
            firstname=input()

            #check input
            print("\nLast Name")
            lastname=input()

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
            result=Account.__init__(newpassword, firstname+lastname, email, shipinfo, payment)

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
        choice=int(input(choice))

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
            choice1=input(choice1)
        print("--------------------------------------------------------")


                 #check input
        if(choice1<1 or choice1>3):
            print("Invalid Input")
            exit()     


        #category 1
        if(choice1==1):
            print("--------------------------------------------------------")

            print("\nElectronics")
            print("\n\n1. Items")
            print("\n2. Price")
            print("\n3. Stock")

            print("\n\nEnter Choice:")
            choice2=int(input(choice2))

        print("--------------------------------------------------------")

                 #check input
        if(choice2<1 or choice2>3):
            print("Invalid Input")
            exit()     

        if(choice2==1):
            print("--------------------------------------------------------")

            #select all items where category is Electronics
            print("here data")

        if(choice2==2):
            print("--------------------------------------------------------")

            #Get all items price where category is Electronics
            print("Here prices")

        if(choice2==3):
            print("--------------------------------------------------------")
    
            #get all stock from database where category is electronics
            print("stuff")


        if(chocie1==2):
            print("--------------------------------------------------------")

            print("\nGarden")
            print("\n\n1. Items")
            print("\n2. Price")
            print("\n3. Stock")

            print("\n\nEnter Choice:")
            choice2=int(input(choice2))
            print("--------------------------------------------------------")


                 #check input
        if(choice2<1 or choice2>3):
            print("Invalid Input")
            exit()     

        if(choice2==1):
            print("--------------------------------------------------------")

            #select all items where category is Electronics
            print("here data")

        if(choice2==2):
            #Get all items price where category is Electronics
            print("Here prices")

        if(choice2==3):
            print("--------------------------------------------------------")

            #get all stock from database where category is electronics
            print("stuff")



        if(chocie1==3):
            print("--------------------------------------------------------")

            print("\nHealth")
            print("\n\n1. Items")
            print("\n2. Price")
            print("\n3. Stock")

            print("\n\nEnter Choice:")
            choice2=int(input(choice2))


                 #check input
        if(choice2<1 or choice2>3):
            print("Invalid Input")
            exit()     

        if(choice2==1):
            #select all items where category is Electronics
            print("here data")

        if(choice2==2):
            #Get all items price where category is Electronics
            print("Here prices")

        if(choice2==3):
            #get all stock from database where category is electronics
            print("stuff")




            #cartinformation

        if(choice==2):
            print("\nCart Information")
            print("\n\n1. Items in Cart")
            print("\n2. Remove Item")
            print("\n3. Checkout Items in Cart")

            print("\n\nEnter Choice:")
            choice1=int(input(chooice1))


            #check input
        if(choice1<1 or choice1>3):
            print("Invalid Input")
            exit()   




            #account
        if(choice==3):
            print("\n Account Information")

            print("\n\n1. Update Shipping Info")
            print("\n2. Update Payment Info")
            print("\n3. Edit Account")
            print("\n4. Delete Account")

            print("\n\nEnter Choice:")
            choice1=int(input(chooice1))


            #check input
        if(choice1<1 or choice1>4):
            print("Invalid Input")
            exit()   
# Close connection
cnx.close()