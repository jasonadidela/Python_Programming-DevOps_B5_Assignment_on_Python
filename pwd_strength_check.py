def password_strength_check(pwd):
    
    check_min_length = 8
    check_upcases = any(c.isupper() for c in pwd)
    check_lowcases = any(c.islower() for c in pwd)
    check_numbers = any(c.isdigit() for c in pwd)
    check_special_symbols = any(c in "!@#$%^&*()_-+" for c in pwd)
    
    if len(pwd) >= check_min_length and check_upcases and check_lowcases and check_numbers and check_special_symbols:
        return True
    else:
        return False

user_input = input("Enter a password: ")
if password_strength_check(user_input):
    print("Password meet the criteria and is strong!")
else:
    print("Password does not meet the criteria.")
