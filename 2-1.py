import pulp

x1 = pulp.LpVariable('x1', 0)
x2 = pulp.LpVariable('x2', 0)

p = pulp.LpProblem('生産計画問題', sense=pulp.LpMaximize)
p += x1 + 2*x2, '目的関数　利益見込み'
p += x1 + 3*x2 <= 24, '原料制約'
p += 4*x1 + 4*x2 <= 48, '労働時間制約'
p += 2*x1 + x2 <= 22, '機械稼働制約'
print(p)

result = p.solve()

print(pulp.LpStatus[result])
pulp.value(p.objective)
for v in p.variables():
    print(f'{v} = {pulp.value(v)}')
