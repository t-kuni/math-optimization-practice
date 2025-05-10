import pulp

C = {1: 18, 2: 14, 3: 16, 4: 7, 5: 12, 6: 22}  # 価値
A = {1: 16, 2: 14, 3: 14, 4: 12, 5: 11, 6: 18}  # 重さ

x = {i: pulp.LpVariable(f'x{i}', cat=pulp.LpBinary) for i in C.keys()}
print(x)

p = pulp.LpProblem('ナップサック問題', sense=pulp.LpMaximize)
p += pulp.lpSum(C[i] * x[i] for i in x.keys()), '目的関数 詰めた品物の価値'
p += pulp.lpSum(A[i] * x[i] for i in x.keys()) <= 50, '重量制約'
print(p)

result = p.solve()

print(pulp.LpStatus[result])
print(f'最大価値: {pulp.value(p.objective)}')
for v in p.variables():
    print(f'{v} = {pulp.value(v):.0f}')
