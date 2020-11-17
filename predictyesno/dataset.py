import pandas as pd, numpy, os, logging, time, json
from joblib import dump, load
from sklearn import linear_model
from sklearn.naive_bayes import GaussianNB, CategoricalNB, MultinomialNB
from sklearn.datasets import load_iris
from sklearn.neural_network import BernoulliRBM, MLPClassifier, MLPRegressor
from sklearn.model_selection import train_test_split
from .  import forms
full_classifier = None

def testmodel(model, *args, **kwargs):
    """Test the chosen model
    Parameters:
    model: class (not instance)"""
    global full_classifier
    toret = {}

    if full_classifier is None:
        starttime = time.time()
        if TESTING:
            logging.info(f"Testing the chosen model{model} (id {id(model)}) with arguments {args} and keywords arguments {kwargs}")
            test_classifier = model(*args, **kwargs)
            X_train, X_test, y_train, y_test = train_test_split(X01numpy, Yarr, test_size=0.4, random_state=None)
            y_pred = test_classifier.fit(X_train, y_train).predict(X_test)
            truthcol = y_test != y_pred
            logging.info("Number of mislabeled points out of a total %d points : %d"
                       % (X_test.shape[0], (truthcol).sum()))
            toret["Number of mislabeled points"] = "%d out of %d"%((y_test != y_pred).sum(), X_test.shape[0])
            score = test_classifier.score(X_test, y_test)
            logging.info(f"Score {score}")
            whr = numpy.where(truthcol)
            print("firstr", whr, whr[0][0])
            first = X.iloc[whr[0][0]]
            fdct = first.to_dict()
            print("jsl", fdct)
            print("first", first, "firsto")
            toret["score"] = score
        #return a classifier trained with all the samples
        if os.path.exists("trained_data.dat") and not FORCE_RETRAIN:
            full_classifier = load("trained_data.dat")
            toret["loaded"] = "data loaded from trained_data.dat"
        else:
            logging.info("Training...")
            full_classifier = model(*args, **kwargs)
            full_classifier.fit(X01numpy, Yarr)
            dump(full_classifier, "trained_data.dat")
            elpstime = time.time() - starttime
            logging.info("Training finished and dumped to trained_data.dat")
            toret["Elapsed time"] = elpstime
        return toret
    else:
        #logging.info("The system had already been trained")
        return {"already trained": "The system had already been trained"}

#Read the csv field
df = pd.read_csv(os.path.join(os.path.dirname(__file__), "bank-full.csv"), sep=";")
#Fields: if int, it admits any int, if a list, it admits any of the values from the list (later they will be
# discretized to the 0-based position of the value in the list)

def field_encoder(nfield, value):
    """Function to encode the categoric values to numbers.
    this function is not apoted in the below code block
    because that block is time-consuming and we don't
    want to add overhead to it"""
    field = forms.fields[nfield]
    #print("fenc", nfield, value, field)
    if field is int:
        return value
    else:
        if value is True:
            value = "yes"
        elif value is False:
            value = "no"
        return field.index(value)

#Encode the categoric values to numbers
columns = list(df.columns)
for (nfield, field) in forms.fields.items():
    col = df[nfield]
    if field is int:
        pass
    else:
        colidx = columns.index(nfield)
        for irow in range(0, df.shape[0]):
            df.iat[irow, colidx] = field.index(df.iat[irow, colidx])

def predict_from_dict(dct):
    for key in forms.fields.keys():
        if dct.get(key) is None:
            dct[key] = 0
    X_test = numpy.fromiter((field_encoder(name, dct[name]) for name in allx), dtype=int).reshape((1, -1))

    #Normalize X in the same way done for the training set... this including using the same sustraends and divisors
    X0_test = X_test - Xminnumpy
    X01_test = X0_test / X0maxnumpy
    testmodel(MLPClassifier, max_iter=MAX_ITER, hidden_layer_sizes=HIDDEN_LAYER_SIZES)
    prediction = full_classifier.predict(X01_test)
    return prediction[0]

#Converts the data to a table where the values of each column are normalized from 0 to 1
allx = ("age", "job", "marital", "education", "default", "balance", "housing", "loan",
    "contact", "day", "month", "duration", "campaign", "pdays", "previous", "poutcome")
X = df.loc[:, allx]
Xnumpy = X.to_numpy()
Xminnumpy = Xnumpy.min(0)
X0numpy = Xnumpy - Xminnumpy
X0maxnumpy = X0numpy.max(0)
X01numpy = X0numpy / X0maxnumpy
Y = df.loc[:, "y"]
Yarr = Y.to_numpy(dtype=float)

#Test the accuracy of the chosen model against a part (40%) the sample dataset
#For production you can use max_iter=500, it is a little (a little) more exact
#but takes 2.5 times to start than 200
MAX_ITER = 500
HIDDEN_LAYER_SIZES=(100,)
TESTING = True
FORCE_RETRAIN = False
#now the testmodel function is called when the model is required, as it is persisted into a file,
#and all the trainings are doing in a development environment
#testmodel(MLPClassifier, max_iter=MAX_ITER, hidden_layer_sizes=HIDDEN_LAYER_SIZES)
