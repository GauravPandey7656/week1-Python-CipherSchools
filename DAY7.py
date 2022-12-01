##LOOPS :
# 1. while loop 
 ## use while in the places where we are not sure ,how many times we have to write it 
i =1
while i <=10:
    print (i)
    i +=1
## i = 1
#3while i >1:
  #  print(i)
  # will print  1. till infinity
   # if we wrote += ,line , then will write the no. till infinity.


## will print the elements seperately .
a = 'hello'
for x in a:
    print(x) 
print(type(x))
print(type(a))


b = ["apple","banana","mango"]
for x in b :
    print(x)
print(type(b))
print(type(x))

c = (12 , 45 , "hello world")
for x in c :
    print(x)
print(type(c))
print(type(x))

##e = 4567890321
#for x in e:
 #   print(x) ## shows int is iterable ## error 
 ## we can't iterate on int , float and complex no.

 ## break in for 
for i in  range (10):

        print(i)
        if i ==3:
            break 
        print(i) 
else :
        print("hi") ## after break it won't get executed


  ## for int we can use range here , as range will give the no. within it 
for i in range(10):
    print(i) ## will give from  0 to 9 
a = range (10)
print(a) ## range(0,10) is the output

## break , continue , pass

for i  in range(5):
    print(i)
    if i==3:
        break ## won't print anything after 3
for i in range(10):
    print(i)
    if i == 4:
        continue ## CONTINUES the other one
    for i in range(5):
        print(i)
        if i ==5 :
            continue
## del deletes it from the memory :-

for i in range(5):
    print(i)
    i=100 # will print upto 4 only 
    del i ## no change 
   ##  print(i) , won't work as we already deleted i 
for i in range (5):
    print(i)
    i = 100
    print(i) ## will give 1 then 100 , and so on.

    ## pass
    ## it just creates a blank string