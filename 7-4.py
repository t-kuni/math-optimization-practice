import pulp

# 問題定義（最大化）
p = pulp.LpProblem("最大化問題", sense=pulp.LpMaximize)

# 変数定義
xA = pulp.LpVariable("xA", lowBound=0)
xB = pulp.LpVariable("xB", lowBound=0)
xC = pulp.LpVariable("xC")
xD = pulp.LpVariable("xD")
xE = pulp.LpVariable("xE")
xF = pulp.LpVariable("xF")
xG = pulp.LpVariable("xG")
xT = pulp.LpVariable("xT")

dA = pulp.LpVariable("dA", lowBound=0, upBound=0.001)
dB = pulp.LpVariable("dB", lowBound=0, upBound=0.001)
dC = pulp.LpVariable("dC", lowBound=0, upBound=0.001)
dD = pulp.LpVariable("dD", lowBound=0, upBound=0.001)
dE = pulp.LpVariable("dE", lowBound=0, upBound=0.001)
dF = pulp.LpVariable("dF", lowBound=0, upBound=0.001)
dG = pulp.LpVariable("dG", lowBound=0, upBound=0.001)

# 目的関数
p += dA + dB + dC + dD + dE + dF + dG

# 制約条件
p += xC >= xA + 4 + dA
p += xC >= xB + 5 + dB
p += xD >= xB + 5 + dB
p += xE >= xC + 7 + dC
p += xF >= xC + 7 + dC
p += xF >= xD + 7 + dD
p += xG >= xE + 2 + dE
p += xG >= xF + 9 + dF
p += xT >= xG + 2 + dG
p += xT <= 23

# 求解
result = p.solve()
print(pulp.LpStatus[result])
print(f'z = {pulp.value(p.objective):.6f}')
for v in p.variables():
    print(f'{v.name} = {v.varValue:.6f}')
