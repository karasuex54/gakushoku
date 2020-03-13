# coding: utf-8

# Dummy Nihongo: あ（私の使っているテキストエディタにUTF-8と認識させるため）


# Import
# -----------------------------------------------------------------------------
# MIPCL-PY
import mipcl_py.mipshell.mipshell as mp
# -----------------------------------------------------------------------------


# Main
# -----------------------------------------------------------------------------
print(f'-' * 40)
print(f'[宣言]')

# 数理最適化問題を宣言（名前をつける必要あり）
prob = mp.Problem('Problem-1')

# 変数を宣言（連続変数）
# 引数を全部指定する場合
x = mp.Var(name='x', type=mp.REAL, lb=0.0, ub=mp.VAR_INF, priority=0)
# 引数をけっこう省略する場合（type以降のデフォルト値は↑と同じ）
y = mp.Var(name='y')

# 目的関数を宣言（最大化）
mp.maximize(x + y)

# 制約条件を宣言
2 * x + y <= 2
x + 2 * y <= 2


print(f'-' * 40)
print(f'[計算]')

# 計算（計算ログを出力）
prob.optimize(silent=False)

print(f'-' * 40)
print(f'[出力]')
# テキスト出力
prob.printSolution()

print(f'-' * 32)
# 目的関数値や変数の値を個別に取得
print(f'目的関数値 = {prob.getObjVal()}')
print(f'変数 x の値 = {x.val}')
print(f'変数 y の値 = {y.val}')

print(f'-' * 40)
# -----------------------------------------------------------------------------