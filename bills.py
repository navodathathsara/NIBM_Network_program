sum=0

def cal():
    if sum>=2000:
        discount = sum*0.10
        x=sum-discount
        print("Discocunt : ",discount)
        print("Total Cost : ",x)
        return file1(x,discount)
        
    elif sum>=1500:
        discount = sum*0.07
        x=sum-discount
        print("Discocunt : ",discount)
        print("Total Cost : ",x)
        return file1(x,discount)

    elif sum>=1000:
        discount = sum*0.05
        x=sum-discount
        print("Discocunt : ",discount)
        print("Total Cost : ",x)
        return file1(x,discount)
        
    elif sum<1000:
        discount=0
        x=sum
        print("no discount")
        print("Total cost : ",x)
        return file1(x,discount)
        
    else:
        print("NOT valid")
        exit()

def file1(x,discount):
    f=open("price.txt",'a+')
    f.write(str(x))
    f.write("\n")
    f.write(str(discount))
    f.write("\n")
    f.close()

def file():
    f=open("price.txt",'a+')
    f.write(str(price))
    f.write("\n")
    f.close()

while True:
    try:
        price = int(input("price : "))
        sum=sum+price
        file()

    except:
        print("no value enterd")
        break

    
cal()
