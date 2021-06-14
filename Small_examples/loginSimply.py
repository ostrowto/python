#loginSimply

accounts_of_users = {}

while True:
    option = input("Type 'Sign in' or 'Log in: '")
    login = input("Login: ")
    password = input("Password: ")
    if option == "Sign in":
        accounts_of_users[login] = password
    elif option == "Log in":
        if accounts_of_users[login] == password:
            print("\nYou`re successfully logged in!")
            break
    else:
        print("Error, try again")
        continue
