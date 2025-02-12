import time

print("Hello there, before you continue here's a quick question")
print("Are you a human being?")

while True:
    userinput = input("\nType Y for yes\nType N for no\nPlease Respond: ")
    I1 = userinput.lower()
    
    if I1 == "y":
        time.sleep(1)
        print("\nWelcome User")
        break

    elif I1 == "n":
        time.sleep(1)
        print("\nPlease Bring A Human Being To The Machine")
        time.sleep(1)

    else:
        time.sleep(1)
        print("\nPlease Enter Either Y or N")
