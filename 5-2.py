import pulp

# 変数定義（0-1変数）
indices = ['x12', 'x13', 'x21', 'x23', 'x24', 'x34', 'x35', 'x45']
vars = {name: pulp.LpVariable(name, 0, 1, cat=pulp.LpBinary) for name in indices}

# 問題定義（最小化）
p = pulp.LpProblem("最短経路問題", sense=pulp.LpMinimize)

# 目的関数
p += (
    2*vars['x12'] + 4*vars['x13'] + 2*vars['x21'] + 1*vars['x23'] +
    4*vars['x24'] + 3*vars['x34'] + 4*vars['x35'] + 3*vars['x45']
), "コスト合計"

# 制約条件
p += (vars['x12'] + vars['x13']) - vars['x21'] == 1
p += (vars['x21'] + vars['x23'] + vars['x24']) - vars['x12'] == 0
p += (vars['x34'] + vars['x35']) - (vars['x13'] + vars['x23']) == 0
p += vars['x45'] - (vars['x24'] + vars['x34']) == 0
p += -(vars['x35'] + vars['x45']) == -1

# 求解
result = p.solve()
print(pulp.LpStatus[result])
print(f'目的関数値 = {pulp.value(p.objective):.0f}')
for name in indices:
    if pulp.value(vars[name]) == 1:
        print(f'{name} = 1')
