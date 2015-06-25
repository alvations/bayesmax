# -*- coding: utf-8 -*-

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB, GaussianNB 

def train(train_docs, train_labels, min_n=5, max_n=5,
          classifier_choice=MultinomialNB):
    ngram_vectorizer = CountVectorizer(analyzer='char',
                                       ngram_range=(min_n, max_n), min_df=1)
    trainset = ngram_vectorizer.fit_transform(train_docs)
    tags = train_labels
    classifier = classifier_choice()
    classifier.fit(trainset, tags)
    return ngram_vectorizer, classifier

def test(test_docs, vectorizer, classifier):
    testset = vectorizer.transform(test_docs)
    results = classifier.predict(testset)
    return results

