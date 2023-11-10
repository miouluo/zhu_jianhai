def count_yanghui():
    """计算每一行杨辉三角数"""
    a=[1]
    while True:
        yield a
        a=[sum(i) for i in zip([0]+a,a+[0])]#杨辉三角算法
def getPascalTriangle(max_num):
    """由用户决定打印几行杨辉三角"""
    n=0
    for x in count_yanghui():
        print(x)#以列表形式输出每一行杨辉三角数,即print(a)
        n+=1
        if n==int(max_num):
            break
if __name__=="__main__":
    n=input("请输入需要打印的杨辉三角行数：")
    getPascalTriangle(n)
