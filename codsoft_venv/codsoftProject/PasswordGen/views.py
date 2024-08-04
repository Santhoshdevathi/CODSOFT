from django.shortcuts import render
import random

# Create your views here.

def GeneratePassword(length):
    letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
               'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',]
    
    symbols = ['!','#','$','%','&','(',')','*','+','_','-','@']

    numbers = ['0','1','2','3','4','5','6','7','8','9']

    password = ''

    if length<=11:
        for i in range(length-4):
            password += random.choice(letters)
        for i in range(2):
            password += random.choice(symbols)
        for i in range(2):
            password += random.choice(numbers)

    else:
        for i in range(length-5):
            password += random.choice(letters)
        for i in range(2):
            password += random.choice(symbols)
        for i in range(3):
            password += random.choice(numbers)
    return str(password)

def passwordGenHome(request):
    if request.method == 'POST':
        length = int(request.POST['length'])
        if length<8 or length>15:
            return render(request,'PasswordGen/PasswordGenHome.html',{'warn':True,'password':None})
        else:
            password = GeneratePassword(length)
            return render(request,'PasswordGen/PasswordGenHome.html',{'warn':False,'password':password})
    return render(request,'PasswordGen/PasswordGenHome.html',{'warn':False,'password':None})