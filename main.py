import random
import json
print("Random password generator")
new_password = ""

while True:
    length = (input("Please pick a length "))
    try:
        val = int(length)
        break
    except ValueError:
        print("This isn't a number")

while val > 0:
    new_password = new_password + random.choice("abcdefghijklmnopqrstuvwxyz123456789")
    val -= 1
print("Your new password is: " + new_password)
with open('data.txt', 'w') as outfile:
    json.dump("New password: " + new_password, outfile)