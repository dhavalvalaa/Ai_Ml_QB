'''
Task: Validate User Input Using Regex in Python
Write a Python program that validates user input for:

Email Addresses (must follow standard email format)

Phone Numbers (must be exactly 10 digits)

Passwords (must include uppercase, lowercase, numbers, and special characters)
'''
import re

def email_validation(email):
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(\.[a-zA-Z]{2,})?$"
    result = re.match(pattern, email)
    return result.group() if result else "Invalid email"

def phone_validation(phone):
    pattern = r"^\d{10}$" 
    result = re.match(pattern, phone)
    return phone if result else "Invalid phone number"

def password_validation(password):
    pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
    result = re.match(pattern, password)
    return "Valid password" if result else "Invalid password"


emails = [
    "aaa@gmail.com", "aaa@google.com", "aa.aa@gmail.com", "aaa@gmail.co.in",
    "invalid@domain", "@missingusername.com", "user@@doubleat.com"
]

print("\n**Email Validation**")
for email in emails:
    print(f"{email}: {email_validation(email)}")


print("\n**Phone Validation**")
phones = ["9876543210", "123456789", "98765432101", "abc1234567"]
for phone in phones:
    print(f"{phone}: {phone_validation(phone)}")


print("\n**Password Validation**")
passwords = ["Strong@123", "weakpassword", "NoSpecial123", "Weak@1"]
for password in passwords:
    print(f"{password}: {password_validation(password)}")
