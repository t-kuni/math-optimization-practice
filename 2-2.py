import pulp

# 食品１ 12円/g, 栄養素A:3/g,  栄養素B:1/g, 栄養素C:4/g
# 食品２ 15円/g, 栄養素A:2/g,  栄養素B:5/g, 栄養素C:3/g
# 栄養素A >= 200/day
# 栄養素B >= 160/day
# 栄養素C >= 250/day

x1 = pulp.LpVariable('x1', 0)
x2 = pulp.LpVariable('x2', 0)

p = pulp.LpProblem('食事問題（線形最適化問題）', sense=pulp.LpMinimize)
p += 12*x1 + 15*x2, '目的関数　食費'
p += 3*x1 + 2*x2 >= 200, '栄養素A >= 200'
p += 1*x1 + 5*x2 >= 160, '栄養素B'
p += 4*x1 + 3*x2 >= 250, '栄養素C'
print(p)

result = p.solve()

print(pulp.LpStatus[result])
pulp.value(p.objective)
for v in p.variables():
    print(f'{v} = {pulp.value(v)}')
