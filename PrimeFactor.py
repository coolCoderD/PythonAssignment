def primeFactorization(n):
    if(n<2):
        return "Prime factorization is defined only for integers greater than 1."
    factors=[]
    cnt=0
    while n%2==0:
        n//=2
        cnt+=1
        
    if cnt>0:
        factors.append((2,cnt))
    
    factor=3
    
    while factor*factor<=n:
        cnt=0
        while n%factor==0:
            n//=factor
            cnt+=1
            
        if cnt>0:
            factors.append((factor,cnt))
        factor+=2
    
    if n>1:
        factors.append((n,1))
    return factors
    
    
try:
    n=int(input("Enter a number: "))
    print(primeFactorization(n))

except ValueError:
    print("Please enter a valid integer.")