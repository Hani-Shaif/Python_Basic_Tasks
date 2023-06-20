#=====================================
#=======Python_Basic_examples=========
#========== Python  If Loop ==========
#=====================================

print(" 1. Print numbers from 0 to 10 using while")
x = 0
while x < 11:
    print(x)
    x += 1
print("----------------------------------------")
print(" 2. Print numbers from 0 to 1o using for")
for x in range(0,11):
    print(x)
print("----------------------------------------")
print(" 3. Stop the loop if the number = 5")
for x in range(0,11):
    print(x)
    if x == 5: break
print("----------------------------------------")
print(" 4. Skip the 5 iteration from print")
for x in range(0,11):
    if x == 5:
        continue
    print(x)
print("----------------------------------------")
print(" 5. Print multiplication table from 1 to 5")
for x in range(1,6):
    for y in range(1,6):
        print(f"{x} X {y} = {x*y}")
    print("------------")
print("----------------------------------------")
print(" 6. How to get numbers from 10 to 20 using range")
for x in range(10,21):
    print(x)
print("----------------------------------------")
print(" 7. How to get numbers from 10 to 100 with 3 at each step using range")
for x in range(10,100,3):
    print(x)
print("----------------------------------------")
print(" 8. Get a list of even numbers from 1 to 100 using for")
numbers= [0,1,2,3,4,5,6,7,8,9] # .....to 100
for x in numbers :
    print(x)
    x += 1
print("----------------------------------------")
print(" 9. Get a list of even numbers from 1 to 100 using while")
x = 0
while x <= 100:
    print(x)
    x += 2
print("----------------------------------------")
print(" 10. Get a list of even numbers from 1 to 100 using range")
for x in range(0,100,2):
    print(x)



































