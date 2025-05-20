exp1_detectors = {'ALPHA', 'BETA', 'GAMMA'}
exp2_detectors = {'GAMMA', 'DELTA', 'EPSILON'}

print('Union:', exp1_detectors.union(exp2_detectors))
print(exp1_detectors | exp2_detectors)

print('Intersection', exp1_detectors.intersection(exp2_detectors))
print(exp1_detectors & exp2_detectors)

print('Difference', exp1_detectors.difference(exp2_detectors))