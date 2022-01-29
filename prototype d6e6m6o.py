import mysql.connector
myConnnection =""
cursor=""
userName=""
password =""
roomrent =0
restaurentbill=0
totalAmount=0
cid=""
def MYSQLconnectionCheck():
    global myConnection
    global userName
    global password
    userName = input("\n ENTER MYSQL SERVER'S USERNAME : ")
    password = input("\n ENTER MYSQL SERVER'S PASSWORD : ")
    myConnection=mysql.connector.connect(host="localhost",user=userName,passwd=password ,
    auth_plugin='mysql_native_password')
    if myConnection:
        print("\n CONGRATULATIONS ! YOUR MYSQL CONNECTION HAS BEEN ESTABLISHED !")
        cursor=myConnection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS HMS")
        cursor.execute("COMMIT")
        cursor.close()
        return myConnection
    else:
        print("\nERROR ESTABLISHING MYSQL CONNECTION CHECK USERNAME AND PASSWORD !")
def MYSQLconnection():
    global userName
    global password
    global myConnection
    global nid
    myConnection=mysql.connector.connect(host="localhost",user=userName,passwd=password , database="HMS" , auth_plugin='mysql_native_password' )
    if myConnection:
        return myConnection
    else:
        print("\nERROR ESTABLISHING MYSQL CONNECTION !")
        myConnection.close()

def registerUser():
    global nid
    if myConnection:
        cursor=myConnection.cursor()
        createTable ="(CREATE TABLE IF NOT EXISTS C_DETAILS(NID VARCHAR(20),C_NAMEVARCHAR(30),C_ADDRESS VARCHAR(30),C_AGE VARCHAR(30),C_COUNTRY VARCHAR(30) ,P_NO VARCHAR(30))"
        cursor.execute(createTable)
        nid = input("Enter Customer Identification Number : ")
        name = input("Enter Customer Name : ")
        address = input("Enter Customer Address : ")
        age= input("Enter Customer Age : ")
        nationality = input("Enter Customer Country : ")
        phoneno= input("Enter Customer Contact Number : ")
        sql = "INSERT INTO C_Details VALUES(%s,%s,%s,%s,%s,%s)"
        values= (nid,name,address,age,nationality,phoneno,)
        cursor.execute(sql,values)
        cursor.execute("COMMIT")
        print("\nNew Customer Entered In The System Successfully !")
        cursor.close()
    else:
        print("SORRY FOR THE ERROR")

def bookingRecord():
    global nid
    customer=searchCustomer()
    if customer:
        if myConnection:
            cursor=myConnection.cursor()
            createTable ="CREATE TABLE IF NOT EXISTS BOOKING_RECORD(NID VARCHAR(20),CHECK_INDATE ,CHECK_OUT DATE)"
            cursor.execute(createTable)
            checkin=input("\n Enter Customer CheckIN Date [ YYYY-MM-DD ] : ")
            checkout=input("\n Enter Customer CheckOUT Date [ YYYY-MM-DD ] : ")
            sql= "INSERT INTO BOOKING_RECORD VALUES(%s,%s,%s)"
            values= (nid,checkin,checkout)
            cursor.execute(sql,values)
            cursor.execute("COMMIT")
            print("\nCHECK-IN AND CHECK-OUT ENTRY MADE SUCCESSFULLY")
            cursor.close()
        else:
            print("SORRY FOR THE ERROR")

def roomRent():
    global nid
    customer=searchCustomer()
    if customer:
        global roomrent
        if myConnection:
            cursor=myConnection.cursor()
            createTable =""CREATE TABLE IF NOT EXISTS ROOM_RENT(NID VARCHAR(20),ROOM_CHOICE,INT,NO_OF_DAYS INT,PNO INT ,ROOMRENT INT)""
            cursor.execute(createTable)
            print ("\n ##### We have The Following Rooms For You #####")
            print (" 1. Super Deluxe ----> 3000 Rs.")
            print (" 2. luxury suite ----> 5000 Rs. ")
            print (" 3. family run in ----> 2500 Rs. ")
            roomchoice =int(input("Enter Your Option : "))
            pno=int(input("Enter no of people : "))
            noofdays=int(input("Enter No. Of Days : "))
            if roomchoice==1:
                roomrent = noofdays * pno * 3000
                print("Super Deluxe rent : ",roomrent)
            elif roomchoice==2:
                roomrent = noofdays * pno * 5000
                print("luxury suite rent : ",roomrent)
            elif roomchoice==3:
                roomrent = noofdays * pno * 2500
                print("family run in rent : ",roomrent)
            else:
                print("Sorry ,May Be You Are Giving Me Wrong Input, Please Try Again !!! ")
                return
            sql= "INSERT INTO ROOM_RENT VALUES(%s,%s,%s,%s,%s)"
            values= (cid,roomchoice,noofdays,pno,roomrent,)
            cursor.execute(sql,values)
            cursor.execute("COMMIT")
            print("Thank You , Your Room Has Been Booked For : ",noofdays , "Days" )
            print("Your Total Room Rent is : Rs. ",roomrent)
            cursor.close()
        else:
            print("SORRY FOR THE ERROR")
    


