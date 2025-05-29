import pulp

# 変数定義（0-1変数）
indices = ['x11','x13','x14','x21','x22','x23','x32','x34','x42','x43']
vars = {name: pulp.LpVariable(name, 0, 1, cat=pulp.LpBinary) for name in indices}

# 問題定義（最大化）
p = pulp.LpProblem("割当問題2", sense=pulp.LpMaximize)

# 目的関数
p += (
    5*vars['x11'] + 3*vars['x13'] + 2*vars['x14'] +
    5*vars['x21'] + 4*vars['x22'] + 2*vars['x23'] +
    2*vars['x32'] + 4*vars['x34'] +
    2*vars['x42'] + 5*vars['x43']
), "評価値合計"

# 制約条件
p += vars['x11'] + vars['x13'] + vars['x14'] == 1
p += vars['x21'] + vars['x22'] + vars['x23'] == 1
p += vars['x32'] + vars['x34'] == 1
p += vars['x42'] + vars['x43'] == 1

p += vars['x11'] + vars['x21'] == 1
p += vars['x22'] + vars['x32'] + vars['x42'] == 1
p += vars['x13'] + vars['x23'] + vars['x43'] == 1
p += vars['x14'] + vars['x34'] == 1

# 求解
result = p.solve()
print(pulp.LpStatus[result])
print(f'目的関数値 = {pulp.value(p.objective):.0f}')
for name in indices:
    if pulp.value(vars[name]) == 1:
        print(f'{name} = 1')
