# letter = '''Dear <|NAME|>,
# Greetings from ABC coding house. I am happy to tell you about your selection
# You are selected!
# Have a great day ahead!
# Thanks and regards,
# Bill
# Date: <|DATE|>
# '''
# name = input("Enter Your Name\n")
# date = input("Enter Date\n")
# letter = letter.replace("<|NAME|>", name)
# letter = letter.replace("<|DATE|>", date)
# print(letter)

letter = '''Dear <|NAME|>,
You are selected for this job
Have a great day ahead
Bill
Date: <|DATE|>'''
name=input("Enter your name\n")
date=input("Enter Todays date\n")
letter=letter.replace("<|NAME|>",name)
letter=letter.replace("<|DATE|>",date)
print(letter)