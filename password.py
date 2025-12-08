def ha():
    info = []
    while True :
        email = input("Email: ")
        if ("@") not in email:
            print("Error: invalid email format.")
        else:
            print("Valid email.")
            info.append(email)
            break

    while True:
        password = input("Password: ")
        errors = 0
        if len(password) < 8:
            print("Error: not enough letters in password.")
            errors += 1
        if not any(num.isdigit() for num in password):
            print("Error: no numbers in password.")
            errors += 1
        if not any(let.isupper() for let in password):
             print("Error: no uppercase letters in password.")
             errors += 1
        if errors <= 0:
            info.append(password)
            print("Succesfully created new account.")
            print(info)
            break
ha()