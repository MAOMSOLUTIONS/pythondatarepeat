def diference(a):
    b=[]
    for i in range(len(a)-1):
        b.append(round(abs (a[i+1]-a[i]),2))
    print ("Diferencia ", b)
    return all(ele == b[0] for ele in b) 
print(diference([1,3,5,7]))
print(diference([194,54,23,7,3,6,8]))
print(diference([44,37,30,23]))
print(diference([-2.3,-1.1,0.1,1.3,2.5,3.7]))
print(diference([1,8]))
print(diference([3,2,1,2,3,4,3]))