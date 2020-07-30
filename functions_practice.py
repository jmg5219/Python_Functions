def add(arg1,arg2):# function to add two arguments
    sum = arg1 + arg2
    return sum
def minus(arg1, arg2):#function to subtract two arguments
    difference = arg1 -arg2 
    return difference
def convert_case(arg):#function to generate upper case letters
    try:
        uppercase = arg.upper()
        return uppercase
    except:
        return print("PLease enter a string")


result = add(2,2)#calling the add function and passing arguments
difference = minus(4,1)#calling the minus function and passing arguments
print(result)#printing the results from the functions
print(difference)

title = "Great Gatsby"
print(convert_case(title))

