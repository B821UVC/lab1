p1a=1
p1b=1

p2a = 2
p2b = 1
n=2
while ((p1a+p2a)/(p1b + p2b))-(p2a/p2b)>0.001 or ((p1a+p2a)/(p1b + p2b))-(p2a/p2b)<-0.001:
    n+=1
    swa = p1a
    swb = p1b
    p1a = p2a
    p1b = p2b
    p2a = swa+p2a
    p2b = swb + p2b
print((p1a+p2a)/(p1b + p2b)-(p2a/p2b))
print("член последовательности: ", n+1)