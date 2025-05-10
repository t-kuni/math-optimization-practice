import pulp

x1 = pulp.LpVariable('x1', 0, cat=pulp.LpInteger)
x2 = pulp.LpVariable('x2', 0, cat=pulp.LpInteger)
x3 = pulp.LpVariable('x3', 0, cat=pulp.LpInteger)
x4 = pulp.LpVariable('x4', 0, cat=pulp.LpInteger)
x5 = pulp.LpVariable('x5', 0, cat=pulp.LpInteger)
x6 = pulp.LpVariable('x6', 0, cat=pulp.LpInteger)

p = pulp.LpProblem('資料切り出し問題', sense=pulp.LpMinimize)
p += x1 + x2 + x3 + x4 + x5 + x6, '目的関数 各パターンで保存したディスク数の和'
p += x1 + x2 >= 26, '15 GBファイルの保存'
p += x1 + 3*x3 + 2*x4 + x5 >= 52, '8 GBファイルの保存'
p += x2 + x4 + 2*x5 + 4*x6 >= 65, '6 GBファイルの保存'
print(p)

result = p.solve()
print(pulp.LpStatus[result])
pulp.value(p.objective)
for v in p.variables():
    print(f'{v} = {pulp.value(v):.0f}')  # 小数点以下を表示しない