def Restaurent():
    global nid
    customer=searchCustomer()
    if customer:
        global restaurentbill
        if myConnection:
            cursor=myConnection.cursor()
                createTable ="""CREATE TABLE IF NOT EXISTS RESTAURENT(NID VARCHAR(20),CUISINEVARCHAR(30),QUANTITY VARCHAR(30),BILL VARCHAR(30))"""
                cursor.execute(createTable)
                print("1. Vegetarian Thali -----> 300 Rs.")
                print("2. Non-Vegetarian Thali -----> 500 Rs.")
                print("3. Continental sizzler -----> 750 Rs.")
                choice_dish = int(input("Enter Your Cusine : "))
                quantity=int(input("Enter Quantity : "))
                if choice_dish==1:
                    print("\nSO YOU HAVE ORDER: Vegetarian Thali ")
                    restaurentbill = quantity * 300
                elif choice_dish==2:
                    print("\nSO YOU HAVE ORDER: Non-Vegetarian Thali ")
                    restaurentbill = quantity * 500
                elif choice_dish==3:
                    print("\nSO YOU HAVE ORDER: Continental sizzler ")
                    restaurentbill= quantity * 750
                else:
                    print("Sorry ,May Be You Are Giving Me Wrong Input, Please Try Again !!! ")
                    return
                sql= "INSERT INTO RESTAURENT VALUES(%s,%s,%s,%s)"
                values= (nid,choice_dish,quantity,restaurentbill)
                cursor.execute(sql,values)
                cursor.execute("COMMIT")
                print("Your Total Bill Amount Is : Rs. ",restaurentbill)
                print("\n\n**** WE HOPE YOU WILL ENJOY YOUR MEAL ***\n\n" )
                cursor.close()
        else:
            print("SORRY FOR THE ERROR")
        
 
def totalAmount():
    global nid
    customer=searchCustomer()
    if customer:
        global grandTotal
        global roomrent
        global restaurentbill
        if myConnection:
            cursor=myConnection.cursor()
            createTable ="""CREATE TABLE IF NOT EXISTS TOTAL(NID VARCHAR(20),C_NAMEVARCHAR(30),ROOMRENT INT ,RESTAURENTBILL INT ,TOTALAMOUNT INT)"""
            cursor.execute(createTable)
            sql= "INSERT INTO TOTAL VALUES(%s,%s,%s,%s,%s)"
            name = input("Enter Customer Name : ")
            grandTotal=roomrent + restaurentbill
            values= (cid,name,roomrent,restaurentbill ,grandTotal)
            cursor.execute(sql,values)
            cursor.execute("COMMIT")
            cursor.close()
            print("\n **** CROWN PLAZA MIAMI **** CUSTOMER BIILING ****")
            print("\n CUSTOMER NAME : " ,name)
            print("\nROOM RENT : Rs. ",roomrent)
            print("\nRESTAURENT BILL : Rs. ",restaurentbill)
            print("\nTOTAL AMOUNT : Rs. ",grandTotal)
            cursor.close()
        else:
            print("SORRY FOR THE ERROR")


#main

            
myConnection = MYSQLconnectionCheck()
if myConnection:
    MYSQLconnection ()
    while(True):
        print("""1.Enter Customer Details,2.Booking Record,3.Calculate Room Rent,4.Calculate Restaurant Bil,5.GENERATE TOTAL BILL AMOUNT,6.EXIT """)
        choice = int(input("Enter Your Choice"))
        if choice == 1:
            registerUser()
        elif choice ==2:
            bookingRecord()
        elif choice ==3:
            roomRent()
        elif choice ==4:
            Restaurent()
        elif choice ==5:
            totalAmount()
        elif choice ==6:
            break
        else:
            print("Sorry ,May Be You Are Giving Me Wrong Input, Please Try Again !!! ")
else:
    print("SORRY FOR THE ERROR")

