# import constraint
# import logilib.constraint


problem = constraint.Problem()

problem.addVariable('x', [1,2,3])
problem.addVariable('y', range(10))

def our_contraint(x,y):
    if x + y >= 5:
        return True;

problem.addConstraint(our_constraint, ['x','y'])

solutions = problem.getSolutions()

for solution in solutions:
    print(solution)