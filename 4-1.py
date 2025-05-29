import pulp

# 変数の定義（非負の整数）
x11 = pulp.LpVariable('x11', 0, cat=pulp.LpInteger)
x12 = pulp.LpVariable('x12', 0, cat=pulp.LpInteger)
x21 = pulp.LpVariable('x21', 0, cat=pulp.LpInteger)
x22 = pulp.LpVariable('x22', 0, cat=pulp.LpInteger)
x31 = pulp.LpVariable('x31', 0, cat=pulp.LpInteger)
x32 = pulp.LpVariable('x32', 0, cat=pulp.LpInteger)

# 問題定義（最小化問題）
p = pulp.LpProblem("輸送問題", sense=pulp.LpMinimize)

# 目的関数
p += 10*x11 + 14*x12 + 12*x21 + 8*x22 + 6*x31 + 12*x32, '総輸送コスト'

# 制約条件
p += x11 + x12 <= 160, 'S1の供給制約'
p += x21 + x22 <= 80,  'S2の供給制約'
p += x31 + x32 <= 80,  'S3の供給制約'
p += x11 + x21 + x31 == 160, 'D1の需要制約'
p += x12 + x22 + x32 == 140, 'D2の需要制約'

# 求解
result = p.solve()
print(pulp.LpStatus[result])
print(f'目的関数値 = {pulp.value(p.objective):.0f}')
for v in p.variables():
    print(f'{v.name} = {pulp.value(v):.0f}')
