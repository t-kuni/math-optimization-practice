import pulp

x1 = pulp.LpVariable('x1', 0, cat=pulp.LpInteger)
x2 = pulp.LpVariable('x2', 0, cat=pulp.LpInteger)
x3 = pulp.LpVariable('x3', 0, cat=pulp.LpInteger)
x4 = pulp.LpVariable('x4', 0, cat=pulp.LpInteger)

p = pulp.LpProblem('資料切り出し問題', sense=pulp.LpMinimize)
p += x1 + x2 + x3 + x4 , '目的関数 各パターンで保存したディスク数の和'
p += x1  >= 15, '制約1'
p += 2*x2 + x3  >= 40, '制約2'
p += x3 + 2*x4 >= 65, '制約3'
print(p)

result = p.solve()
print(pulp.LpStatus[result])
pulp.value(p.objective)
for v in p.variables():
    print(f'{v} = {pulp.value(v):.0f}')  # 小数点以下を表示しない
