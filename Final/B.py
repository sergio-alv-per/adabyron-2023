N = int(input())

for _ in range(N):
    x,y,z = [int(a) for a in input().split(" ")]
    
    A = (y-x+z)//2
    B = z-A
    C = x-B

    print(" ".join([str(x) for x in sorted([A,B,C])]))