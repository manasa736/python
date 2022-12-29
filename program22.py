inpl=['anjali','divya','manasa','gani']
def rev_str(a):
    return a[::-1]
outl=list(map(rev_str,inpl))
print(inpl)
print(outl)

print('-'*50)
inpl=['anjali','divya','manasa','gani']
outl=list(map(lambda x:x[::-1],inpl))
print(inpl)
print(outl)
