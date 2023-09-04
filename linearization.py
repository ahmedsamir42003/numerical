def linearization(x_list,y_list):

  s_y=sum(y_list)
  s_x=sum(x_list)
  n=len(x_list)
  s_xs=sum([i*i for i in x_list])
  s_yx=sum([i*j for i,j in zip(x_list,y_list)])

  return ( [[n,s_x,s_y],[s_x,s_xs,s_yx]])

def solve(lis):

    for i in range(len(lis)):
        for j in range(i + 1, len(lis)):
            factor = -lis[j][i] / lis[i][i]
            for k in range(len(lis[i])):
                lis[j][k] = factor * lis[i][k] + lis[j][k]

    a=lis[1][2]/lis[1][1]
    b=( lis[0][2]-(lis[0][1]*a) )/lis[0][0]

    return (a,b)

x_list=[float(i) for i in input('please enter list of x values').split()]
y_list=[float(i) for i in input('please enter list of y values').split()]

lis=linearization(x_list,y_list)
a,b=solve(lis)

print(f'the linear equation is: y = {a} x + {b}')


