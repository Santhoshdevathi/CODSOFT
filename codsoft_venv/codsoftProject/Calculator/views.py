from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'Calculator/home.html')


def Calculations(request):
    res=''
    if request.method == 'POST':
        num1 = int(request.POST['first_num'])
        num2 = int(request.POST['second_num'])
        activity = request.POST['operation']
        if activity == 'add':
            res = num1+num2
            operation = '+'
        elif activity == 'subtract':
            res = num1-num2
            operation = '-'
        elif activity == 'multiply':
            res = num1*num2
            operation = '*' 
        elif activity == 'divide':
            res = num1//num2
            operation = '//'
        elif activity == 'modulo':
            res = num1%num2 
            operation = '%'  
        print(res)     
        return render(request,'Calculator/CalculatorHome.html',{'result':res,'num1':num1,'num2':num2,'operation':operation})    
    return render(request,'Calculator/CalculatorHome.html',{'result':res})                       