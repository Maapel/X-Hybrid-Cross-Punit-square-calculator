import itertools as it
import csv

def cross(T,t):
    a,b=(T,t)
    a=list(a)
    b = list(b)
    gam1=[]
    gam2=[]
    for z in range(0,len(a),2):
        gam1.append(a[z])
        gam2.append(b[z])

    #alilles
    al=""
    for z in range(len(gam1)):
        al+=gam1[z]+gam2[z]
    return (al,gam1,gam2)

def g(x):
    x=list(x)
    if len(x)==2:
        if x[0]==x[1]:
            return [x[0]]
        else:
            return [x[0],x[1]]
    else:
        g=[]
        tmp=[]
        tmp = list(it.combinations(x,(len(x)//2)))
        for i in tmp:
            valid = False
            for z in range(0,len(i)):
                a = i[z].lower()
                for y in range(0,len(i)):
                    if y ==z:
                        continue

                    if a ==i[y]:
                        # print(valid)
                        valid =True
                        break

            if valid:
                pass
            else:
                y=""
                for z in i:
                    y+=str(z)
                g.append(y)

        return g

def self(g):
    gen = []
    for i in g:

        for c in g:
            tmp=""
            for z in range(len(i)):
                if i[z].islower():
                    tmp+=c[z]+i[z]
                else:
                    tmp+=i[z]+c[z]
            gen.append(tmp)
    return gen


a=input(" Trait in capital ")
b=a.lower()
t = input("title ")
f=[]

t+=".csv"

#f1 generation
s,g1,g2=cross(a,b)
f.append(s)
a1,a2 = ((g1),(g2))
g1=""
g2=""
for i in a1:
    g1+=i
for i in a2:
    g2+=i


print("Gamets  " +g1 +"  "+ g2)
print("F1 = "+f[0])

gam = g(f[0])
print("Gamets " + str(gam))
f.append(self(gam))
print("F"+str(2)+ "     " +  str(f[1]))
field=["Gamets"]
for a in gam:
    field.append(a)
with open(t, mode='w') as csv_file:
    # fieldnames = field

    writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerow([a,b])
    writer.writerow(["Gamets",g1,g2])
    writer.writerow(["F1",f[1][0]])
    writer.writerow(field)

    writer.writerow(  field)
    for i in range(len(gam)):
        row = [gam[i]]
        for z in range(len(gam)):
            row.append(f[1][z])


        writer.writerow(row)
