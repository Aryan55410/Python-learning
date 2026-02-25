#prob-1
'''n =int(input("enter the number: "))
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")'''
#prob-2
'''l = ["Aryan",  "Patel"]

for name in l:
    if(name.startswith("A")):
        print(f"hello{name}")'''
#prob-3
'''n = int(input("enter the number: "))

i = 1
while i <= 10:
    print(f"{n} x {i} = {n * i}")
    i += 1'''

#prob-4

'''n = int(input("enter the number: "))
for i in range(2 , n):
    if(n%i) == 0:
        print("number is not prime")
        break
    else:
        print("number is prime")'''

#prob-5


'''n = int(input("enter the number: "))
i = 1
sum=0
while(i<=n):
    sum +=i
    i+=1
print(sum)''' 
   
#prob-6
n = int(input("enter the number: "))
for i in range(1, n+1):
    print(" "* (n-i), end="")
    print("*"* (2*i-1), end="")
    print(" ")