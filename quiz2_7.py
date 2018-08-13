import numpy as np
x=np.matrix([1,2,3]).T
y=np.matrix([4,5,6]).T
S=np.matrix([[2,1,4],[5,-1,3],[1,7,2]])
A=np.matrix([[0.4,0.1,0.14],[12.4,-0.01,0.3],[1.6,7.5,0.2]])

def cal(x,y,s,a):
    p1 = y.T.dot(np.outer(x,y))
    p2 = p1.dot(a)
    p3 = p2.dot(np.diag(np.diag(np.linalg.inv(s))))
    p4 = p3.dot(y)
    p5 = (1/np.linalg.det(A)**2)*p4
    return p5