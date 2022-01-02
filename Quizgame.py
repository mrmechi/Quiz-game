print("Welcome to my computer QUIZ!")
playing=input('Do you want to play? ')
if playing.lower() !='yes':
    quit()
print('Great, Lets Play!')
score=0


ques1= input('What is capital of India? ')
ans1 = "delhi"
def Quiz(ques1, ans1):
    if ques1.lower()==ans1.lower():
        return True
    else:
        return False
if Quiz(ques1, ans1)==True:
    print('You are correct!')
    score += 1
else:
    print('You are incorrect!')


ques2= input('What is capital of Madhya Pradesh? ')
ans2 = "bhopal"

def Quiz(ques2, ans2):
    if ques2.lower()==ans2.lower():
        return True
    else:
        return False

if Quiz(ques2, ans2)==True:
    print('You are correct!')
    score+= 1
else:
    print('You are incorrect!')


ques3=input("Who is Prime Minister of India? ")
ans3="Narendra Modi"

def Quiz(ques3, ans3):
    if ques3.lower()==ans3.lower():
        return True
    else:
        return False

if Quiz(ques3, ans3)==True:
    print('You are correct!')
    score+= 1
else:
    print('You are incorrect!')

ques4=input("India got Independence in which year? ")
ans4='1947'

def Quiz(ques4, ans4):
    if ques4.lower()==ans4.lower():
        return True
    else:
        return False

if Quiz(ques4, ans4)== True:
    print("That's right!")
    score+= 1
else:
    print("That's not correct")



ques5 = input("Do India is the most populated country? ")

if ques5.lower()=='no':
    print("That's right!")
    score += 1
else:
    print("That's not correct")

print('You got ' + str(score)+ ' marks')
print('You got ' + str((score/5) * 100)+ ' percentage ')

if score>=3:
    print('Congratulations! You passed the exam')
else:
    print('You failed!')












