print("WELCOME TO ARUN REINGS HOTEL")
menus=["parota","dosa","Biriyani","Chappathi","Idly","Poori","Pongal","ChickenFriedRice","Tandoori","ChilliChicken","Mojito","Faluda"]
parota_amount=10
dosa_amount=20
Biriyani_amount=100
Chappathi_amount=15
Idly_amount=5
Poori_amount=10
Pongal_amount=30
ChickenFriedRice_amount=110
Tandoori_amount=250
Chillichicken_amount=100
Mojito_amount=60
Faluda_amount=150                       
Your_order=input("Give your order: ").upper()

def par_amt(a,b):
    Total=a*b
    print(f"Your total bill is Rs {Total}")
    
if Your_order in menus:
    print(f"yes your {Your_order} is availabe")
How_many=int(input(f"How many {Your_order} you want "))
if Your_order=="parota".upper():
        par_amt(parota_amount,How_many)

def dosa_amt(a,b):
    Total=a*b
    print(f"You total bill is Rs{Total} ")
if Your_order=="dosa".upper():
    dosa_amt(dosa_amount,How_many)

def biriyani_amt(a,b):
    Total=a*b
    print(f"Your total bill is Rs {Total}")
if Your_order=="Biriyani".upper():
    biriyani_amt(Biriyani_amount,How_many)

def chappathi_amt(a,b):
    Total=a*b
    print(f"Your total bill is Rs {Total}")
if Your_order=="Chappathi".upper():
    chappathi_amt(Chappathi_amount,How_many)

def idly_amt(a,b):
    Total=a*b
    print(f"Your total bill is Rs {Total}")
if Your_order=="Idly".upper():
    idly_amt(Idly_amount,How_many)

def Poori_amt(a,b):
    Total=a*b
    print(f"Your total bill is Rs {Total}")
if Your_order=="Poori".upper():
    Poori_amt(Poori_amount,How_many)

def Pongal_amt(a,b):
    Total=a*b
    print(f"Your total bills is Rs {Total}")
if Your_order=="Pongal".upper():
    Pongal_amt(Pongal_amount,How_many)

def ChickenFriedrice_amt(a,b):
    Total=a*b
    print(f"Your total bill is Rs {Total}")
if Your_order=="ChickenFriedRice".upper():
    ChickenFriedrice_amt(ChickenFriedRice_amount,How_many)

def Tandoori_amt(a,b):
    Total=a*b
    print(f"Your total bill is Rs {Total}")
if Your_order=="Tandoori".upper():
    Tandoori_amt(Tandoori_amount,How_many)

def chillichicken_amt(a,b):
    Total=a*b
    print(f"Your Total bill is Rs{Total}")
if Your_order=="ChilliChicken".upper():
    chillichicken_amt(Chillichicken_amount,How_many)

def mojito_amt(a,b):
    Total=a*b
    print(f"Your total bill is Rs {Total}")
if Your_order=="Mojito".upper():
    mojito_amt(Mojito_amount,How_many)

def faluda_amt(a,b):
    Total=a*b
    print(f"Your total bill is {Total}")
if Your_order=="Faluda".upper():
    faluda_amt(Faluda_amount,How_many)
