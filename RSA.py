import random as rand
class RSA:
    def __int__(self):
        print(self.genPrimeList())
        self.p,self.q = map(int,input().split())
        self.N = self.p * self.q
        print(self.genEList())
        self.e = int(input())
def encrypt(self,msg):
    print("Encrypt")
def decrypt(self,msg):
    print("Decrypt")
def grnRandomList(self):
    data = []
    while len(data)<6:
        y=rand.randint(1024,25536)
        if isPrime(y):
            data.append(y)
        return data
def isPrime(self,x):
    flag = True
    i=2
    while i<x//2:
        if x % i == 0:
            flag = False
            break
        i = i + 1
    return flag
def fun(self,N1,e):
    maxVal = max(N1,e)
    minVal = min(N1,e)
    if maxVal % minVal == 0:
        return minVal
    else:
        return self.fun(mixVal,maxVal % mixVal)
if __name__ == '__main__':
    rsa = RSA()
    rsa.encrypt()
