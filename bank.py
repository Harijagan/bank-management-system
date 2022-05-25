import mysql.connector as a
con=a.connect(host="localhost",user="root",password="Hari@jagan406",database="bank")
def openaccount():
    n=input("Enter Customer Name: ")
    ac=input("Enter Account No. :")
    db=input("Enter D.O.B :")
    p=input("Enter phone No. :")
    ad=input("Enter Address :")
    ob=int(input("Enter the Opening Balanace :"))
    data1=(n,ac,db,ad,p,ob)
    data2=(n,ac,ob)
    sql1='insert into account values(%s,%s,%s,%s,%s,%s)'
    sql2='insert into amount values(%s,%s,%s)'
    c=con.cursor()
    c.execute(sql1,data1)
    c.execute(sql2,data2)
    con.commit()
    print("account opened successfully...!")
    main()
def depositeamount():
    am=int(input("Enter Amount :"))
    ac=input("Enter Account No :")
    a='select balance from amount where accountno=%s'
    data=(ac,)
    c=con.cursor()
    c.execute(a,data)
    myresult=c.fetchone()
    tam=myresult[0]+am
    sql="update amount set balance=%s where accountno=%s"
    d=(tam,ac)
    c.execute(sql,d)
    con.commit()
    print("Money Added Successfully...!")
    main()

def withdrawnamount():
    am=int(input("Enter Amount :"))
    ac=input("Enter Account No :")
    a='select balance from amount where accountno=%s'
    data=(ac,)
    c=con.cursor()
    c.execute(a,data)
    myresult=c.fetchone()
    tam=myresult[0]-am
    sql="update amount set balance=%s where accountno=%s"
    d=(tam,ac)
    c.execute(sql,d)
    con.commit()
    print("Money Removed Successfully...!")
    main()
    

def balanceenquiry():
    ac=input("Enter Account No :")
    a='select balance from amount where accountno=%s'
    data=(ac,)
    c=con.cursor()
    c.execute(a,data)
    myresult=c.fetchone()
    print("Balance for Account :",ac,"is",myresult[0])
    main()


def displaycustomerdetails():
    ac=input("Enter Account No :")
    a='select * from account where accountno=%s'
    data=(ac,)
    c=con.cursor()
    c.execute(a,data)
    myresult=c.fetchone()
    for i in myresult:
        print(i,end=" ")
    main()

def closeanaccount():
    ac=input("Enter Account No :")
    sql1='delete from account where accountno=%s'
    sql2='delete from amount where accountno=%s'
    data=(ac,)
    c=con.cursor()
    c.execute(sql1,data)
    c.execute(sql2,data)
    con.commit()
    main()



def main():
    print(""" 
    1. OPEN NEW ACCOUNT
    2. DEPOSIT AMOUNT
    3. WITHDRAWN AMOUNT
    4. BALANCE ENQUIRY
    5. DISPLAY CUSTOMER DETAILS
    6. CLOSE AN ACCOUNT
    """)
    choice=input("Enter Task No:")
    if choice=='1':
        openaccount()
    elif choice=='2':
        depositeamount()
    elif choice=='3':
        withdrawnamount()
    elif choice=='4':
        balanceenquiry()
    elif choice=='5':
        displaycustomerdetails()
    elif choice=='6':
        closeanaccount()
    else:
        print("Please select above choices only:")
        main()
main()