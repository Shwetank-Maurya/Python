accepted = False

while not accepted:
    password = input("Enter the password: ").strip()

    count_upper = 0
    count_lower = 0
    count_number = 0
    count_special = 0

    if len(password) >= 8:
        for i in password:
            if i.isupper():
                count_upper += 1
            elif i.islower():
                count_lower += 1
            elif i.isdigit():
                count_number += 1
            else:
                count_special += 1

        if count_upper >= 1 and count_lower >= 1 and count_number >= 1 and count_special >= 1:
            print("The password is Okay.")
            accepted = True
        else:
            print("The password is not Okay. Please include at least:")
            if count_upper < 1:
                print("- One uppercase letter")
            if count_lower < 1:
                print("- One lowercase letter")
            if count_number < 1:
                print("- One digit")
            if count_special < 1:
                print("- One special character")
    else:
        print("The password must be at least 8 characters long.")
