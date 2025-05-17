def add(x, y):
  """This function adds two numbers together."""
  return x + y

def subtract(x, y):
    return x - y

if __name__ == "__main__":
    num1 = float(input("最初の数字を入力してください: "))
    num2 = float(input("2番目の数字を入力してください: "))
    sum = add(num1, num2)
    print(f"{num1} + {num2} = {sum}")
    difference = subtract(num1, num2)
    print(f"{num1} - {num2} = {difference}")
