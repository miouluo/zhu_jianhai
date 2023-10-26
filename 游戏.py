# 导入pygame模块
import pygame

# 调用init方法,加载pygame内所有游戏模块，并初始化
pygame.init()

# 编写游戏代码
# print('游戏的代码...')

# 创建游戏的窗口 480 700
scree = pygame.display.set_mode((480, 700))

# 绘制背景图像
# （1）加载图像数据
bg = pygame.image.load("./images/background.png")

# （2）blit 绘制图像
scree.blit(bg, (0, 0))

# （3）update 更新屏幕显示,不调用update方法无法查看背景图像
# pygame.display.update()

# 创建英雄飞机
hero = pygame.image.load("./images/me1.png")
scree.blit(hero, (200, 500))

# 可以在绘制完所有图像后统一更新显示图像
pygame.display.update()

# 创建时钟对象，刷新页面
clock = pygame.time.Clock()

# （1）定义一个rect记录飞机的初始位置
hero_rect = pygame.Rect(200, 500, 102, 126)

# 建立一个无限循环，使游戏窗口不消失

while True:

    # 在游戏循环内部调用时钟对象，可以指定循环内部代码执行的频率
    clock.tick(60)

    # 捕获事件，get()方法返回一个列表
    # event_list = pygame.event.get()

    # exit()方法直接退出当前程序

    # 监听事件
    for event in pygame.event.get():

        # 判断事件类型是否为退出事件
        if event.type == pygame.QUIT:
            print("游戏退出...")

            # 调用quit()方法卸载pygame模块所有的模块
            pygame.quit()

            # exit()
            exit()

    # # 判断event_list中是否有事件，避免出现空列表，以查看更加详细的操作信息
    # if len(event_list) > 0:
    #     print(event_list)

    # (2)修改飞机的位置
    hero_rect.y -= 1

    # 判断飞机的y值, 如果飞机的初始位置y值加上飞机的原始高度y值小于0，则证明飞机尾部已全飞出游戏屏幕
    if hero_rect.y <= 0:
        hero_rect.y = 700

    # (3)调用blit方法绘制图像
    scree.blit(bg, (0, 0))
    scree.blit(hero, hero_rect)

    # （4）调用update方法更新显示
    pygame.display.update()

    pass

# 调用quit方法释放内存，游戏结束，卸载所有pygame模块
pygame.quit()

# （x，y）表示左上角原点位置，  （width，height）表示矩形区域大小， pygame.Rect用于描述矩形区域
