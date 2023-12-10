from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction import DictVectorizer
from sklearn.feature_extraction.text import CountVectorizer


# sklearn数据集使用
def datasets_deom():
    iris = load_iris()
    print('鸢尾花数据集：\n', iris)
    print("查看数据集描述：\n", iris["DESCR"])
    print("查看特征值的名字：\n", iris.feature_names)
    print("查看特征值：\n", iris.data, iris.data.shape)

    # 数据集划分
    x_train, x_text, y_train, y_text = train_test_split(iris.data, iris.target, test_size=0.2, random_state=22)
    print("训练集特征值：\n", x_train, x_train.shape)

    return None


# 字典特征抽取
def dict_demo():
    data = (
        {'city': '北京', 'temperature': 100}, {'city': '上海', 'temperature': 60}, {'city': '深圳', 'temperature': 30})
    # 实例化转换器类
    transfer = DictVectorizer(sparse=False)
    # 调用fit_transform()
    data_new = transfer.fit_transform(data)
    print("data_new:\n", data_new)
    print("特征名字：\n", transfer.get_feature_names_out())

    return None


def count_demo():
    # 文本特征获取
    data = ["life is short,i like like python", "life is too long,i dislike python"]
    # 实例化转换器类
    transfer = CountVectorizer()  # 统计样本特征值个数
    # 调用fit_transform()
    data_new = transfer.fit_transform(data)
    print("data_new:\n", data_new.toarray())  # .toarray()变为二维矩阵
    print("特征名字：\n", transfer.get_feature_names_out())


if __name__ == "__main__":
    # sklearn数据集使用
    # datasets_deom()
    # 字典特征抽取
    # dict_demo()
    # 文本特征获取
    count_demo()
