import pulp

# 変数定義（連続変数、非負）
x11 = pulp.LpVariable('x11', 0)
x12 = pulp.LpVariable('x12', 0)
x21 = pulp.LpVariable('x21', 0)
x22 = pulp.LpVariable('x22', 0)
x31 = pulp.LpVariable('x31', 0)
x32 = pulp.LpVariable('x32', 0)

# 問題定義（最小化）
p = pulp.LpProblem("輸送問題_等式制約", sense=pulp.LpMinimize)

# 目的関数
p += 16*x11 + 8*x12 + 10*x21 + 16*x22 + 12*x31 + 14*x32, "総輸送コスト"

# 制約条件
p += x11 + x12 == 120, "S1供給"
p += x21 + x22 == 100, "S2供給"
p += x31 + x32 == 80,  "S3供給"
p += x11 + x21 + x31 == 160, "D1需要"
p += x12 + x22 + x32 == 140, "D2需要"

# 求解
result = p.solve()
print(pulp.LpStatus[result])
print(f'目的関数値 = {pulp.value(p.objective):.0f}')
for v in p.variables():
    print(f'{v.name} = {pulp.value(v):.0f}')
