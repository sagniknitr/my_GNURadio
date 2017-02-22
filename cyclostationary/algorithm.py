import numpy as np

a = 0
A = 0
def idft_mat(N):
    global a,A
    a=np.zeros(shape=(N,N),dtype=complex)
    for i in range(0,N-1):
        for j in range(0,N-1):
            a[i,j]=((2j*22*i*j)/(N*7))
    A=np.exp(a)        
        
   

idft_mat(10)
print A
