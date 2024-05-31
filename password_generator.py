import secrets
import string
import random

def gen_pass(k,d,p): #generating a password based on requirement
    password=""
    for i in range(d):
        password=password+secrets.choice(string.digits)
    for i in range(p):
        password=password+secrets.choice(string.punctuation) 
    for i in range(1):
        password=password+secrets.choice(string.ascii_uppercase) #we need to keep atleast one uppercase letter to make password valid
    for i in range(k-p-d-1):
        password=password+secrets.choice(string.ascii_letters)
    return password

def randomize(password): #to randomise the password generated
    pass_list=list(password)
    random.shuffle(pass_list)
    return "".join(pass_list)

print("Welcome to PASSWORD GENERATOR:")
print("-----------")
print("Here we provide the most secured passwords based on your choice which satisfy the conditions of any website: ")
print("Enter the length of the password you require: ")
n=int(input())
print("Enter number of digits and punctuation marks you require: ")
li=list(map(int,input().split()))
d=li[0]
p=li[1]
res=gen_pass(n,d,p)
print("The password as per your requirement is \033[1m{}\033[0m".format(randomize(res)))