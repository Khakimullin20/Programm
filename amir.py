"""
a = int(input())
b = int(input())
n = int(input())
def func():
    z = [a,b,n]
    maximum= z[0]
    for i in range(1,len(z)):
        if z[i] > maximum:
           maximum = z[i]
    print(maximum)
func()
"""
a = [1,2,3,4,5,6,7,8,9,0,9,8,7,7]
def func2(a):
    z=0
    for i in a:
        z +=i
    print(z)




func2(a)








        

