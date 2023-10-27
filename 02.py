import matplotlib.pyplot as plt
import numpy as np
x1 = np.linspace(0, 50, 100)
x2 = np.linspace(0, 50, 100)

# 创建网格点坐标矩阵
X1, X2 = np.meshgrid(x1, x2)
# plt.plot((-3 / 5) * x2, (-5 / 3) * x1, 'black', label='Z=50*x1+30*x2')
plt.grid(True, linestyle=':', linewidth=0.8)

a1 = 2-x1
a2 = x1/2
a3 = -2*x1
a5 = np.full_like(x1, 0)
# plt.plot(x1, a4, 'black', label=' max-Z =40*x1+30*x2')
plt.plot(x1, a1, 'r', label='x1 + x2 >= 2')
plt.plot(x1, a2, 'b', label='x1 - x2 * 2 <= 0')
plt.plot(x1, a3, 'black', label='min-Z=2 * x1 + x2')

plt.plot(x1, a5, 'black')


# 绘制可行域
x2_min = np.maximum(0, np.minimum(2-x1,  -x1/2))
plt.fill_between(x1, 0, x2_min, where=(x2_min >= 0),
                 color='y', alpha=0.6, label='yu')

# 设置x轴和y轴的范围
plt.xlim(0, 10)
plt.ylim(-10, 20)
# 设置坐标轴标签和标题
plt.xlabel('x1')
plt.ylabel('x2')

# 设置图例
plt.legend()
# 显示图形
plt.show()
