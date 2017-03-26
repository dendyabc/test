import math

def poiont(in_r):
    point_list=[]
    bound=int(math.sqrt(in_r))
    x=0
    for x in range(0,bound+1):
        gap=in_r-x*x
        if gap-math.sqrt(gap)>0.000-1 and gap-math.sqrt(gap)<0.0001:
            point_list.append(x,math.sqrt(gap))
	return len(point_list)
input_r=int(raw_input())
print poiont(input_r)