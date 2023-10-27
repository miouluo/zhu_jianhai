import pymprog as mp
lp=mp.begin('Sensitivity Analysis')
x1=mp.var('x1',kind=int)
x2=mp.var('x2',kind=int)
x3=mp.var('x3',kind=int)
x4=mp.var('x4',kind=int)
x5=mp.var('x5',kind=int)
a1=mp.var('a1',kind=int)
a2=mp.var('a2',kind=int)
a3=mp.var('a3',kind=int)
a4=mp.var('a4',kind=int)
b1=mp.var('b1',kind=int)
b2=mp.var('b2',kind=int)
b3=mp.var('b3',kind=int)
x1>=10
x1+x2>=8
x1+x2+x3>=9
x1+x2+x3+x4>=11
x2+x3+x4+x5+a1+b1>=13
x3+x4+x5+a2+b1+b2>=8
x4+x5+a3+b2+b3>=5
x5+a4+b3>=3

mp.minimize(25*8*(x1+x2+x3+x4+x5)+30*2*(a1+a2+a3+a4)+30*4*(b1+b2+b3))
mp.solve()
print("Optimal Solution:")
print("x1 =", x1.primal)
print("x2 =", x2.primal)
print("x3 =", x3.primal)
print("x4 =", x4.primal)
print("x5 =", x5.primal)
print("a1 =", a1.primal)
print("a2 =", a2.primal)
print("a3 =", a3.primal)
print("a4 =", a4.primal)
print("b1 =", b1.primal)
print("b2 =", b2.primal)
print("b3 =", b3.primal)
print("Objective Value =", mp.vobj())
mp.end()
