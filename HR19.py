import re

if __name__ == '__main__':
    s = input()

    hasAlphanumeric = any(char.isalnum() for char in s)
    print(hasAlphanumeric)
    hasAlphabetical = any(char.isalpha() for char in s)
    print(hasAlphabetical)
    hasDigit = any(char.isdigit() for char in s)
    print(hasDigit)
    hasLowercase = any(char.islower() for char in s)
    print(hasLowercase)
    hasUppercase = any(char.isupper() for char in s)
    print(hasUppercase)
