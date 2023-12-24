from sklearn.feature_selection import VarianceThreshold
import pandas as pd
from scipy.stats import pearsonr
from sklearn.decomposition import PCA


def variance_demo():
    # 过滤低方差特征
    # 获取数据
    data = pd.read_csv("factor_returns.csv")
    data = data.iloc[:, 1:-2]
    print("data:\n", data)

    # 实例化一个转换器类
    transfer = VarianceThreshold(threshold=10)

    # 调用fit_transform
    data_new = transfer.fit_transform(data)
    print("data_new:\n", data_new, data_new.shape)

    # 计算某两个变量之间的相关系数
    r1 = pearsonr(data["pe_ratio"], data["pb_ratio"])
    print("相关系数：\n", r1)
    r2 = pearsonr(data['revenue'], data['total_expense'])
    print("revenue与total_expense之间的相关性：\n", r2)

    return None


def pca_demo():
    # PCA降维
    data = [[2, 8, 4, 5], [6, 3, 0, 8], [5, 4, 9, 1]]

    # 实例化一个转换器类
    transfer = PCA(n_components=0.95)

    # 调用fit_transform
    data_new = transfer.fit_transform(data)
    print("data_new:\n", data_new)
    return None


if __name__ == "__main__":
    # 低方差特征过滤
    # variance_demo()
    # PCA降维
    pca_demo()