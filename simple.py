import random
#import pandas as pd
import csv
Compte = {}
Clients = {}
ClientCompte = {}
numcl = 0
def add_client(mpc,soldec):
    global numcl
    numcl +=1
    generernumcompte = lambda code : str(numcl) + str(random.randint(0,100))
    numc = generernumcompte(numcl)
    Compte[numc] = soldec
    Clients[numcl] = mpc
    ClientCompte[numc] = numcl
    print("your account is created")
    print("your client number is :" , numcl)
    print("your account numbre is :", numc)
    #print(Compte)
    #print(ClientCompte)
    #print(Clients)

def delete_client(numcl,numC):
    if numcl in Clients:
        del Clients[numcl]
        if numC in Compte and ClientCompte:
            del Compte[numC]
            del ClientCompte[numC]
        return "your account is deleted !!"

    return "Inccorect information !!"


def modify_password(numCl, oldMP, newMP):
    if Clients[numCl] == oldMP:
        Clients[numCl] = newMP
        return "Password successfully updated."
    else:
        return "Incorrect password."
def Show_Balance(numc):
    if numc in Compte :
        return "Your Current Balance is :",Compte[numc]
    else :
        return "Your Account number not exist in our database try Again !!"
def Deposer(numc,argent):
    if numc in Compte:
        Compte[numc] += argent
        return "your Current Balance is",Compte[numc]
    else :
        return "your code doesnt exist try again !!"
def retirer(numc,SoldeR):
    if numc in Compte :
        if Compte[numc]>=SoldeR:
            Compte[numc] -=SoldeR
            return "your Current Balance is",Compte[numc]
        else :
            return "you dont have Enough Money to do this operation !!"
def savedatacsv():
    with open("idriss.csv","w+",newline="") as f1 :
        file = csv.writer(f1, delimiter=";")
        for key in Clients.items():
            file.writerow(key)


#add_client("idriss",500)
#add_client("ayoub",400)
#savedatacsv()
#print(Show_Balance(25))
#print(Deposer(25,400))
#print(retirer(25,300))
#print(modify_password(2,"idriss","anaNadi"))
#add_client(2,56,"wow",125)
#delete_client(56)
#dd_client

choix =""
while choix != "0":
    print("-------------------------------")
    print("1- Agence")
    print("2- Client")
    print("0- EXIT")
    choix = input("enter 1 or 2 : ")
    print("-------------------------------")
    if choix == "1":
        print("1- Add Account")
        print("2- Delete Account")
        choix = input("enter 1 or 2 : ")
        if choix == "1":
            code = input("enter your password :")
            solde = int(input("enter your current balance :"))
            add_client(code,solde)
            savedatacsv()
        if choix =="2":
            client_num = int(input("enter your client num :"))
            account_num = int(input("enter your account number :"))
            print(delete_client(client_num,account_num))
            savedatacsv()
    if choix =="2":
        print("1- Modify password")
        print("2- AfficheSolde")
        print("3- DeposeSoldeArgent")
        print("4- Retirer Argent")
        print("0 _ EXIT")
        choix = input("select a number : ")
        if choix == "1":
            clientnum = int(input("enter your your numcl numero de client :"))
            oldpass = input("enter your old password :")
            newpass = input("enter your new password :")
            print(modify_password(clientnum,oldpass,newpass))
            savedatacsv()
        if choix == "2":
            account_num = input("enter your account number :")
            print(Show_Balance(account_num))

        if choix == "3":
            account_num = input("enter your account number :")
            soldeajouter = int(input("enter la somme que vous avez ajouter :"))
            print(Deposer(account_num,soldeajouter))
        if choix == "4" :
            account_num = input("enter your account number :")
            solderetirer = int(input("enter la somme que tu peux retirer : "))
            print(retirer(account_num,solderetirer))

