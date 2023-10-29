n=int(input("Somar de 1 até "))
c=1
c2=1
while c<n:
    valid=c%2
    c+=1
    if valid ==0:
         print(c)
         c2+=c
print("soma=" , c2)