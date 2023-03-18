print("Welcome to the world of Quiz!\nTest yourself!")
choice=input("Do you want to play? ")
score=0
if choice.lower()!="yes":     
    quit()
print("Okay!Let us play the game ")  
answer=input("What is capital of India? ") 
if answer.lower()=="delhi":                  #1
    print("Correct!:)")
    score+=1
else:
    print("Incorrect!:(")
answer=input("What does IPL stands for? ") 
if answer.lower()=="indian premirier league":  #2
    print("Correct!:)")
    score+=1
else:
    print("Incorrect!:(")
answer=input("What is capital of America? ") 
if answer.lower()=="washington dc":             #3
    print("Correct!:)")
    score+=1
else:
    print("Incorrect!:(") 
print("You have guessed " + str(score) +" correctly") 
print("You percentage " + str((score/3)*100) +"%.")    


