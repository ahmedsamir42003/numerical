def lagrange(x_list,x):
    lx=[]
    for i in range(len(x_list)):
        up=1
        down=1
        for j in range(len(x_list)):
            if j==i:
                continue
            up=up*(x-x_list[j])
            down=down*(x_list[i]-x_list[j])
        lx.append((up/down))
    return lx

def output(lx,y_list):
    out=0
    for i in range(len(lx)):
        out=out+(lx[i]*y_list[i])
    return out



x_list=[float(i) for i in input('please enter list of x values').split()]
y_list=[float(i) for i in input('please enter list of y values').split()]
x=float(input('enter x value you try to predict'))

lx=lagrange(x_list,x)
out=output(lx,y_list)

print(f'the output of {x} : {out}')
