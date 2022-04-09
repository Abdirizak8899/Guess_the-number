#copyright of this code have Abdirizak abdullahi hussein 
# Guess the number 

guess = ''

secret = '13'

while guess != secret:
	guess = input('Guess the number 1-20: ')
	if guess == secret:
		break
	else:
		print()
		print('Nope ! ')
		continue