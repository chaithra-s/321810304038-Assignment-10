#python progran to print in place multiples of 3 as Fuzz and multiples of 5 as "Buzz" and multiples of both as "Fuzzbuzz"
for i in range(1,101):
	if i%3==0 and i%5==0:
		print("FizzBuzz")
	elif i%3==0:
		print("Fizz")
	elif i%5==0:
		print("Buzz")
	else:
		print(i)

#program to remove consecutive duplicates from list		
x=[1,2,2,3,3,3,4,4,4,5,5,5,6,6,6,8]
previous_value = None
new_lst = []

for elem in x:
   if elem != previous_value:
       new_lst.append(elem)
       previous_value = elem

print(new_lst)

#program to find unique element of list
list=[1,2,4,6,8,8,2,1]
uniqueitems=[]
dupitems=set()
for ele in list:
	if ele is not dupitems:
		uniqueitems.append(ele)
		dupitems.add(ele)
print(dupitems)

#to check number in given range
def  a(num,low,high):
    for i in range(low,high+1):
        if num==i:
            print('Number is within the range',)
            break
    else :
            print('Number is out of range')
a(4,5,10)
#5.Write a Python function that accepts a string and calculates the number of 

#upper case letters and lower case letters.

#Sample String : 'Hello Mr. Rogers, how are you this fine Tuesday?'

#Expected Output : 

#No. of Upper case characters : 4

#No. of Lower case Characters : 33

#HINT: Two string methods that might prove useful .isupper()
def p(s):
    d={"UPPER_CASE":0, "LOWER_CASE":0}
    for c in s:
        if c.isupper():
           d["UPPER_CASE"]+=1
        elif c.islower():
           d["LOWER_CASE"]+=1
        else:
           pass
    print ("Original String : ", s)
    print ("No. of Upper case characters : ", d["UPPER_CASE"])
    print ("No. of Lower case Characters : ", d["LOWER_CASE"])

p('MYASSIGNMEnt')
