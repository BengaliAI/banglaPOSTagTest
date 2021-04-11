# -*-coding: utf-8 -
'''
    @author:  MD. Nazmuddoha Ansary
'''
from __future__ import print_function
import string 
import numpy as np
from .data import create_features
#---------------------------------------------------------------
# tagger ops
#---------------------------------------------------------------
class BanglaPOSTagger(object):
    def __init__(self,model,label_encoder,dict_vectorizer):
        '''
            the BanglaPOSTagger class is created for generalizing various models 
            args:
                model           :   the model (with weights) that will be used for tagging
                label_encoder   :   the label_encoder that encodes the pos-tag strings
                dict_vectorizer :   the vectorizer that is created through some dictionary features
        '''
        self.model              =   model
        self.label_encoder      =   label_encoder
        self.dict_vectorizer    =   dict_vectorizer
    
    def __tokenize(self):
        '''
            tokenizes a single sentence
        '''
        tokens = []
        # split words
        words = self.__sentence.split(' ')
        words = [x.strip(' ') for x in words] 
        words = [i for i in words if i] 
        # end of sentence
        dict_ = {}
        dict_['।'] = True

        for p in string.punctuation:
            dict_[p] = True

        for word in words:
            # if the last char is a puncuation
            # split the word part and punctuation
            if dict_.get(word[-1]):
                # the word
                tokens.append(word[:-1])
                # the punct
                tokens.append(word[-1])
            else:
                tokens.append(word)
        # again clean check for null chars
        tokens = [token for token in tokens if token]
        # set token
        self.tokens=tokens    

    def __predict_tags(self):
        '''
            creates feature from tokesn
        '''
        # adds features 
        feat=[]
        for index in range(len(self.tokens)):
            feat.append(create_features(self.tokens, index))
        # creates vector
        feat_vec    =   self.dict_vectorizer.transform(feat)
        # predictions
        predictions =   self.model.predict([feat_vec])
        # get encoded tags
        tags = []
        for x in range(len(predictions)):
            tags.append(np.argmax(predictions[x]))
        # get pure tags
        tags  = self.label_encoder.inverse_transform(tags)  

        # tagged_sentence
        self.tagged= list(zip(self.tokens,tags))

    def tag(self,sentence):
        '''
            the public function that tags the sentence
        '''
        self.__sentence=sentence
        # tokenize
        self.__tokenize()
        # predict
        self.__predict_tags()
        return self.tagged