from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.tree import DecisionTreeClassifier, export_graphviz


def nb_news():
    # 用朴素贝叶斯算法对新闻进行分类

    # 获取数据
    news = fetch_20newsgroups(subset="all")

    # 划分数据集
    x_train, x_test, y_train, y_test = train_test_split(news.data, news.target)

    # 特征工程：文本特征抽取-tfidf
    transfer = TfidfVectorizer()
    x_train = transfer.fit_transform(x_train)
    x_test = transfer.transform(x_test)

    # 朴素贝叶斯算法预估器流程
    estimator = MultinomialNB()
    estimator.fit(x_train, y_train)

    # 模型评估
    # 直接比对真实值和预测值
    y_predict = estimator.predict(x_test)
    print("y_predict:\n", y_predict)
    print("直接比对真实值和预测值:\n", y_test == y_predict)

    # 计算准确率
    score = estimator.score(x_test, y_test)
    print("准确率为：\n", score)

    return None


def decision_iris():
    # 用决策树对鸢尾花进行分类

    # 获取数据集
    iris = load_iris()

    # 划分数据集
    x_train, x_test, y_train, y_test = train_test_split(iris.data, iris.target, random_state=22)

    # 决策树预估器
    estimator = DecisionTreeClassifier(criterion="entropy")
    estimator.fit(x_train, y_train)

    # 模型评估
    # 直接比对真实值和预测值
    y_predict = estimator.predict(x_test)
    print("y_predict:\n", y_predict)
    print("直接比对真实值和预测值:\n", y_test == y_predict)

    # 计算准确率
    score = estimator.score(x_test, y_test)
    print("准确率为：\n", score)

    # 可视化决策树
    export_graphviz(estimator, out_file="iris_tree.dot", feature_names=iris.feature_names)

    return None


if __name__ == "__main__":
    # 用朴素贝叶斯算法对新闻进行分类
    # nb_news()
    # 用决策树对鸢尾花进行分类
    decision_iris()
