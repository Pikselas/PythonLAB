from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC

class Classifier:
    def __init__(self , type : str):
        self.clsf = None
        if type == "KNN":
            self.clsf = KNeighborsClassifier(1)
        elif type == "MLP":
            self.clsf = MLPClassifier(max_iter=1000)
        elif type == "SVM":
            self.clsf = SVC()
        elif type == "RF":
            self.clsf = RandomForestClassifier(max_depth=2, random_state=0)
    def Train(self , data , label):
        self.clsf.fit(data , label)
    def Classify(self , test_matrix):
        return self.clsf.predict(test_matrix)

class ClassificationSystem:
    def __init__(self , scikit_dataset , testsize):
        self.Types = scikit_dataset.target_names
        self.TrainableData , self.TestableData , self.TrainableLabel , ignoreableLabel = train_test_split(scikit_dataset.data , scikit_dataset.target , test_size = testsize)
    def Classify(self , classifier : Classifier):
        classifier.Train(self.TrainableData , self.TrainableLabel)
        return [ self.Types[indx] for indx in classifier.Classify(self.TestableData)]


cs = ClassificationSystem(datasets.load_breast_cancer() , 0.30)

print(cs.Classify(Classifier("KNN")))
print(cs.Classify(Classifier("MLP")))
print(cs.Classify(Classifier("SVM")))
print(cs.Classify(Classifier("RF")))