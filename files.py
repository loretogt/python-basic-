#Wowsers!```
#We could read that file like this:
#**script.py**
#```py
#with open('real_cool_document.txt') as cool_doc:
#    cool_contents = cool_doc.read()
#print(cool_contents)
#This opens a file object called cool_doc and creates a new indented block where you can read the contents of the opened file. We then read the contents of the file cool_doc using cool_doc.read() and save the resulting string into the variable cool_contents. Then we print cool_contents, which outputs the statement Wowsers!.

#.readlines() function to read a text file line by line instead of having the whole thing
#Here we pass the argument 'w' to open() in order to indicate to open the file in write-mode. with open('generated_file.txt', 'w') as gen_file:
#we open it with 'a' for append-mode
# In Python we can convert that data into a dictionary using the csv library’s DictReader object.
#we call csv.DictReader we pass in the delimiter parameter, which is the string that’s used to delineate separate fields in the CSV.
#import json    json.load       json.dump: takes two arguments: first the data object, then the file object you want to save.

import csv
import json

compromised_users=[]

with open('passwords.csv') as password_file:
    password_csv = csv.DictReader(password_file)
    for password_row in password_csv:
    #print(password_row['Username'])
    compromised_users.append(password_row['Username'])


with open('compromised_users.txt', 'w') as compromised_user_file:
    for comp_user in compromised_users:
    compromised_user_file.write(comp_user)


with open('boss_message.json', 'w') as boss_message:
    boss_message_dict= {
    'recipient': 'The Boss',
    'message': 'Mission Success'
        }
            json.dump(boss_message_dict, boss_message)

with open('new_passwords.csv', 'w') as new_passwords_obj:
    slash_null_sig="""
        _  _     ___   __  ____
        / )( \   / __) /  \(_  _)
        ) \/ (  ( (_ \(  O ) )(
        \____/   \___/ \__/ (__)
        _  _   __    ___  __ _  ____  ____
        / )( \ / _\  / __)(  / )(  __)(    \
        ) __ (/    \( (__  )  (  ) _)  ) D (
        \_)(_/\_/\_/ \___)(__\_)(____)(____/
        ____  __     __   ____  _  _
        ___   / ___)(  )   / _\ / ___)/ )( \
        (___)  \___ \/ (_/\/    \\___ \) __ (
        (____/\____/\_/\_/(____/\_)(_/
        __ _  _  _  __    __
        (  ( \/ )( \(  )  (  )
        /    /) \/ (/ (_/\/ (_/\
        \_)__)\____/\____/\____/
        """
            new_passwords_obj.write(slash_null_sig)
