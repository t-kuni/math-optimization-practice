import pulp

# 問題定義（最小化）
p = pulp.LpProblem("最小化問題", sense=pulp.LpMinimize)

# 変数定義（上下限あり）
bounds = {
    'x12': (0, 20), 'x13': (0, 20), 'x23': (0, 15), 'x24': (0, 20),
    'x34': (0, 30), 'x35': (0, 10), 'x45': (0, 30)
}
vars = {k: pulp.LpVariable(k, lowBound=lo, upBound=hi) for k, (lo, hi) in bounds.items()}

# 目的関数
p += (
    4*vars['x12'] + 4*vars['x13'] + vars['x23'] +
    2*vars['x24'] + 5*vars['x34'] + 3*vars['x35'] + 5*vars['x45']
), "目的関数"

# 制約条件
p += vars['x12'] + vars['x13'] == 30
p += -vars['x12'] + vars['x23'] + vars['x24'] == 0
p += -vars['x13'] - vars['x23'] + vars['x34'] + vars['x35'] == 0
p += -vars['x24'] - vars['x34'] + vars['x45'] == -10
p += -vars['x35'] - vars['x45'] == -20

# 求解
result = p.solve()
print(pulp.LpStatus[result])
print(f'z = {pulp.value(p.objective):.0f}')
for k in vars:
    print(f'{k} = {pulp.value(vars[k]):.0f}')
