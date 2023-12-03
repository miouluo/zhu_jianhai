import requests
from bs4 import BeautifulSoup
import csv

# 获取新闻列表
def get_news_list(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    news_list = soup.find_all('a', {'target': '_blank'})
    return news_list

# 解析新闻内容
def parse_news_content(news_url):
    response = requests.get(news_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    title = soup.title.string.strip()
    time = soup.find('span', {'class': 'date'}).string.strip()
    content = soup.find('div', {'class': 'article'}).text.strip()
    return title, time, content

# 保存新闻文件
def save_news_file(news_id, title, time, content):
    filename = '{:02d}.txt'.format(news_id)
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(title + '\n')
        f.write(time + '\n')
        f.write(content)

# 统计新闻字数
def count_news_words(news_id, content):
    words = len(content.split())
    return (news_id, words)

# 保存统计结果到CSV文件
def save_statistics(statistics):
    with open('统计.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['序号', '时间', '字数', '标题'])
        writer.writerows(statistics)

# 主函数
def main():
    url = 'https://news.sina.com.cn/'
    news_list = get_news_list(url)
    statistics = []
    news_id = 0
    for news in news_list:
        if '发布时间' in str(news):
            news_url = news.get('href')
            title, time, content = parse_news_content(news_url)
            news_id += 1
            save_news_file(news_id, title, time, content)
            word_count = count_news_words(news_id, content)
            statistics.append(word_count)
            if news_id >= 50:
                break
    save_statistics(statistics)
    print('爬取完成！')

if __name__ == '__main__':
    main()