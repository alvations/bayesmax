# -*- coding: utf-8 -*-

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

def train(train_docs, train_labels, n=5):
    ngram_vectorizer = CountVectorizer(analyzer='char',
                                       ngram_range=(n, n), min_df=1)
    trainset = ngram_vectorizer.fit_transform(train_docs)
    tags = train_labels
    classifier = MultinomialNB()
    classifier.fit(trainset, tags)
    return ngram_vectorizer, classifier

def test(test_docs, vectorizer, classifier):
    testset = vectorizer.transform(test_docs)
    results = classifier.predict(testset)
    return results
