import random
import array
# setting staple values
min = 1
max = 10
Check_input = ["y", "n", "yes", "no"]
myRoll=[]
myResults=[]

# asking user for information
dice_number = int(raw_input("Number of dice to Roll? Minimum 1:"))
if dice_number <= 0:
    exit()
target_number = int(raw_input("Target number for action? Range is 2 to 10, default 6:"))
if target_number > 10 or target_number < 0:
    exit()
specialization = str(raw_input("Does skill and action count as character specialty? 'y' or 'n':"))
specialization.lower()
if any(x in Check_input for x in specialization):
    specialization = "y"
    print "input accepted"
else:
    exit()

for die in range(0, int(dice_number)):
    tempRoll = random.randint(min, max)
    myRoll.append(tempRoll)
    print tempRoll
    # if this is a speciality for the character, roll another dice if roll is a 10 (crit)
    if specialization is "y" and tempRoll is 10:
        print "CRIT!!!! Rolling another dice, ignoring botch"
        tempRoll = random.randint(min, max)
        print "CRIT roll was", tempRoll
        if tempRoll > 1:
            myRoll.append(tempRoll)
        else:
            print "throwing away the botch as this was a crit re-roll"

print myRoll

#check the Value of the results agains the target number for this challenge
#turn this into a function and call it here
for xRoll in myRoll:
    if xRoll >= target_number:
        myResults.append(1)
    if xRoll < target_number:
        myResults.append(0)
    if xRoll == 1:
        myResults.append(-1)

#give the overall result from the data.
dice_succeded = 0
for a in myResults:
    dice_succeded = dice_succeded + a

#qualify the dice roll here
if dice_succeded > 0:
    print "SUCCESS!", dice_succeded
if dice_succeded == 0:
    print "FAILED", dice_succeded
if dice_succeded < 0:
    print "BOTCH! Outch, please look to the GM to understand the scope of your character's failure. May the Force be with you...", dice_succeded