'''

Task: Extract Email Addresses from a Text

Write a Python script using the re module to find all email addresses in the given text.

Example Input:

python

text = """
Hello John, your email is john.doe@example.com.
You can also reach Alice at alice123@work.net.
Bob's email is bob_smith@gmail.co.uk, but he's rarely online.
"""

'''

text = """
Hello John, your email is john.doe@example.com.
You can also reach Alice at alice123@work.net.
Bob's email is bob_smith@gmail.co.uk, but he's rarely online.
"""

import re

result = re.findall("\w*[@]\w*",text)
print(result)

