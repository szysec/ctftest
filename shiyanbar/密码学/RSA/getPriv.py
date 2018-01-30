#coding:utf-8
import math  
import sys  
from Crypto.PublicKey import RSA  
keypair=RSA.generate(1024)  
keypair.p=##the value of p
keypair.q=##the value of q
keypair.e=65537  
keypair.n=keypair.p*keypair.q  
Qn=long((keypair.p-1)*(keypair.q-1))  
  
i=1  
while(True):  
    x=(Qn*i)+1  
    if(x%keypair.e==0):  
        keypair.d=x/keypair.e  
        break  
    i+=1  
private=open('private.pem','w')  
private.write(keypair.exportKey())  
private.close()  
