#Ask for an int
#check if int is a positive numer
#if positive number and higher than before name num_int = max_int and ask for a new int
#ask for in until input is negative, then print maximum int

max_int = 0

num_int = int(input("Input a number: "))

while num_int > 0:
    if num_int > max_int:
        max_int = num_int
    if max_int > 0:
        num_int = int(input("Input a number: "))
else:
    print("The maximum is", max_int)  
    