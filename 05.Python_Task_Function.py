#=====================================
#=======Python_Basic_examples=========
#======== Python  Function ===========
#=====================================

print("---------------------------")
print(" 1.Create a simple function that takes 2 numbers and print their values")
x = 10
y = 20
def numbers():
    print(x,y)
numbers()
print("---------------------------")
print(" 2. Create a simple function that takes 2 numbers and return their values")
def numbers(num1,num2):
    print(num1,num2)
numbers(100,200)
print("---------------------------")
print("  3. In the above return function , use keyword arguments when calling the function")
def myFunc(name):
    print("Hello",name)
myFunc("Hani")
print("---------------------------")
print(" 4. In the above return function , give x and y default values of 0 and call the function with no arguments")
def numFun(x  = 0,y = 0):
    print()
print("---------------------------")
print(" 5. Create a function that can take any number of arguments and print the sum of them")
def sumFunc(x,y):
    sum = x + y
    print("The Sum :" ,sum)
sumFunc(10,30)
print("---------------------------")
print(" 6. Create the same sum function using the lambda")
sumFunc = lambda x , y : x + y
print("The Sum : ",sumFunc(10,30))
print("---------------------------")
print(" 7. Call the lambda function at the same definition line")
sumFunc = lambda x , y : x + y
print("The Sum : ",sumFunc(10,30))
print("---------------------------")
print(" 8. Write the difference between the local variable and global variable")

x = 10 # global variable
print(x) # x = 10

def func():
    #local variable
    x = 20
    print(x) # x = 20
func()
print(x) # x = 10


print("-----------------")
x = 10 
print(x) # x = 10

def func():
    global x # convert Local value to Global value
    x = 20
    print(x) # x = 20
func()
print(x) # x = 20
































