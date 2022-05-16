
from sklearn.cluster import KMeans
from sklearn import datasets

def ApplyK_Means(data_set , clusterCount):
    return KMeans(clusterCount).fit_predict(data_set)

if __name__ == "__main__":
    iris = datasets.load_iris()
    for indx in ApplyK_Means(iris.data , 3):
        print(iris.target_names[indx])