import pulp

# 係数
c = {
    'x12': 20, 'x13': 10, 'x23': 5, 'x24': 10,
    'x34': 20, 'x35': 10, 'x45': 20
}

# 変数定義（連続変数）
bounds = {
    'x12': (0, 30), 'x13': (0, 5), 'x23': (0, 10), 'x24': (0, 20),
    'x34': (0, 20), 'x35': (0, 5), 'x45': (0, 10)
}
vars = {k: pulp.LpVariable(k, lowBound=b[0], upBound=b[1]) for k, b in bounds.items()}

# 問題定義（最小化）
p = pulp.LpProblem("最小化問題", sense=pulp.LpMinimize)

# 目的関数
p += pulp.lpSum(c[k] * vars[k] for k in c), "目的関数"

# 制約条件
p += vars['x12'] + vars['x13'] == 30
p += vars['x23'] + vars['x24'] - vars['x12'] == 0
p += vars['x34'] + vars['x35'] - (vars['x13'] + vars['x23']) == 0
p += vars['x45'] - (vars['x24'] + vars['x34']) == -20
p += -(vars['x35'] + vars['x45']) == -10

# 求解
result = p.solve()
print(pulp.LpStatus[result])
print(f'目的関数値 = {pulp.value(p.objective):.0f}')
for k in vars:
    print(f'{k} = {pulp.value(vars[k]):.0f}')
