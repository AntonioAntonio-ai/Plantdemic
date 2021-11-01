from math import gcd


class Line3(list):
    def __init__(self,list_of_xyz):
        self = list_of_xyz

'''
print(Line3([[0,50,0],[20,50,0],[20,60,-10]]))
'''

def simplify(frac):
    div = gcd(frac[0],frac[1])
    return([frac[0] // div,frac[1] // div])
