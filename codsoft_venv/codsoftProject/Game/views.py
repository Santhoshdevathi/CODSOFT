from django.shortcuts import render
import random

# Create your views here.
youScored = [0]
computerScored = [0]

def getYourScore():
    return youScored[0]

def getComputerScore():
    return computerScored[0]

def incYourScore():
    youScored[0]+=1
    return youScored[0]

def incCompScore():
    computerScored[0]+=1
    return computerScored[0]

def randomChoice():
    choices = ['Rock','Paper','Scissors']
    return random.choice(choices)

def GameHome(request):
    yourScore = getYourScore()
    computerScore=getComputerScore()
    if request.method == 'POST':
        yourChoice = request.POST['choice']
        computerChoice = randomChoice()
        if yourChoice == computerChoice:
            return render(request,'Game/nextRound.html',{'tie':True,'won':False,'lost':False,'yourScore':yourScore,'computerScore':computerScore,'yourChoice':yourChoice,'computerChoice':computerChoice})
        elif ((yourChoice=='Rock' and computerChoice=='Scissors') or (yourChoice=='Scissors' and computerChoice=='Paper') or (yourChoice=='Paper' and computerChoice=='Rock')):
            yourScore=incYourScore()
            return render(request,'Game/nextRound.html',{'tie':False,'won':True,'lost':False,'yourScore':yourScore,'computerScore':computerScore,'yourChoice':yourChoice,'computerChoice':computerChoice})
        else:
            computerScore=incCompScore()  
            return render(request,'Game/nextRound.html',{'tie':False,'won':False,'lost':True,'yourScore':yourScore,'computerScore':computerScore,'yourChoice':yourChoice,'computerChoice':computerChoice})  
    return render(request,'Game/GameHome.html',{'yourScore':yourScore,'computerScore':computerScore})

def quitGame(request):
    youScored[0]=0
    computerScored[0]=0
    return render(request,'Calculator/home.html')

def newGame(request):
    youScored[0]=0
    computerScored[0]=0
    return GameHome(request)