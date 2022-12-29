dict1={'sedan':1500, 'SUV':2000, 'pickup':2500, 'minivan':1600, 'van':2400, 'semi':13600,
       'Bicycle':7, 'motorcycle':110}
ans=[i.upper()for i in dict1 if dict1[i]<
     5000]
##for i in dict1:
##    if dict1[i]<5000:
##        ans.append(i.upper())
print(ans)
