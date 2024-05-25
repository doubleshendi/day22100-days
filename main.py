#import random

#mynumber = random.randint(1,100)
#print(mynumber)

#counter = 0 
#print("Number Guessing Game")
#print()
#print("Enter a number between 1 and 1,000")
#print()
#userinput = 0


#answer = random.randint(1,000)

#while (userinput != answer) :
# userinput = input("What is your guess? ")
 #counter = counter +1

 #if int(userinput) == answer :
   #print("correct !!")
   #print("It took you", counter, "guesses to get it correct!") 
   #break
# elif int(userinput) < answer :
  # print("too low")
 #elif int(userinput) > answer :
  # print("too high")
 #if int(userinput) <  0 :
  # print("You have entered a negitive number")
   #break



import random

# mynumber = random.randint(1,100)
# print(mynumber)
counter = 0 
print("Number Guessing Game")
print()
print("Enter a number between 1 and 1,000")
print()
userinput = 0
answer = random.randint(1, 1000)
while userinput != answer:
    userinput = input("What is your guess? ")
    counter += 1
    if int(userinput) == answer:
        print("correct !!")
        print(f"It took you {counter} guesses to get it correct!")
        break
    elif int(userinput) < answer:
        print("too low")
    elif int(userinput) > answer:
        print("too high")
    if int(userinput) < 0:
        print("You have entered a negative number")
        break

print("Press the run button to try again with a different number")



