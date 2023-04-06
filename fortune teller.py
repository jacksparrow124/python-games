import random
#comment
fortune = []
fortune.append ('you will die soon')
fortune.append ('you will win the mega millions jackpot')
fortune.append ('you will get accused of murder')
fortune.append ('you will gain a lover')
fortune.append ('you will spend time in jail')
fortune.append ('you will win a trip to hawaii')
fortune.append ('you will be hospitalized')
fortune.append ('you will win a lexus')
fortune.append ('you will be dumped')
fortune.append ('you will fall when you leave my tent')

print ('hi. my name is madame beatrice. why are you here?')
answer = input()
print ('oh.')
print ('would you like me to read your fortune?')
answer = input ('yes or no? ')
print (random.choice(fortune))