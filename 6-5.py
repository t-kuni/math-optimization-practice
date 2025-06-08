import pulp

# 問題定義（最大化）
p = pulp.LpProblem("最大化問題", sense=pulp.LpMaximize)

# 変数定義（0-1変数）
x = {f'x{i}{j}': pulp.LpVariable(f'x{i}{j}', cat='Binary')
     for i in [1,2,3,4,5] for j in [1,2,3,4,5] if f'x{i}{j}' in [
         'x11', 'x13', 'x22', 'x24', 'x25',
         'x31', 'x33', 'x34', 'x43', 'x45',
         'x51', 'x52', 'x55'
     ]}

# 目的関数
p += (
    5*x['x11'] + x['x13'] + 2*x['x22'] + 8*x['x24'] + 7*x['x25'] +
    4*x['x31'] + 6*x['x33'] + 7*x['x34'] + 9*x['x43'] + 4*x['x45'] +
    7*x['x51'] + 8*x['x52'] + 6*x['x55']
), "目的関数"

# 制約条件
p += x['x11'] + x['x13'] == 1
p += x['x22'] + x['x24'] + x['x25'] == 1
p += x['x31'] + x['x33'] + x['x34'] == 1
p += x['x43'] + x['x45'] == 1
p += x['x51'] + x['x52'] + x['x55'] == 1

p += x['x11'] + x['x31'] + x['x51'] == 1
p += x['x22'] + x['x52'] == 1
p += x['x13'] + x['x33'] + x['x43'] == 1
p += x['x24'] + x['x34'] == 1
p += x['x25'] + x['x45'] + x['x55'] == 1

# 求解
result = p.solve()
print(pulp.LpStatus[result])
print(f'z = {pulp.value(p.objective):.0f}')
for k in x:
    print(f'{k} = {pulp.value(x[k]):.0f}')
