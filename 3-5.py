import pulp

C = {1: 18, 2: 12, 3: 14, 4: 19, 5: 11, 6: 15}  # 価値
A = {1: 22, 2: 9, 3: 13, 4: 24, 5: 21, 6: 14}  # 重さ

x = {i: pulp.LpVariable(f'x{i}', cat=pulp.LpBinary) for i in C.keys()}
print(x)

p = pulp.LpProblem('ナップサック問題', sense=pulp.LpMaximize)
p += pulp.lpSum(C[i] * x[i] for i in x.keys()), '目的関数 詰めた品物の価値'
p += pulp.lpSum(A[i] * x[i] for i in x.keys()) <= 60, '重量制約'
print(p)

result = p.solve()

print(pulp.LpStatus[result])
pulp.value(p.objective)
for v in p.variables():
    print(f'{v} = {pulp.value(v):.0f}')
