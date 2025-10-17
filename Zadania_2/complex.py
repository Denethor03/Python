class Complex:
    def __init__(self,re,im):
        self.real = re
        self.imag = im
    def __add__(self,other):
        return Complex(self.real+other.real,self.imag+other.imag)
    def __sub__(self,other):
       return Complex(self.real-other.real,self.imag-other.imag)
    def __iadd__(self,other):
        self.real+=other.real
        self.imag+=other.imag
        return self
    def __isub__(self,other):
        self.real-=other.real
        self.imag-=other.imag
        return self
    def __str__(self):
        if self.imag>=0:
            return f"{self.real}+{self.imag}i"
        else:
            return f"{self.real}{self.imag}i"
    
if __name__ == "__main__":

    c1 = Complex(1,2)
    c2 = Complex(2,3)
    print(c1)
    print(c1+c2)
    c1+=c2
    print(c1)
    c2-=c1
    print(c2)