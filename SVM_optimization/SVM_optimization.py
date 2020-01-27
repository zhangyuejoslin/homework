import gurobipy as gp
from gurobipy import GRB


m = gp.Model("svm_optimizer")

# create variable
w1 = m.addVar(vtype=GRB.CONTINUOUS, name="w1",lb=-GRB.INFINITY)
w2 = m.addVar(vtype=GRB.CONTINUOUS, name="w2",lb=-GRB.INFINITY)
b = m.addVar(vtype=GRB.CONTINUOUS, name="b",lb=-GRB.INFINITY)

# set objective
m.setObjective(1/2 * (w1 * w1 + w2 * w2), GRB.MINIMIZE)

data = [(0, 0, -1), (2, 2, -1), (2, 0, 1), (2, 2, -1)]

for x1, x2, y in data:
    m.addConstr(y * w1 *x1 + y * w2 * x2 + y * b >= 1, "c")

m.optimize()

for v in m.getVars():
    print('%s %g' % (v.varName, v.x))

print('Obj: %g' % m.objVal)

