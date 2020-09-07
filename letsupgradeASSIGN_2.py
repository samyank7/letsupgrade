altitude=int(input("enter the current altitude : "))

if altitude<=1000:
    print(" SAFE to land")
elif altitude>1000 and altitude<=5000:
    print("bring it down to 1000ft")
else:
    print("turn around")