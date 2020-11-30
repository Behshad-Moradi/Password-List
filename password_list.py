from itertools import product
from os import getcwd

def createPasswordList(characters, answer):
	if (answer == 'y'):
		first = int(input("Enter your desired length: "))
		_file = open(getcwd() + "/pass.txt",'w')
		print("Password creation started with a length of " + str(first))
		for _pass in product(characters, repeat=first):
			#print(''.join(_pass))
			_file.write(''.join(_pass) + "\n")
		print("Password creation finished with a length of " + str(first))
			
	else:
		first = int(input("Enter your first length: "))
		second = int(input("Enter your second length: "))
		_file = open(getcwd() + "/pass.txt",'w')
		
		for length in range(first, second+1):
			print("Password creation started with a length of " + str(length))
			for _pass in product(characters, repeat=length):
				_file.write(''.join(_pass) + "\n")
			print("Password creation finished with a length of " + str(length))
	_file.close()
	
characters = input("Please enter your desired characters: ")

answer = input("Do you want to create password with specified length?(y/n) ")

createPasswordList(characters, answer)
