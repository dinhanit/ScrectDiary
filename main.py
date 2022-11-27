import os
from datetime import date
from colored import fg
blue= fg('blue')
yellow= fg('yellow')

def hash(data):
    NewData =''
    key = 0
    for word in data:
        if ord(word) == 10:
            key = 10
        else:
            key = ord(word)+23
            if key > 126:
                key=key - 126 + 31
        NewData = NewData+chr(key)
    return NewData

def UnHash(data):
    NewData =''
    key = 0
    for word in data:
        if ord(word) == 10:
            key = 10
        else:
            key = ord(word)-23
            if key<32:
                key=key+126 - 31
        NewData = NewData+chr(key)
    return NewData

def HashPath(data):
    key = ''
    for w in data:
        key+=str(ord(w))
    return key

def Menu():
    print(yellow+'WELCOME TO SECRET DIARY')
    print('Create/Login')
    A=Account()
    choose = input('Choose: ')
    while choose.upper() not in ['CREATE','LOGIN']:
        prRed('WRONG CHOOSE')
        choose = input('Choose: ')

    if choose.upper() == "CREATE":
        A.Create()
    elif choose.upper() == "LOGIN":
        A.Login()
        
def prYellow(skk): print("\033[93m {}\033[00m" .format(skk))
def prRed(skk): print("\033[91m {}\033[00m" .format(skk))
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))

class Account:
    def __init__(self):
        self.user = None
        self.password = None
        self.content = None
        
    def Create(self):
        user=input('User: ')
        while ('%U'+user in open('Account.txt','r').read()) or (user==""):
            prRed("User Not Available")
            user=input('User: ')
        prGreen('User Available')
        password = input('Password: ')
        while password == "":
            prRed('Not Available Password')
            password = input('Password: ')
        file = open('Account.txt','a')
        acc = "%U"+user+"%P"+password+"/n"
        hash_acc = hash(acc)
        file.write(hash_acc)
        file.close()
        os.system(f"mkdir C:\diary\{HashPath(user)}")
        prGreen('Create Successful')
        self.Login()
    
    def Login(self):
        prYellow('Please Login Your Account')
        user=input('User: ')
        while ('%U'+user not in UnHash(open('Account.txt','r').read())) or (user==""):
            prRed("User Not Exist")
            user=input('User: ')
        password = input('Password: ')
        while ("%U"+user+"%P"+password not in UnHash(open('Account.txt','r').read())) or (password==""):
            prRed("Wrong Password")
            password=input('Password: ')
        self.user = user
        self.password = password
        prGreen("Login Successful")
        D=Diary(self.user)       
        D.Run()
        
class Diary:
    def __init__(self,user):
        self.user = user
        
    def Run(self):
        prYellow('Read/Write')
        choose = input('Choose: ')
        if choose.upper() =="READ":
            self.Read()
        elif choose.upper() =="WRITE":
            self.Write()
            
    def Read(self):

            path = "c:\\diary\\"+HashPath(self.user)
            # cmd = "cd C:\\ && cd diary\\" + self.user + "&& dir /TC"
            ListDiary = os.listdir(path)
            for i in range(len(ListDiary)):
                print('(',i,')',ListDiary[i])
            if len(ListDiary) == 0:
                prRed('No Story...')
            else:
                choose = int(input('Choose Number: '))
                path = path + "\\" + ListDiary[choose]
                self.OpenFile(path)
            
    def OpenFile(self,path):
        file = open(path,'r')
        for data in file.readlines():
            prYellow(UnHash(data))
        file.close()
        
    def Write(self):
            title = input('TITLE: ')
            prYellow(title)
            rows = ''
            All = []
            while rows != "finish":
                rows = input()
                All.append(rows)
            prYellow('ALL CONTENT: ')
            for data in All:
                print(data,'\n')
            self.Save(All)
            
    def Save(self,content):
        prYellow('DO YOU WANT TO SAVE...')
        choose = input('Choose: ')
        if choose.upper() == 'SAVE':
            name = str(date.today())
            path = "c:\\diary\\"+HashPath(self.user)+"\\"+name+".txt"
            file = open(path,'a')
            for row in content:
                file.writelines(hash(row)+"\n")
            file.close()
            prGreen("Saved")
        else:
            prRed('It not saved')
        
def Manager_Account():
    pass

Menu()