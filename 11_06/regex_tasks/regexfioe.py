import re

text = "The rain in ain Spain falls ainy  mainly in the plain."

matches = re.findall(r"\bain\w*", text)  # Matches words starting with "ain"

print(matches)  # Output: []
