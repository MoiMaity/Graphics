import math
import numpy as np
import matplotlib.pyplot as plt

def multiplication(a,b):
    c=[[0 for i in range(len(b[0]))] for j in range(len(a))]
    for i in range(len(c)):
        for j in range(len(c[0])):
            for k in range(len(b)):
                c[i][j]+=a[i][k]*b[k][j];
    return c

def translate(tx,ty):
    c=[[0.0 for i in range(3)] for j in range(3)]
    for i in range(3):
        for j in range(3):
            if(i==j):
                c[i][j]=1.0
    c[2][0]=tx
    c[2][1]=ty
    return c

def rotate(angle):
    c=[[math.cos(angle),math.sin(angle),0],
       [-math.sin(angle),math.cos(angle),0],
       [0,0,1]]
    return c

def reflect(x,y):
    c=[[x,0,0],
       [0,y,0],
       [0,0,1]]
    return c

print("the line is in the form y=mx+c")
print("m value of the line: ")
print("If the line is about y axis, press m=999")
m=float(input())


print("c value of the line: ")
print("If the line is about y axis, press c=999")
print("If the line is about y axis, press c=998")

c=float(input())

n=int(input("Enter number of vertices of object : "))
x=[]
y=[]
v=[[1 for i in range(3)] for j in range(n)]
print(v)
print("Enter the coordinates in clockwise order or anticlockwise order : ")
for i in range(n):
    print("vertex",i+1,"- Enter x and y coordinates separated by space : ")
    a,b=list(map(float,input().split()))
    x.append(a)
    y.append(b)
    plt.scatter(x,y,color="blue")
    v[i][0]=a
    v[i][1]=b

x.append(x[0])
y.append(y[0])

tx=0.0
ty=0.0

x_values=[-max(max(x),max(y)),+max(max(x),max(y))]
y_values=[0,0]
plt.plot(x_values,y_values,color="none")

#y-axis
y_values=[-max(max(x),max(y)),+max(max(x),max(y))]
x_values=[0,0]
plt.plot(x_values,y_values,color="none")

if (m==999):
    print("Enter x and y coordinates of 1st point separated by space : ")
    x1,y1=list(map(float,input().split()))
    plt.scatter(x1,y1,color="red")

    print("Enter x and y coordinates of 2nd point separated by space : ")
    x2,y2=list(map(float,input().split()))
    plt.scatter(x2,y2,color="red")
    tx=x1
    t_inverse=translate(-tx,ty)     #inverse translation
    reflect_y=reflect(-1,1)         #reflection about y axis
    t=translate(tx,ty)              #translation
    ref=multiplication((multiplication(t_inverse,reflect_y)),t)
    ans=multiplication(v,ref)
    
    y_line = np.linspace(-max(max(x),max(y))-5,max(max(x),max(y))+5,5)
    x_line = 0*y_line+tx
    plt.plot(x_line,y_line,color="red",label="mirror")
    
elif(m==0):
    print("Enter x and y coordinates of 1st point separated by space : ")
    x1,y1=list(map(float,input().split()))
    plt.scatter(x1,y1,color="red")

    print("Enter x and y coordinates of 2nd point separated by space : ")
    x2,y2=list(map(float,input().split()))
    plt.scatter(x2,y2,color="red")
    ty=y1
    t_inverse=translate(tx,-ty)     #inverse translation
    reflect_x=reflect(1,-1)         #reflection about x axis
    t=translate(tx,ty)              #translation
    ref=multiplication((multiplication(t_inverse,reflect_x)),t)
    ans=multiplication(v,ref)
    
    x_line = np.linspace(-max(max(x),max(y))-5,max(max(x),max(y))+5,5)
    y_line = 0*x_line+ty
    plt.plot(x_line,y_line,color="red",label="mirror")

else:
    
    angle=math.atan(m)
    print(angle)
    ty=c
    t_inverse=translate(tx,-ty)     #inverse translation
    r_inverse=rotate(-angle)        #inverse rotation
    reflect_x=reflect(1,-1)         #reflection about x axis
    r=rotate(angle)                 #rotation
    t=translate(tx,ty)              #translation
    ref_=multiplication((multiplication(t_inverse,r_inverse)),reflect_x)
    ref=multiplication((multiplication(ref_,r)),t)
    ans=multiplication(v,ref)
    
    x_line = np.linspace(-max(max(x),max(y))-5,max(max(x),max(y))+5,5)
    y_line = m*x_line+ty
    plt.plot(x_line, y_line,color="red",label="mirror")

plt.plot(x,y,color="blue",label="original image")

x_new=[]
y_new=[]
for i in range(len(ans)):
    x_new.append(ans[i][0])
    y_new.append(ans[i][1])
    plt.scatter(ans[i][0],ans[i][1],color="violet")
    
x_new.append(x_new[0])
y_new.append(y_new[0])
plt.plot(x_new,y_new,color="violet",label="reflected image")

ax = plt.gca()
ax.spines['top'].set_color('none')
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')

plt.grid()
plt.title("2D Reflection")
plt.legend()
plt.show()