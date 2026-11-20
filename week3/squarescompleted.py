while True:
    try:
        n = int(input("enter any positive number"))
                
        if n <=0:
            print(" Enter a positive number ")
        else:
            break

    except ValueError:
            print(" Please enter any positive number")
            

i = 0
while i <= n:
    if i % 2 == 0:
        
        print(i**2)
    i = i + 1




