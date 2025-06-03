import pulp

# 変数定義
variables = {
    'x12': pulp.LpVariable('x12', 0, 4),
    'x13': pulp.LpVariable('x13', 0, 3),
    'x21': pulp.LpVariable('x21', 0, 1),
    'x23': pulp.LpVariable('x23', 0, 4),
    'x25': pulp.LpVariable('x25', 0, 3),
    'x34': pulp.LpVariable('x34', 0, 3),
    'x35': pulp.LpVariable('x35', 0, 2),
    'x45': pulp.LpVariable('x45', 0, 2),
    'x53': pulp.LpVariable('x53', 0, 2),
    'z':   pulp.LpVariable('z')
}

# 問題定義（最大化）
p = pulp.LpProblem("最大化問題", sense=pulp.LpMaximize)

# 目的関数
p += variables['z'], "zの最大化"

# 制約条件
p += (variables['x12'] + variables['x13']) - variables['x21'] == variables['z']
p += (variables['x21'] + variables['x23'] + variables['x25']) - variables['x12'] == 0
p += (variables['x34'] + variables['x35']) - (variables['x13'] + variables['x23'] + variables['x53']) == 0
p += variables['x45'] - variables['x34'] == 0
p += variables['x53'] - (variables['x25'] + variables['x35'] + variables['x45']) == -variables['z']

# 求解
result = p.solve()
print(pulp.LpStatus[result])
print(f'z = {pulp.value(variables["z"]):.2f}')
for name in variables:
    if name != 'z':
        print(f'{name} = {pulp.value(variables[name]):.2f}')
