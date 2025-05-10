# 九九の計算一覧を出力するプログラム

# 九九の計算一覧
for i in range(1, 10):
    for j in range(1, 10):
        print(f"{i} x {j} = {i * j}")

# ログ出力
print("九九の計算開始")
print("九九の計算終了")


for i in range(1, 5):
    for j in range(1, 5):
        print(i*j)
        
for j in range(10, 5,-1):
    for k in range(9, 5,-1):
        try:
            result = i * k
            print(f"{i} * {k} = {result}")
        except NameError:
            print("Error: i or k is not defined")
        except TypeError:
            print("Error: i or k is not a number")


a = 100
print(a)
