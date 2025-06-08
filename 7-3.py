import pulp

# 問題定義（最小化）
p = pulp.LpProblem("最小化問題", sense=pulp.LpMinimize)

# 変数定義
xA = pulp.LpVariable("xA", lowBound=0)
xB = pulp.LpVariable("xB", lowBound=0)
xC = pulp.LpVariable("xC")
xD = pulp.LpVariable("xD")
xE = pulp.LpVariable("xE")
xF = pulp.LpVariable("xF")
xG = pulp.LpVariable("xG")
xT = pulp.LpVariable("xT")

# 目的関数
p += xT

# 制約条件
p += xC >= xA + 4
p += xC >= xB + 5
p += xD >= xB + 5
p += xE >= xC + 7
p += xF >= xC + 7
p += xF >= xD + 2
p += xG >= xE + 9
p += xG >= xF + 2
p += xT >= xG + 2

# 求解
result = p.solve()
print(pulp.LpStatus[result])
print(f'xT = {pulp.value(xT):.0f}')
for v in p.variables():
    print(f'{v.name} = {v.varValue:.0f}')
