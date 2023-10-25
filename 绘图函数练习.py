import matplotlib.pyplot as plt
import numpy as np


def yyplot():
    plt.rcParams['font.sans-serif'] = 'SimHei'
    plt.rcParams['axes.unicode_minus'] = False
    fig = plt.figure(figsize=(6, 4))
    ax1 = fig.add_subplot(111)
    ax1.bar(x1, y1, color=['#E0FFFF', '#76EEC6', '#66d88e', '#66CDAA', '#8FBC8F'])
    ax1.set_ylabel('销量', fontsize=10)
    ax1.set_xlabel('年份', fontsize=10)
    ax1.set_title(title, fontsize=15)
    ax2 = ax1.twinx()
    ax2.plot(x2, y2, '#006400')
    ax2.set_ylabel(ylabel, fontsize=15)
    plt.xticks(x1, x1, fontsize=10)
    plt.show()


