
lst1 = [i for i in range(1, 6)]
lst2 = []
lst3 = []
lst4 = []
while len(lst2) < 5:
    new = input('请输入商品的名称：')
    lst2.append(new)
d = {key: value for key, value in zip(lst1, lst2)}
for key, value in d.items():
    print(key, value)
while 1:
    num = int(input('请输入要购买的商品编号：'))
    if 1 <= num <= 5:

        lst3.append(num)
        lst4.append(d.get(num))
        print('商品已成功添加到购物车')
    elif num == 0:
        d2 = {key: value for key, value in zip(lst3, lst4)}
        print('--------------------------')
        print('您购物车里已选择的商品为:')
        for key, value in d2.items():
            print(key, value)
        break
    else:
        print('该商品不存在')
