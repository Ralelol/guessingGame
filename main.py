print ('[------------------------------]')
print ('[      Select the Imposter     ]')
print ('[  Select: a color Red    (1)  ]')
print ('[  Select: a color Blue   (2)  ]')
print ('[  Select: a color Pink   (3)  ]')
print ('[  Select: a color Green  (4)  ]')
print ('[  Select: a color Orange (5)  ]')
print ('[  Select: a color Yellow (6)  ]')
print ('[  Select: a color Cyan   (7)  ]')
print ('[  Select: a color Black  (8)  ]')
print ('[  Select: a color White  (9)  ]')
print ('[------------------------------]')
print("You have 5 tries to guess the impostor")

numberOfTries = 5
triesLeft = numberOfTries
rightAnswer = 8

for x in range(numberOfTries):
    triesLeft -= 1
    number = int(input('Enter your answer: '))

    if (number == rightAnswer):
        print ("Nice! You found the Imposter!")
    else:
        print ("Wrong answer, try again")
        print ("You have " + str(triesLeft) + " tries left")