# -*- coding: utf-8 -*-

import numpy as np
import io, os

this_directory = os.path.dirname(os.path.realpath(__file__))

def read_tsv(filename):
    """ Lazy corpus reader that yields documents and labels in numpy array. """
    docs, labels = zip(*[line.strip().split('\t') for line in 
                         io.open(filename, 'r')])
    docs = np.array(docs)
    labels = np.array(labels)
    return docs, labels

def sents(infile):
    """ Lazy corpus reader that yields line. """
    with io.open(infile, 'r', encoding='utf8') as fin:
        for line in fin:
            yield line.strip()

class DSLCC:
    """
    Corpus interface for Discriminating Similar Language 
    Corpus Collection (DSLCC), see http://goo.gl/BQBhkW
    
    >>> dslcc = DSLCC(version=1.0)
    >>> for i, j in dslcc.test():
    ...     print j, i
    
    """
    def __init__(self, version):
        self.version = version
        self.files = self.fileids(version)
        
    
    def fileids(self, version):
        files = {1.0: {'train': '/data/DSLCC-v1.0/train-dev/train.txt', 
                       'train-eng': '/data/DSLCC-v1.0/train-dev/train-eng.txt',
               
                       'devel': '/data/DSLCC-v1.0/train-dev/devel.txt',
                       'devel-eng': '/data/DSLCC-v1.0/train-dev/devel-eng.txt',
               
                       'test':'/data/DSLCC-v1.0/test/test.txt',
                       'test-eng':'/data/DSLCC-v1.0/test/test-eng.txt',
                       
                       'gold':'/data/DSLCC-v1.0/gold/test-gold.txt',
                       'gold-eng': '/data/DSLCC-v1.0/gold/test-eng-gold.txt',
                       },
                 
                 2.0: {'train':'/data/DSLCC-v2.0/train-dev/train.txt',
                       'devel':'/data/DSLCC-v2.0/train-dev/devel.txt',
                       'test':'/data/DSLCC-v2.0/test/test.txt',
                       'test-none':'/data/DSLCC-v2.0/test/test-none.txt',
                       'gold':'/data/DSLCC-v2.0/gold/test-gold.txt',
                       'gold-none':'/data/DSLCC-v2.0/gold/test-none-gold.txt',
                       },
                 
                 2.1: {'train':'/data/DSLCC-v2.1/train-dev/train.txt',
                       'devel':'/data/DSLCC-v2.1/train-dev/devel.txt',
                       }
                 }
        return files[version]
    
    def data(self, option):
        possible = ['train', 'devel', 'test', 'gold']
        if self.version == 1.0:
            possible += ['test-eng', 'gold-eng']
        elif self.version == 2.0:
            possible += ['test-none', 'gold-none']
        assert option in possible, \
        "Make sure option is one of these: %s " % str(possible)
        
        filename = this_directory + self.files[option]
        
        if option in ['test', 'test-none', 'test-eng']:
            return np.array(list(sents(filename)))
        
        return read_tsv(filename)

''' 
corpus = DSLCC(version=2.0)
train_docs, train_labels =  corpus.data('train')
dev_docs, dev_labels =  corpus.data('devel')
test_docs, gold_labels =  corpus.data('gold')
test_none_docs, gold_none_labels =  corpus.data('gold')
test_docs = corpus.data('test')
'''