def lower_triangle(n):
    for i in range(1,n+1):
        for j in range(0,i):
            print("*",end="")
        print()

def upper_triangle(n):
    for i in range(n,0,-1):
        for j in range(i,0,-1):
            print("*",end="")
        print()

def Pyramid(n):
    for i in range(0,n):
        for k in range(n-1,i,-1):
            print(" ",end="")
        for j in range(0,2*i+1):
            print("*",end="")
        print()
            
n = int(input("Please enter the number of rows:"))

print("Lower Triangular:")
lower_triangle(n)
print("Upper Triangular:")
upper_triangle(n)
print("Pyramid:")
Pyramid(n)
