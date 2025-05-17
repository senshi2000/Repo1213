a=10
b=20

# 足し算をして

# 結果を表示する関数
def add(a, b):
    """足し算をして結果を表示する関数"""
    result = a + b
    return result

# 引き算をして結果を表示する関数
def subtract(a, b):
    """引き算をして結果を表示する関数"""
    result = a - b
    return result

res = add(a, b)
print(f"{a} + {b} = {res}")