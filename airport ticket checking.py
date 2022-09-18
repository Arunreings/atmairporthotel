import mysql.connector
from mysql.connector import Error
connection = mysql.connector.connect(
    host="localhost",
    database="airport_ticket",
    user="root",
    password="#Arun2002"
)
mycursor=connection.cursor()
n=int(input("click 1 for Buisness class 2 for First class  3 for Second Class "))
if n==1:
   print("Buisness class=15000")
if n==2:
    print("First class is 10000")
if n==3:
    print("Second class is 5000")
name=input("Enter your name:  ")
place=input("Enter your place name: ")
seattype=input("Enter your seat_type: ")
Number=int(input("Enter your mobile number: "))


myname=name
p=place
type=seattype
num=Number
val=(myname,p,type,num)
sql="Insert into passenger(passenger_name,place,seat_type,Mobile_number)Values(%s,%s,%s,%s)"
mycursor=connection.cursor()
mycursor.execute(sql,val)
connection.commit()
print("Welcome To Chennai Airlines")
Ticket=input("Show your Ticket and Original id  ")
if Ticket=="valid":
    print("You can go for checkin process")
if Ticket=="not valid":
    print("Your ticket or id is not original")
Vaccine=input("Show your Covid Vaccine Certificate ")
if Vaccine=="valid":
    print("you can go")
if Vaccine=="not valid":
    print("you must be vaccinated to fly in airways")
PCRChecking=input("Show your covid Result ")
if PCRChecking=="Positive":
    print("You can go")
if PCRChecking=="negative":
    print("you are not allowed to fly and you must be corantined")
Passport=input("Show your passport ")
Visa=input("Visa ")
ID=input("ID ")
if Passport and Visa and ID=="valid":
    print("valid")
else:
    print("not valid")
EmigrationChecking=input("Show your passport ")
if EmigrationChecking=="valid":
    print("photo will be taken")
else:
    print("you are not eligible to fly")
Bagweight=input("show your luggage ")
if Bagweight<="20kg":
    print("you are now ready to board")
elif  Bagweight>"20kg":
    print("reduce your weight or pay extra amount")
Boardingpass=input("Show all your documents ")
if Boardingpass=="valid":
    print("you can now board the Flight")
else:
    print("you are not allowed to board")

