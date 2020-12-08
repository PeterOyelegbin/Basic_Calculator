# MyMath Module
from math import sin, cos, tan, asin, acos, atan, sqrt, log, log10, factorial

# Trigonometric functions
def Sin(deg):
    return sin(deg * (3.142/180))

def Cos(deg):
    return cos(deg * (3.142/180))

def Tan(deg):
    return tan(deg * (3.142/180))

def aSin(deg):
    return asin(deg) * (180/3.142)

def aCos(deg):
    return acos(deg) * (180/3.142)

def aTan(deg):
    return atan(deg) * (180/3.142)

# Pythagoras Theorem
def hyp(Opp, Adj):
    return sqrt(Opp**2 + Adj**2)

def opp(Hyp, Adj):
    return sqrt(Hyp**2 - Adj**2)

def adj(Hyp, Opp):
    return sqrt(Hyp**2 - Opp**2)

# The soh-cah-toa Rule (Trigonometric functions on right triangle)
def soh(opp, hyp):
    return asin(opp/hyp) * (180/3.142)

def cah(adj, hyp):
    return acos(adj/hyp) * (180/3.142)

def toa(opp, adj):
    return atan(opp/adj) * (180/3.142)

# Law of Cosines
def cosine(a, b, C):
    return sqrt(a**2 + b**2 - (2*a*b * cos(C * (3.142/180))))

# def Sinh(deg):
#     return sinh(deg)

# def Cosh(deg):
#     return cosh(deg)

# def Tanh(deg):
#     return tanh(deg)

# def Log(deg):
#     return log10(deg)

# def ln(deg):
#     return log(deg)

# def Sqr(deg):
#     return deg * deg

# def Sqrt(deg):
#     return sqrt(deg)

# def E():
#     return 2.718281828459045

# def Pi():
#     return 3.141592653589793

# def Fac(deg):
#     return factorial(deg)
