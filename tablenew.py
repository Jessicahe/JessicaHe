for i in range (1,10):
	print("\n") 
	for j in range (1,10):
			print("%d*%d=%d"%(i,j,i*j))
    
value='一二三四五六七八九十'

def trans(k):
    temp = ''
    if k == 10:
        temp = value[9]
    elif k>=10:
        temp = value[k//10-1]+value[9]+value[k%10-1]
    else:
        temp = value[k-1]
    return temp
for x in range (1,10):
    for y in range (1,10):
        print (value[x-1],'乘以',value[y-1],'等於',trans(x*y))