tup=()
print(tup)
print('type of tuple',type(tup))
tup2=(45,)
print('single element tuple is',tup2)
tup3=tuple(range(10,20))
print(tup3)
l1=[20,30,40]
t1=tuple(l1)
print('tuple from lists',t1)
t3=tup2+t1
print(t3)
for i in t3:
    print(i)
    t3=(10,20,30,40,50,60,70,80,90,30,70,10,60,80)
print('tuple slicing',t3[2:4])
print('tuple from beginning',t3[:5])
print('count of a no',t3.count(20))
print('index of a no',t3.index(30))
print('max of tuple',max(t3))
print('min of tuple',min(t3))
print('length is',len(t3))
print('sum of tuple is',sum(t3))
t4=t3*2
print(' new tuple with repeated elements',t4)
print('check the presence of element',(40 in t3))
print('check the absence of element',(100 not in t3))
