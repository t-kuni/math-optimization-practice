import pulp

# 問題定義（最小化）
p = pulp.LpProblem("最小化問題", sense=pulp.LpMinimize)

# 変数定義（連続変数）
vars = ['xA', 'xB', 'xC', 'xD', 'xE', 'xF', 'xT']
x = {v: pulp.LpVariable(v, lowBound=0) for v in vars}

# 目的関数
p += x['xT'], "目的関数"

# 制約条件
p += x['xA'] >= 0
p += x['xB'] >= 0
p += x['xC'] >= x['xA'] + 10
p += x['xC'] >= x['xB'] + 7
p += x['xD'] >= x['xA'] + 10
p += x['xD'] >= x['xB'] + 7
p += x['xE'] >= x['xC'] + 3
p += x['xF'] >= x['xD'] + 8
p += x['xF'] >= x['xE'] + 3
p += x['xT'] >= x['xF'] + 4

# 求解
result = p.solve()
print(pulp.LpStatus[result])
print(f'z = {pulp.value(p.objective):.0f}')
for v in vars:
    print(f'{v} = {pulp.value(x[v]):.0f}')
