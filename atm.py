import mysql.connector
from mysql.connector import Error
connection = mysql.connector.connect(
    host="localhost",
    database="atm",
    user="root",
    password="#Arun2002"
)
mycursor = connection.cursor()
#cur.close()
#mydb.close()
print("ATM")
n=int(input("Click 1 for login & 0 for register: "))
password = " "
Name= " "
deposit= " "
id =" "

if n == 0:
    name=input("Enter the name: ")
    account=int(input("Enter your account Number: "))
    t= int(input("Enter starting amount to be deposite "))
    pwd=int(input("Set your password: "))

    myname=name
    password=pwd
    deposit=t
    id=account 

    val = (myname,password,deposit,id)

    sql = "Insert into Accountdetail(my_name, pass_word, de_posit, i_d ) VALUES (%s,%s,%s,%s)"
    mycursor = connection.cursor()

    mycursor.execute(sql,val)
    connection.commit()

if n==1:
    info = int(input("Enter ur id: "))
    password=int(input('Enter your password: '))
    mycursor = connection.cursor()
    mycursor.execute("select * from Accountdetail where i_d =%s"%(info))
    row=mycursor.fetchone()
    if mycursor.rowcount == 1:
        mycursor.execute("select * from Accountdetail where pass_word =%s"%(password))
        row = mycursor.fetchone()
        if mycursor.rowcount == 1:
            print("login succesfull")
            d = int(input("Enter 0 for deposit or 1 for withdraw or 3 for exist: "))
            if d == 1:
                a=int(input("how much you want to withdraw: "))
                #mycursor.execute("select de_posit=%s from Accountdetail where pass_word =%s"%(password))
                col=mycursor.fetchone()
                x=list(col)
                for i in x:
                    z=(int(i))
                    c=z-a
                mycursor.execute("Update de_posit=%s from Accountdetail  where pass_word=%s" %(c,password))
                col=mycursor.fetchone()
                x=list(col)
                for i in x:
                    z=(int(i))
                    c=z-a
                mycursor.execute("Update de_posit=%s from Accountdetail where pass_word=%s"% (c,password))
            if d==0:
                a = int(input("How much you want to deposit: "))
                #mycursor.execute("select de_posit=%s from Accountdetail where pass_word=%s"%(password))
                col=mycursor.fetchone()
                
                #x=list(col)
                
                for i in x:
                    z = (int(i))
                    c=z+a
                #mycursor.execute("Update de_posit=%s from Accountdetail where pass_word=%s"%(c,password))
            
            if d == 3:
                print("Logged out Succesfully")
        else:
            print("Invalid password")
    else:
        print("Account doesnot exist")
        connection.commit()