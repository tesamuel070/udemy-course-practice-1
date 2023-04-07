# while loop
i = 0
while i < 5:
    print(i)
    i += 1

i = 5
while True:  # this is the while it meant if it is true then the loop is not end
    print(i)
    break  # break means stop the loop
    if i < 5:
        print(i)
    elif i > 5:
        break
        print("their is something")

# example 2 about the loop
min_length = 2
name = input("pleace enter your name: ")

while not (len(name) >= min_length and name.isprintable() and name.isalpha()):
    name = input("pleace enter your name: ")

print("hello,{0}".format(name))

"""the above and the previous example are the same
     """
# example 3 about the loop
min_length = 2
while True:
    name = input("please enter your name: ")
    if len(name) >= min_length and name.isprintable() and name.isalpha():
        break
print("hello,{0}".format(name))

#example 4 about the loop







#example5
l = [1, 2, 3]
val = 10

found = True
idx= 0
while idx< len(l):
    if l[idx] == val:
        found = True
        break
    idx +=1

if not found:
    l.append(val)

print(l)

#practice 1
i= 0
while i<= 5:
    print(i)
    i += 1
