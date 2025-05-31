import pulp

# 変数定義（0-1変数）
indices = ['x12','x13','x21','x23','x25','x32','x34','x35','x45','x53']
vars = {name: pulp.LpVariable(name, 0, 1, cat=pulp.LpBinary) for name in indices}

# 問題定義（最小化）
p = pulp.LpProblem("最短経路問題", sense=pulp.LpMinimize)

# 目的関数
p += (
    1*vars['x12'] + 5*vars['x13'] + 1*vars['x21'] + 2*vars['x23'] +
    3*vars['x25'] + 4*vars['x32'] + 3*vars['x34'] + 2*vars['x35'] +
    2*vars['x45'] + 2*vars['x53']
), "コスト合計"

# 制約条件
p += (vars['x12'] + vars['x13']) - vars['x21'] == 1
p += vars['x53'] - (vars['x25'] + vars['x35'] + vars['x45']) == -1
p += (vars['x21'] + vars['x23'] + vars['x25']) - (vars['x12'] + vars['x32']) == 0
p += (vars['x32'] + vars['x34'] + vars['x35']) - (vars['x13'] + vars['x23'] + vars['x53']) == 0
p += vars['x45'] - vars['x34'] == 0

# 求解
result = p.solve()
print(pulp.LpStatus[result])
print(f'目的関数値 = {pulp.value(p.objective):.0f}')
for name in indices:
    if pulp.value(vars[name]) == 1:
        print(f'{name} = 1')
