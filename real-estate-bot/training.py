from sklearn.naive_bayes import GaussianNB
import pickle5 as cPickle

def train_classifier(features,y,clf):
    with open('vectorizer.pkl', 'rb') as f:
        vectorizer = cPickle.load(f)

    vectors =vectorizer.transform(features)

    clf.partial_fit(vectors.toarray(), y, classes=[0,1])





