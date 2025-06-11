import re

pattern = re.compile(r"""
    \b[A-Za-z]+   # Match a word (letters only)
    \s+           # Followed by whitespace
    \d{2,4}       # Then a number (2 to 4 digits)
""", re.VERBOSE)

text = "John 1995 Alice 2023 Bob 87"
matches = pattern.findall(text)

print(matches)  