import pulp

# 問題定義（最小化）
p = pulp.LpProblem("最小化問題", sense=pulp.LpMinimize)

# 変数定義
x = [[pulp.LpVariable(f"x{i+1}{j+1}", cat="Binary") for j in range(6)] for i in range(3)]
t = [pulp.LpVariable(f"t{i+1}", lowBound=0) for i in range(3)]

# 目的関数
p += t[0] + t[1] + t[2]

# 制約1：各列に1つだけ割り当てる
for j in range(6):
    p += x[0][j] + x[1][j] + x[2][j] == 1

# 制約2：t1に関する上下限
p += t[0] >= 14*x[0][0] + 13*x[0][1] + 12*x[0][2] + 14*x[0][3] + 13*x[0][4] + 10*x[0][5] - 25.33
p += t[0] >= -(14*x[0][0] + 13*x[0][1] + 12*x[0][2] + 14*x[0][3] + 13*x[0][4] + 10*x[0][5] - 25.33)

# 制約3：t2に関する上下限
p += t[1] >= 14*x[1][0] + 13*x[1][1] + 12*x[1][2] + 14*x[1][3] + 13*x[1][4] + 10*x[1][5] - 25.33
p += t[1] >= -(14*x[1][0] + 13*x[1][1] + 12*x[1][2] + 14*x[1][3] + 13*x[1][4] + 10*x[1][5] - 25.33)

# 制約4：t3に関する上下限
p += t[2] >= 14*x[2][0] + 13*x[2][1] + 12*x[2][2] + 14*x[2][3] + 13*x[2][4] + 10*x[2][5] - 25.33
p += t[2] >= -(14*x[2][0] + 13*x[2][1] + 12*x[2][2] + 14*x[2][3] + 13*x[2][4] + 10*x[2][5] - 25.33)

# 求解
p.solve()

# 結果表示
print(pulp.LpStatus[p.status])
print(f'z = {pulp.value(p.objective):.4f}')
for i in range(3):
    for j in range(6):
        print(f'x{i+1}{j+1} = {x[i][j].varValue}')
for i in range(3):
    print(f't{i+1} = {t[i].varValue:.4f}')
