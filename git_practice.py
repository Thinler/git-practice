users=['admin','john','bob','sarah','alice']
for user in users:
    if user=='admin':
        print("hello Admin,would you like tp see a status report")
    else:
        print(f"hello,{user.title()},thank you for logging")
