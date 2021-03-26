import pulp as p

Lp_Prob=p.LpProblem("Problem",p.LpMaximize)

x=p.LpVariable("x", lowBound=0)
y=p.LpVariable("y", lowBound=0)
z=p.LpVariable("z", lowBound=0)

Lp_Prob+=x*1.25+y*1.50+z*1.75

Lp_Prob+=2*x+3.50*y<=0.25
Lp_Prob+=2.75*x+2*y<=0.75
Lp_Prob+=3.50*x<=0.60

Lp_Prob+=x+y+z>=30

print (Lp_Prob)

status=Lp_Prob.solve()
print (p.LpStatus[status])

print ("x= ",p.value(x), "y= ",p.value(y), "z= ",p.value(z), "objcetive= ",p.value(Lp_Prob.objective))
