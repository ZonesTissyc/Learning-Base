import math

ak1 = [41.005,41.167,41.324,41.462,41.602]
ak2 = [42.380,42.510,42.605,42.732,42.842]

bk1 = [33.715,33.555,33.399,33.255,33.110]
bk2 = [32.322,32.222,32.105,31.980,31.875]

ra = []
rb = []

for i in range(5):
    rta = round(round((ak2[i]-bk1[i])*(ak2[i]-ak1[i]),5)/(5893)*(1000000) ,2)
    rtb = round(round((bk2[i]-ak1[i])*(bk2[i]-bk1[i]),5)/(5893)*(1000000) ,2)
    ra.append(rta)
    rb.append(rtb)
ls = ra + rb
r_bar = round(math.fsum(ls)/len(ls), 3)
print(r_bar)