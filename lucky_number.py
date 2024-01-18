n = int(input("Enter the number: "))


#print(l)

def lucky_number():
    l=[]
    number =str(n)
    for i in number:
        l.append(i)
    print(l)  

    if '7' in l:
        print("True")
    else:
        print("False")

lucky_number()