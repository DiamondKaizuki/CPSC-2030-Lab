import time

print("Hello there, before you continue here's a quick question")
print("Are you a human being?")
while True:
	userinput = input("\nType Y for yes\nType N for no\nPlease Respond: ")
	I1 = userinput.lower()
if I1 == "y":
	print("\nWelcome User")
        break
elif I1 == "n":
        print("\nPlease Bring A Human Being To The Machine")
else:
        print("\nPlease Enter Either Y or N")
