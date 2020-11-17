import numpy
from . import dataset
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB, BernoulliNB, CategoricalNB, MultinomialNB
from sklearn.linear_model import LogisticRegression, Perceptron
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.mixture import GaussianMixture, BayesianGaussianMixture
from sklearn.neural_network import BernoulliRBM, MLPClassifier, MLPRegressor


def test_each_line():
    predicts = {0: [], 1: []}
    for irow in range(0, dataset.df.shape[0]):
        line = dataset.xarr[irow, :]
        val = dataset.Y.iat[irow]
        lline = line.reshape(1, -1)
        pr = dataset.gnb.predict(lline)
        predicts[val].append(pr)
    predicts[0].sort()
    predicts[1].sort()
    hist0 = numpy.histogram(predicts[0], bins=10)
    hist1 = numpy.histogram(predicts[1], bins=10)
    print("predicts0", hist0, len(predicts[0]))
    print("predicts1", hist1, len(predicts[1]))
    print("predicts", dataset.gnb.class_count_)


def tts():
    locx = dataset.df.loc[:, dataset.allx]
    locx0 = locx- locx.min()
    locx01 = locx0/locx0.max()
    X_train, X_test, y_train, y_test = train_test_split(locx01, dataset.yarr, test_size=0.4, random_state=None)
    gnb = GaussianNB()
    #gnb = BernoulliNB()
    #gnb = CategoricalNB()
    gnb = LogisticRegression() #score aroun6 0.89 con locx, locx0 y locx01
    #gnb = Perceptron()
    #gnb = GaussianMixture()
    #gnb = BayesianGaussianMixture()
    gnb = MLPClassifier()
    gnb = MultinomialNB()
    #gnb = MLPRegressor()
    y_pred = gnb.fit(X_train, y_train).predict(X_test)
    print("Number of mislabeled points out of a total %d points : %d"
               % (X_test.shape[0], (y_test != y_pred).sum()))
    assert 0, gnb.score(X_test, y_test)


def test_predict_Y():
    dct = {'age': 45, 'job': 'admin.', 'marital': 'married', 'education': 'unknown', 'default': True,
    'balance': 50, 'housing': False, 'loan': False, 'contact': 'unknown', 'day': 2, 'month': 'may',
    'duration': 5, 'campaign': 6, 'pdays': 6, 'previous': 3, 'poutcome': "success"}
    prediction = dataset.predict_from_dict(dct)
    assert 0, prediction


#tts()
#test_each_line()
test_predict_Y()