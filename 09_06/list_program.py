# Program to print duplicates from a list of integers     

l = [10,201,30,10,20,30,10,10]

temp = []
for i in l:
    if i not in temp:
        temp.append(i)
    else:
        print(i)

#Python program to find Cumulative sum of a list          
l = [10,20,30,40,50]
result_list = []
sum = 0
for i in l:
    sum += i
    result_list.append(sum)

print(result_list)
print(sum)

