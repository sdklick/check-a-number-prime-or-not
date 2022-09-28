# write a program to check a number prime or not

userinput=int(input("please input a number : "))

isprime=True

# check the number greater then 1 or not

if userinput>1:
    for num in range(2,userinput):
        if userinput%num==0:
            isprime=False
            break
    if isprime:
     print(userinput,"is a prime number")
    else:
     print(userinput,"is not prime number")    


