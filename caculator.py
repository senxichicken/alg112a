import math 

f1 = lambda x : (3+ 5**0.5)/2 
f2 = lambda x : (x*x +1)/3
f3 = lambda x : 3-(1/x)

x1 = x2 = x3 = 1

for i in range(20):
    x1, x2, x3 = f1(x1), f2(x2), f3(x3)
    print('x1:', x1, 'x2', x2, 'x3', x3)



![](https://hackmd.io/_uploads/HyDoqzZgp.png)
