import constraint


problem = constraint.Problem()

problem.addVariable('CGB', range(1,10))
problem.addVariable('BQS', range(10))

def our_contraint(c,g,d,b,q,s,r):
    if (c*100 + g*10 + b)*(b*100 + q*10 + s) == (d*100000 + s*10000 + b*1000 + r*100 + s*10 + c):
        return True

problem.addConstraint(our_constraint, "DSBRSC")

problem.addConstraint(constraint.AllDifferentConstraint())

solutions = problem.getSolutions()

for solution in solutions:
    print(solution)