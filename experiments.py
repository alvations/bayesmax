# -*- coding: utf-8 -*-

import cPickle as pickle
import os, time
import re

from bayesmax.corpus import DSLCC
from bayesmax import bayesline
from bayesmax.evaluate import breakdown_evaluation

def test_MNB_5grams(version=2.0):
    print '''
    ###########################################################################
    # Bayesline.py : Multinomial Naive Bayes Classifier with 5-grams features.
    ###########################################################################
    '''
    dslcc = DSLCC(version)
    
    vectorizer_file = 'bayesline-dslcc2.vectorizer'
    classifier_file = "bayesline-dslcc2.clf"
    
    if os.path.exists(vectorizer_file) and os.path.exists(classifier_file):
        print 'Loading...', 
        start = time.time()
        # Loads vectorizer and classifier.
        with open(vectorizer_file, "rb") as fin:
            ngram_vectorizer = pickle.load(fin)
        with open(classifier_file, "rb") as fin:
            classifier = pickle.load(fin)
        print 'took', time.time() - start, 'secs'
    else: # Trains vectorizer and classifer
        print 'Training...', 
        start = time.time()
        train_docs, train_labels = dslcc.data('train')
        ngram_vectorizer, classifier = bayesline.train(train_docs, train_labels)
        # Pickle dump
        with open(vectorizer_file, "wb") as fout:
            pickle.dump(ngram_vectorizer, fout)
        with open(classifier_file, "wb") as fout:
            pickle.dump(classifier, fout)
        print 'took', time.time() - start, 'secs' 
    
    print '''
    ####################################################################
    # Bayesline.py :Evaluating on dev set
    ####################################################################'''
    
    print 'Predicting...',
    start = time.time()
    dev_docs, dev_labels = dslcc.data('devel')
    results = bayesline.test(dev_docs, ngram_vectorizer, classifier)
    print 'took', time.time() - start, 'secs'
    
    print 'Evaluating...\n'
    breakdown_evaluation(results, dev_labels)
    
    print '''
    ####################################################################
    # Evaluating on test set
    ####################################################################'''
    
    print 'Predicting...',
    start = time.time()
    test_docs = dslcc.data('test')
    results = bayesline.test(test_docs, ngram_vectorizer, classifier)
    print 'took', time.time() - start, 'secs' 
    
    print 'Evaluating...\n'
    _, gold_labels = dslcc.data('gold')
    breakdown_evaluation(results, gold_labels)
    
    
    print '''
    ####################################################################
    # Bayesline.py :Evaluating on test-none set
    ####################################################################'''
    
    print 'Predicting...',
    start = time.time()
    test_docs = dslcc.data('test-none')
    results = bayesline.test(test_docs, ngram_vectorizer, classifier)
    print 'took', time.time() - start, 'secs' 
    
    print 'Evaluating...\n'
    _, gold_labels = dslcc.data('gold-none')
    breakdown_evaluation(results, gold_labels)
    
    print '#######################################################'

    print'''
    ####################################################################
    # Bayesline.py : Retraining/Reloading classifier with blinded NEs
    ####################################################################'''


    vectorizer_none_file = 'bayesline-dslcc2-none.vectorizer'
    classifier_none_file = "bayesline-dslcc2-none.clf"
    
    if os.path.exists(vectorizer_none_file) and os.path.exists(classifier_none_file):
        print 'Loading...', 
        start = time.time()
        # Loads vectorizer and classifier.
        with open(vectorizer_file, "rb") as fin:
            ngram_vectorizer_none = pickle.load(fin)
        with open(classifier_file, "rb") as fin:
            classifier_none = pickle.load(fin)
        print 'took', time.time() - start, 'secs'
    else: # Trains vectorizer and classifer
        print 'Training...', 
        start = time.time()
        train_docs, train_labels = dslcc.data('train', blindne=True)
        ngram_vectorizer_none, classifier_none = bayesline.train(train_docs, train_labels)
        # Pickle dump
        with open(vectorizer_file, "wb") as fout:
            pickle.dump(ngram_vectorizer_none, fout)
        with open(classifier_file, "wb") as fout:
            pickle.dump(classifier_none, fout)
        print 'took', time.time() - start, 'secs' 

    ####################################################################
    # Evaluating on test-none set with new classifier trained on blinded NE
    ####################################################################'''
    
    print 'Predicting...',
    start = time.time()
    test_docs = dslcc.data('test-none')
    results = bayesline.test(test_docs, ngram_vectorizer_none, classifier_none)
    print 'took', time.time() - start, 'secs' 
    
    print 'Evaluating...\n'
    _, gold_labels = dslcc.data('gold-none')
    breakdown_evaluation(results, gold_labels)
    
    print '#######################################################'
    

def test_MNB_Ngram(min_n, max_n, version=2.0):
    dslcc = DSLCC(version)
    print 'Training n=('+','.join([str(min_n), str(max_n)])+')...', 
    start = time.time()
    train_docs, train_labels = dslcc.data('train')
    ngram_vectorizer, classifier = bayesline.train(train_docs, train_labels, 
                                                   min_n, max_n)
    print 'took', time.time() - start, 'secs' 
    
    print 'Predicting...',
    start = time.time()
    test_docs = dslcc.data('test')
    results = bayesline.test(test_docs, ngram_vectorizer, classifier)
    print 'took', time.time() - start, 'secs' 
    
    print 'Evaluating...\n'
    _, gold_labels = dslcc.data('gold')
    print breakdown_evaluation(results, gold_labels, human_readable=False,
                         overall_only=True)
    print '#######################################################'

def test_MNB_126grams(version=2.0):
    for i in range(1,7):
        test_MNB_Ngram(i,i)
        if i != 1:
            test_MNB_Ngram(1,i)
        
    
#test_MNB_5grams()

test_MNB_Ngram(1,6)

'''
Training n=(5,6)... took 138.935706854 secs
Predicting... took 4.82505702972 secs
Evaluating...

0.940142857143
'''