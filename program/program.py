def say_hi(name):
	if name=='':
		print("you dind't enter your name!")
	else:
		print("hi there...")
		for letter in name:	
			print(letter)
name=input("your name: ")
say_hi(name)
