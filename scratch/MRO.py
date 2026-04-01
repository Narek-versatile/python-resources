class X: 
    pass 
 
class Y(X): 
    pass 
 
class Z(X): 
    pass 
 
class W(Y, Z): 
    pass 

#x = x obj
#y = y x obj
#z = z x obj
#w = w y z x obj



 
class Base: 
    pass 
 
class A: 
    pass 
 
class B: 
    pass 
 
class FinalClass(Base, A, B): 
    pass 
 
#Base = Base obj
#A = A obj
#B = B obj
#FinalClass = FinalClass Base A B obj





class A: 
    pass 
 
class B(A): 
    pass 
 
class C(A): 
    pass 
class D(B, C): 
    pass 
 
class E(C): 
    pass 
class F(D, E): 
    pass 
 
#A = A obj
#B = B A obj
#C = C A obj
#D = D B C A obj
#E = E C A obj
#F = F D B E C A obj



class X: 
    pass 
 
class Y: 
    pass 
 
class Z(X, Y): 
    pass 
 
class W(Y, X): 
    pass 
 
class V(Z, W): 
    pass 
 

#X = X obj
#Y = Y obj
#Z = Z X Y obj
#W = W Y X obj #error
#V = V Z W Y X obj 
#
#



class A: 
    pass 
 
class B(A): 
    pass 
 
class C(A): 
    pass 
 
class Mixin1: 
   pass 
 
class Mixin2(Mixin1): 
    pass 
 
class D(B, Mixin2, C): 
    pass 
 
#A =  A obj
#B = B A obj
#C = C A obj
#Minin1 = Mixin1 obj
#Mixin2 = Mixin2 Mixin1 obj
#D = D B Mixin2 Mixin1 C A obj
#






class A: 
    pass 
 
class B(A): 
    pass 
 
class C(B): 
    pass 
 
class D(A): 
    pass 
 
class E(C, D): 
    pass 
 
class F(E, B): 
    pass 
 

#A = A obj
#B = B A obj
#C = C B A obj
#D = D A obj
#E = E C B D A obj
#F = F E C D B A obj #error(one parent is another parent's parent)

 
