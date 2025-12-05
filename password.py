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
        if len(password) < 8:
            print("Error: not enough letters in password.")
        if not any(num.isdigit() for num in password):
            print("Error: no numbers in password.")
        if not any(let.isupper() for let in password):
             print("Error: no uppercase letters in password.")
        else:
            info.append(password)
            print("Succesfully created new account.")
            print(info)
            break
ha()