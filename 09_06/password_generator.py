import string
import random

sc = ["!","@","#","$","%","^","&"]
passw = ""
for i in range(random.randrange(8,10)):
    if random.randint(0,2) == 0:
        passw += random.choice(string.ascii_uppercase)
    else:
        passw += random.choice(string.ascii_lowercase)

for i in range(random.randrange(2,4)):
    passw += str(random.randint(0,9))

for i in range(random.randrange(2,4)):
    passw += random.choice(sc)
print(type(passw))


print(passw)