from gmssl import sm3,func
from time import time
import random

res=[]
a=random.randint(0,2**16)

start=time()
for i in range(0,2**8):
    m=bytes(str(a), encoding='utf-8')
    h=sm3.sm3_hash(func.bytes_to_list(m))
    res.append(h)
    a=a*2+1
    if h in res:
        print(h)
        break
print("Time:",time()-start)
