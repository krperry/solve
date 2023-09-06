def primeFact (i, f):
    if i < f:
        return []
    if i % f == 0:
        return [f] + primeFact (i / f, 2)
    return primeFact (i, f + 1)

def sqrt(nl):
    v={}
    for n in nl:
        if n in v.keys():
            v[n]+=1
        else:
            v[n]=1  
    f=r=1
    for  n in v.keys():
        f*=int(n)**int(v[n]/2)
    r*=int(n)**int(v[n]%2)
    return f,r
      
num=int(input("Enter number: ")) 
left, under=sqrt(primeFact(num,2))
if under == 1:
    print (left)
else:
    print ("{} times square root of  {}".format(left,under))
