excercise = []
for i in range (1,8):
    day = int(input("how many minutes  did you excercise today? : "))
    excercise.append(day)
    if day < 30:
        print("You excercised less than 30 minutes today")
    else:
        print("You excercised enough today")

total = sum(excercise)

average = total/len(excercise)
print("This week your average is " + str(average) + " minutes per day")
print("You excercised a total of " + str(total) + " minutes")
if total < 210:
    print("You excercised less than 210 minutes this week, good luck next week")
else:
    print("You have excercised enough good job!")