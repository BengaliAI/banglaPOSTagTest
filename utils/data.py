# -*-coding: utf-8 -
'''
    @author:  MD. Nazmuddoha Ansary
'''
from __future__ import print_function
#---------------------------------------------------------------
# imports
#---------------------------------------------------------------
import pandas as pd
from tqdm.auto import tqdm
tqdm.pandas()
#---------------------------------------------------------------
# tag utils
#---------------------------------------------------------------

def untag(tagged_sentence):
    '''
        simply returns the list of words in a senteces (excludes tags from a tagged sentence)
    '''
    return [w for w, _ in tagged_sentence]

def create_features(sentence_terms, index):
    '''
        creates features for the tagged sentences
        args:
            sentence_terms  :   simply the list of words in a sentence
            index           :   the index of the term to create feature for
    '''
    term = sentence_terms[index]
    return {
        'nb_terms': len(sentence_terms),
        'term': term,
        'is_first': index == 0,
        'is_last': index == len(sentence_terms) - 1,
        'prefix-1': term[0],
        'prefix-2': term[:2],
        'prefix-3': term[:3],
        'suffix-1': term[-1],
        'suffix-2': term[-2:],
        'suffix-3': term[-3:],
        'prev_word': '' if index == 0 else sentence_terms[index - 1],
        'next_word': '' if index == len(sentence_terms) - 1 else sentence_terms[index + 1]
    }   


def transform_to_dataset(tagged_sentences):
    ''' 
        converts tagged sentences to features and classes
    '''
    X, y = [], []

    for pos_tags in tqdm(tagged_sentences):
        for index, (term, class_) in enumerate(pos_tags):
            # Add basic NLP features for each sentence term
            X.append(create_features(untag(pos_tags), index))
            y.append(class_)
    return X, y
#---------------------------------------------------------------
# dataset utils
#---------------------------------------------------------------
def split_data_and_label(line,eda=False):
    '''
        returns two lists  (words,tags) as a tuple 
        args:
            line : a line that contains labeled data where data and pos-tag are separated by \\
            eda  : use eda true for creating the eda dataframe
    '''
    # holder
    words    = []
    tags     = []
    sentence = []
    # split line by space
    line = line.split(' ')
    # iterate elements
    for x in line:
        # avoid empty data
        if x != '':
            if "\n" in x:
                x=x.replace("\n",'')
            # split data
            x = x.split('\\')
            # constuct word and tag
            word=x[0]
            tag =x[-1]
            if eda:
                words.append(word)
                tags.append(tag)
            else:
                # this is easier for training
                sentence.append(tuple([word,tag]))
    if eda:    
        return words,tags
    else:
        return sentence    


def textfile_to_dataset(text_file,eda=False):
    '''
        converts the labeled data into a dataset that is intended. 
            If
                we want to do eda then, the dataset is in form of a dataframe 
            else
                the dataset is formatted as a list of sentences where each sentence holds (word,tag) tuple
                NOTE:this is not necessary but simply easier to use  
                
                
                Within tagged_sentences dataset format the feature construction is as follows : 
                
                {
                    'nb_terms'  : number of terms in the sentence,
                    'term'      : the specific term,
                    'is_first'  : True if the term is the first one in sentence,
                    'is_last'   : True if the term is the last ine in sentence,
                    'prefix-1'  : term[0],
                    'prefix-2'  : term[:2],
                    'prefix-3'  : term[:3],
                    'suffix-1'  : term[-1],
                    'suffix-2'  : term[-2:],
                    'suffix-3'  : term[-3:],
                    'prev_word' : the previous word,
                    'next_word' : the next word
                }   

                For Non-EDA mode: 
                    the return parameters are X,y where X is the features as formatted above and y is the class
        args:
            text_file   :   the text file that contains the labeled data 
            eda         : use eda true for creating the eda dataframe

    '''
    # read the tagged_data
    with open(text_file, encoding='utf8') as f:
        # read lines
        texts=f.readlines()
    
    if eda:
        # iterate lines
        words=[]
        tags=[]
        for line in tqdm(texts):
            _words,_tags=split_data_and_label(line,eda=True)
            words+=_words
            tags+=_tags
        # dataframe
        df=pd.DataFrame({"word":words,"tag":tags})
        return df 
    else:
        sentences=[]
        for line in tqdm(texts):
            sentences.append(split_data_and_label(line,eda=False))
        X,y=transform_to_dataset(sentences)
        return X,y 
