while True:
	passwordFile = open('SecretPasswordFile.txt')
	secretPassword = passwordFile.read()
	print('Enter you password')

	while True:

		typePassword = input()
		if typePassword == secretPassword:
			print('Acess granted')
		if typePassword == '12345':
			print('That password is one that an idiot puts on their luggage.')
			break
		else:
			print('Acess denied')

		
		print('Volta para o ínicio do programa')