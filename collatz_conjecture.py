#n = 4

def collatz_conjecture():
    n = int(input("Enter integer to check collatz conjecture: "))
    
    if n <= 0:
        print("Not valid!")
    while n > 1:
        if n % 2 ==0:
            print("EVEN", n)
            n = n / 2
        else:
            print("ODD", n)
            n = n * 3
            n += 1
    print("DONE")
    print(n)
    
    
collatz_conjecture()