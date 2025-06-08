import pulp

# 問題定義（最大化）
p = pulp.LpProblem("最大化問題", sense=pulp.LpMaximize)

# 変数定義
bounds = {
    'x12': (0, 5), 'x13': (0, 4), 'x21': (0, 2), 'x23': (0, 1),
    'x24': (0, 2), 'x34': (0, 2), 'x35': (0, 5), 'x45': (0, 3)
}
vars = {k: pulp.LpVariable(k, lowBound=lo, upBound=hi) for k, (lo, hi) in bounds.items()}
z = pulp.LpVariable("z")

# 目的関数
p += z, "目的関数"

# 制約条件
p += vars['x12'] + vars['x13'] - vars['x21'] == z
p += -vars['x12'] + vars['x21'] + vars['x23'] + vars['x24'] == 0
p += -vars['x13'] - vars['x23'] + vars['x34'] + vars['x35'] == 0
p += -vars['x24'] - vars['x34'] + vars['x45'] == 0
p += -vars['x35'] - vars['x45'] == -z

# 求解
result = p.solve()
print(pulp.LpStatus[result])
print(f'z = {pulp.value(z):.0f}')
for k in vars:
    print(f'{k} = {pulp.value(vars[k]):.0f}')
