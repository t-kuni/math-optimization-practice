import pulp

x1 = pulp.LpVariable('x1', lowBound=0)
x2 = pulp.LpVariable('x2', lowBound=0)

p = pulp.LpProblem('線形計画問題', sense=pulp.LpMaximize)

# 目的関数
p += 4*x1 + 3*x2, '目的関数'

# 制約条件
p += 5*x1 + 2*x2 <= 50, '制約1'
p += x1 + x2 <= 20, '制約2'
p += 4*x1 + 5*x2 <= 90, '制約3'

print(p)

result = p.solve()

print(pulp.LpStatus[result])
print('目的関数の値 =', pulp.value(p.objective))
for v in p.variables():
    print(f'{v.name} = {pulp.value(v)}')
