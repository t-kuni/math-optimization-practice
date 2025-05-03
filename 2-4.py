import pulp

x1 = pulp.LpVariable('x1', lowBound=0)
x2 = pulp.LpVariable('x2', lowBound=0)

p = pulp.LpProblem('コスト最小化問題', sense=pulp.LpMinimize)

# 目的関数
p += 9*x1 + 6*x2, '目的関数'

# 制約条件
p += 8*x1 + 5*x2 >= 1300, '制約1'
p += 2*x1 + 3*x2 >= 500, '制約2'

print(p)

result = p.solve()

print(pulp.LpStatus[result])
print('目的関数の値 =', pulp.value(p.objective))
for v in p.variables():
    print(f'{v.name} = {pulp.value(v)}')
