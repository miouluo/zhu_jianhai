

try:
    a = float(input('请输入数字a：'))
    b = float(input('请输入数字b：'))
    if a < 0:
        raise ValueError('a值应该大于等于0')
    assert 'b != 5', 'b值不可为5'
    result = a / (b - 5)
    print("结果为：", result)

except ValueError as e:
    print("error：", e)
except AssertionError as e:
    print("AssertionError：", e)
except Exception as e:
    print("Exception：", e)




'''
try:
    a = float(input("请输入a的值："))
    if a < 0:
        raise ValueError("a值应该大于0")
    b = float(input("请输入b的值："))
    assert b != 5, "b值不可为5"
    result = a / (b - 5)
    print("结果为：", result)
except ValueError as e:
    print("error：", e)
except AssertionError as e:
    print("AssertionError：", e)
except Exception as e:
    print("Exception：", e)
'''