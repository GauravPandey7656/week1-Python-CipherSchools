#1. ##conditional statements :-
a = True 
if a : 
    print("the value is true.")
print("end") ## this is not under the if condition 
      ## 1 indent = 2 spaces , 4 space, 8 spaces

a = False 
if a :
    print("the value is true.")
else:
    print("the value is false.")

a = 5 
if a==3:
    print("the value is 3 .")
elif a ==5:
    print("the value is 5 .")
else:
    print("the value is neither 3 nor 5.")

     ## nested if-else
# when the conditions are mutually exclusive.
# use :- if and elif only
# # when we can't rep all the things :- or when the conditions have something in common :- 
# use else also 

## questions :- 
a = int(input("Enter the length of side AB.\n"))
print(a)
b = int(input("Enter the length of side BC.\n"))
print(b)
c = int(input("Enter the length of side CD.\n"))
print(c)
d = int(input("Enter the length of side AD.\n"))
print(d)
if a==b==c==d :
    print("ABCD is a square.")
elif a==c and b==d :
    print("ABCD is a .")
else :
    print ("ABCD is a parallelogram.")

a = int(input("Enter a no.\n"))
b= int(input("Enter another no.\n"))
if a >b:
    print("a is greater than b.")
elif b<a:
    print("b is greater than a.")
else:
    print("None of the above Condition is true.")