from calculator import Calculator

def main():
    calc = Calculator()
    
    # 数値を入力
    num1 = int(input("1つ目の数値を入力してください: "))
    num2 = int(input("2つ目の数値を入力してください: "))
    
    # 計算を実行
    calc.add(num1, num2)
    calc.subtract(num1, num2)
    calc.multiply(num1, num2)
    calc.divide(num1, num2)
    
    # 計算結果を表示
    print(f"\n計算結果:")
    print(f"足し算: {calc.get_add_result()}")
    print(f"引き算: {calc.get_subtract_result()}")
    print(f"掛け算: {calc.get_multiply_result()}")
    print(f"割り算: {calc.get_divide_result()}")

if __name__ == "__main__":
    main()
