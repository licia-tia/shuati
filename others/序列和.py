def duang(n, l):
    _res = []
    for i in range(l, min(n, 101)):
        if n%i == 0:
            if i%2==0:
                pass
            else:
                if n//i - (i-1)/2>=0:
                    for p in range(n//i - (i-1)//2, n//i + (i-1)//2):
                        print(p, end=" ")
                    print(n//i + (i-1)//2, end="")
                    return
        elif (2*n)%i == 0:
            if n//i - (i-1)//2>=0:
                    for p in range(n//i - (i-1)//2, n//i + (i-1)//2+1):
                        print(p, end=" ")
                    print(n//i + (i-1)//2+1, end="")
                    return
    print("No", end="")

raw_input = input()
n, l = raw_input.split(" ")
n, l = int(n), int(l)
duang(n, l)
