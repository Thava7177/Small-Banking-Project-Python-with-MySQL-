# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 17:41:54 2024

@author: thava
"""
import random
import sys
import mysql.connector
from tabulate import tabulate

try:
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Thava&90",
        database="python_db"
    )
    res = con.cursor()
except :
    print("\t\t\tSorry Connection Error Please Check Connection...")
    sys.exit(1)
    
def create_table():
    res.execute("show tables")
    tables1= res.fetchall()
    tables=[i[0] for i in tables1]
    if 'accounts' in tables:
        return
    else:
        create_table='''create table accounts(
        Account_no bigint not null unique,
        Cname varchar(25) not null,
        Age int ,
        Amount float default 0,
        Place varchar(25),
        Password varchar(25)
        );'''
        res.execute(create_table)
        print("\t\t\tTable created successfully")
        return
        
        
def get_name():
    while True:
        name = input("\nEnter your name: ")
        if any(char.isdigit() for char in name):
            print("\nNames should not contain numbers. Please try again.")
        else:
            return name
        
        
def get_age():
    while True:
        try:
            age=int(input("\nEnter Your Age :"))
            if age>0 and age<101:
                return age
            else:
                print("\nEnter Your Correct Age ...")
        except ValueError:
            print("\nAge Must be Number, Please Try again...")

def get_amount():
    while True:
        try:
            amount=int(input("\nEnter Initial deposit: "))
            return amount
        except ValueError:
            print("\nAmount Must be Number, Please Try agin...")

def get_password():
    while True:
        pass1=input("\nCreate a Password Within 25 Character :")
        pass2=input("\nRe-Enter Password :")
        if pass1==pass2:
            return pass1
        else:
            print("Passwords do not match, Please Try again...")
            
def get_district():
    while True:
        district = input("\nEnter Your District: ")
        if any(char.isdigit() for char in district):
            print("\nDistrict should not contain numbers. Please try again...")
        else:
            return district
        
def deposit_amount():
    while True:
        try:
            amount=int(input("\nEnter deposit Amount: "))
            return amount
        except ValueError:
            print("\nAmount Must be Number, Please Try agin...")
            
def withdraw_amount():
    while True:
        try:
            amount=int(input("\nEnter Withdraw Amount: "))
            return amount
        except ValueError:
            print("\nAmount Must be Number, Please Try agin...")
    
def Care():
    try:
        def insert(a, b, c, d, e, f):
            sql = "INSERT INTO accounts (Account_no, Cname, Age, Amount, Place, Password) VALUES (%s, %s, %s, %s, %s, %s)"
            user = (a, b, c, d, e, f)
            res.execute(sql, user)
            con.commit()
            
        def create_acc():
            print("\n\t\t\tPlease Enter Details ...")
            Account_no = random.randint(10**10, 10**11 - 1)
            Name = get_name()
            Age = get_age()
            Amount = get_amount()
            Place = get_district()
            Pass = get_password()
            insert(Account_no, Name, Age, Amount, Place, Pass)
            print(f"\n\t\t\tAccount Successfully Created... Mr/Ms {Name} and Note your Account Number: {Account_no} ")
            ex_customer_menu()
            
        def deposit():
            try:
                Ac=int(input("\nEnter Your Account Number :"))
            except ValueError:
                print("\nEnter Valid Account Number...")
                ex_customer_menu()
            Ps=input("\nEnter Your Password :")
            try:
                res.execute("select * from accounts where Account_no=%s",(Ac,))
                rows=res.fetchall()
                t1,t2,t3,t4,t5,t6=rows[0]
            except IndexError:
                print("\nAccount Number Or Password is Not Matching , Please Try Again... ")
                ex_customer_menu()
            if Ac==t1 and Ps==t6:
                am=deposit_amount()
                t4+=am
                res.execute("UPDATE accounts SET Amount=%s WHERE Account_no=%s",(t4,t1))
                con.commit()
                print(f"\n\t\t\tMr {t2} Deposit {am} Successfully...")
            else:
                print("\nAccount Number Or Password is Not Matching ... ")
                ex_customer_menu()
            
        def withdraw():
            try:
                Ac=int(input("\nEnter Your Account Number :"))
            except ValueError:
                print("\nEnter Valid Account Number...")
                ex_customer_menu()
            Ps=input("\nEnter Your Password :")
            try:
                res.execute("select * from accounts where Account_no=%s",(Ac,))
                rows=res.fetchall()
                t1,t2,t3,t4,t5,t6=rows[0]
            except IndexError:
                print("\nAccount Number Or Password is Not Matching , Please Try Again... ")
                ex_customer_menu()
            if Ac==t1 and Ps==t6:
                am=withdraw_amount()
                if t4>=am:
                    t4-=am
                    res.execute("UPDATE accounts SET Amount=%s WHERE Account_no=%s",(t4,t1))
                    con.commit()
                    print(f"\n\t\t\tMr {t2} Amount {am} Withraw Successfully....")
                else: 
                    print(f"\nMr {t2} Your Account Has Low Balance.. Your Balrnce is: {t4} ")
            else:
                print("\nAccount Number Or Password is Not Maching ... ")
                ex_customer_menu()
            
        def check_bal():
            try:
                Ac=int(input("\nEnter Your Account Number :"))
            except ValueError:
                print("\nEnter Valid Account Number...")
                ex_customer_menu()
            Ps=input("\nEnter Your Password :")
            print("\n")
            try:
                res.execute("select * from accounts where Account_no=%s",(Ac,))
                rows=res.fetchall()
                t1,t2,t3,t4,t5,t6=rows[0]
                
            except IndexError:
                print("\nAccount Number Or Password is Not Matching , Please Try Again... ")
                ex_customer_menu()
            if Ac==t1 and Ps==t6:
                print(tabulate(rows,headers=["Account_No","Name","Age","Account_Bal","District","Password"]))
                print("\n")
            else:
                print("\nAccount Number Or Password is Not Matching so, Please Try Again... ")
                ex_customer_menu()
            
        def Delete1():
            
            print("\nAre You Sure To Delete Account Press 1 ")
            print("\nBack Menu press 2")
            try:
                sa=int(input())
            except ValueError:
                print("\nEnter only press 1 or 2  please Try Again ...")
                Delete1()
            if sa==1:
                Delete()
            elif sa==2:
                print("\n\t\t\tThank You !")
                ex_customer_menu()
            else:
                print("Invalid Input Please Try Again ..")
                Delete1()
                
                
        def Delete():
            try:
                Ac=int(input("\nEnter Your Account Number :"))
            except ValueError:
                print("\nEnter Valid Account Number...")
                ex_customer_menu()
            Ps=input("\nEnter Your Password :")
            try:
                res.execute("select * from accounts where Account_no=%s",(Ac,))
                rows=res.fetchall()
                t1,t2,t3,t4,t5,t6=rows[0]
            except IndexError:
                print("\nAccount Number Or Password is Not Matching , Please Try Again... ")
                ex_customer_menu()
            if Ac==t1 and Ps==t6:
                
                res.execute("Delete from accounts where Account_no=%s",(Ac,))
                con.commit()
                print("\n\t\t\tYour Account Deleted Successfully....")
                print("\n\t\tNow Create New Account To Press 1 or press 3 To Exit ")
                main_menu()
            else:
                print("\nAccount Number Or Password is Not Matching ... ")
                ex_customer_menu()
 
        def main_menu():
            print("-------------------------------------------------------------------------------------------")
            print("\t\t\tWELCOME TO TN BANKING ")
            print("-------------------------------------------------------------------------------------------\n")
            print("\n\t\t\tPress 1 You are New Customer   ")
            print("\n\t\t\tPress 2 Existing Customer")
            print("\n\t\t\tPress 3 To Exit")
            print("-------------------------------------------------------------------------------------------")
            try:
                ch=int(input())
            except ValueError:
                print("\tEnter Valid Input 1 to 3...")
                main_menu()      
            if ch==1:
                create_acc()
            elif ch==2:
                ex_customer_menu()
            elif ch==3:
                print("\t\t\tThank You !")
                print(sys.exit(0))
            else:
                print("\tEnter Valid Input 1 to 3... Please Try Again...")
                main_menu()
            
         
             
        
        def ex_customer_menu():
            while True:
                print("-------------------------------------------------------------------------------------------")
                print("\n\t\t\tPress 1 To Check Balance ")
                print("\n\t\t\tPress 2 To Deposit ")
                print("\n\t\t\tPress 3 To withdraw ")
                print("\n\t\t\tPress 4 To Delete Account")
                print("\n\t\t\tPress 5 To back menu")
                print("-------------------------------------------------------------------------------------------")
                
                try:
                    ch1=int(input())
                except ValueError:
                    print("Enter Valid Input 1 to 5...")
                    ex_customer_menu()
                if ch1==1:
                    check_bal()
                elif ch1==2:
                    deposit() 
                elif ch1==3:
                    withdraw()
                elif ch1==4:
                    Delete1()
                elif ch1==5:
                    main_menu()
                else:
                    print("\tEnter Valid Input 1 to 5... Please Try Again...")
           
        
                
        main_menu()  
    except KeyboardInterrupt:
        print("\nKeyboardInterrupt Error ....")
        Care()
    
create_table()
Care()