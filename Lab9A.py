def allMath(input1, input2):
    add = input1 + input2
    sub = input1 - input2
    mul = input1 * input2
    pow_result = input1 ** input2
    if input2 == 0:
        div = None
        floordiv = None
        mod = None
    else:
        div = input1 / input2
        floordiv = input1 // input2
        mod = input1 % input2
    return (add, sub, mul, div, floordiv, mod, pow_result)

input1 = int(input("Enter your first number: "))
input2 = int(input("Enter your second number: "))
result = allMath(input1, input2)
print(f"Your resulting tuple is {result}")