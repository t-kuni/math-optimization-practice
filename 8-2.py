import pulp

# 問題定義（最大化）
p = pulp.LpProblem("最大化問題", sense=pulp.LpMaximize)

# 変数定義（二値変数）
x = {}
for i in [1, 2, 3, 4]:
    for j in [1, 2, 3, 4]:
        x[(i, j)] = pulp.LpVariable(f"x{i}{j}", cat="Binary")

# t変数（連続、非負）
t = pulp.LpVariable("t", lowBound=0)

# 目的関数
p += t

# 制約条件
p += x[(1,1)] + x[(1,3)] + x[(1,4)] == 1
p += x[(2,1)] + x[(2,2)] + x[(2,3)] == 1
p += x[(3,2)] + x[(3,4)] == 1
p += x[(4,2)] + x[(4,3)] == 1

p += x[(1,1)] + x[(2,1)] == 1
p += x[(2,2)] + x[(3,2)] + x[(4,2)] == 1
p += x[(1,3)] + x[(2,3)] + x[(4,3)] == 1
p += x[(1,4)] + x[(3,4)] == 1

p += 5*x[(1,1)] + 3*x[(1,3)] + 2*x[(1,4)] >= t
p += 5*x[(2,1)] + 4*x[(2,2)] + 2*x[(2,3)] >= t
p += 2*x[(3,2)] + 4*x[(3,4)] >= t
p += 2*x[(4,2)] + 5*x[(4,3)] >= t

# 求解
p.solve()

# 結果表示
print(pulp.LpStatus[p.status])
print(f't = {t.varValue:.4f}')
for key in x:
    print(f'x{key[0]}{key[1]} = {x[key].varValue}')
