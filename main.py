from calculator import Calculator

def main():
    calc = Calculator()
    
    # 数値を入力
    num1 = float(input("1つ目の数値を入力してください: "))
    num2 = float(input("2つ目の数値を入力してください: "))
    
    # 計算結果を表示
    print(f"\n計算結果:")
    print(f"足し算: {calc.add(num1, num2)}")
    print(f"引き算: {calc.subtract(num1, num2)}")
    print(f"掛け算: {calc.multiply(num1, num2)}")
    print(f"割り算: {calc.divide(num1, num2)}")

if __name__ == "__main__":
    main()
