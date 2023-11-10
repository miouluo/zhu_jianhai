# 根据需求输入单词，统计出现的次数，并输出结果。然后，循环会再次开始，等待下一次输入，如果不需要，则按q退出程序
# 统计一个 TXT 中英文单词出现的次数
# 打开文件并读取内容
with open('C:\\Users\\W\\Desktop\\Python编程技术\\code\\file.txt', 'r') as file:
    text = file.read()
# 将文本内容分割成单词，以空格和换行符合为分隔符
words = text.split()
# 初始化一个空字典用于存储单词计数
word_count = {}
# 遍历单词列表并统计单词出现次数
for word in words:
    # 去除标点符合
    word = word.strip('.,?()[]{}"\'')
    # 如有需要，可以转换成小写
    # word=word.strip('.,?()[]{}"\'').lower()
    if word:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
# 无限循环直到输入 'q' 退出
while True:
    # 输入要统计的单词或退出字符
    input_word = input("请输入要统计的单词（输入 q 退出）: ")
    # 如果输入为退出字符，则退出循环
    if input_word == 'q':
        break
    # 获取输入单词的出现次数
    count = word_count.get(input_word, 0)
    # 输出结果
    print(f"{input_word} 出现的次数为: {count}")