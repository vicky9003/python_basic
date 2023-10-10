txt="hii\"tushar\""
print(txt)

a="hello\n world"
print(a)

a="Hello\t world"
print(a)

#capitalize
a="hello,and welcome to my world"
x=a.capitalize()
print(x)

#isalnum()
a="Tushar9003"
x=a.isalnum()
print(x)

#isalpha()
a="tushar"
x=a.isalpha()
print(x)

#isdigit()
a="9003"
x=a.isdigit()
print(x)

#islower()
a="Tushar"
x=a.islower()
print(x)

#isupper()
a="TUSHar"
x=a.isupper()
print(x)

#join()
a=["Tushar","Upamanyu","Juhi","Radhika"]
x="#".join(a)
print(x)

#swapcase()
a="TUSHar"
x=a.swapcase()
print(x)

#translate()
a={65: 66}
x="Tushar"
print(x.translate(a))
