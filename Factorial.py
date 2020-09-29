n = int(input("Enter the number"))
output = 1
for i in range(n,0,-1):
    output = output*i
print("Factorial of", n , "is", output)