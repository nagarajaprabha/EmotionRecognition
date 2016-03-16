# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 09:36:39 2016

@author: Nagaraja
"""

import arff,numpy as np , pandas as pd 
from sklearn.ensemble import RandomForestClassifier

dataset = "";
data = "";


def loadFile():
    #TODO add the logic to loop through list of generated arff files;
    dataset = arff.load(open('input\emo_large.arff','r'));
    print("*******************");
    #print(dataset)
    
    #dataset contains two arrays namely 'attributes' and 'data'.'data' is 
    #  a multidimensional array..
    data=np.array(dataset['data']);
    
    #Output log;accessing data elements
    #print(data[0][1]);
    
    #accessing attributes
 #   print(len(dataset['attributes']));
    parse(data);


def parse(data):
    #remove string element from the data array as first element is name
    #TODO either we can remove the attribute 'name' from generating the 
    #arff file itself.
   
   # print(data);
   
#(10, 6555)   
    print(data.shape);
    
    print(data[0:2,1:3]);
    
    print(data[0:2, 0]);
    
    print(data[0:3, 6554]);
    #data=np.array(dataset['data']);
    data = np.delete(data,[0][0])
    #print(data[0]);
    print(data);
    #TODO Pass the parsed input data elements to the algorithm

loadFile();
forest = RandomForestClassifier(n_estimators = 100);
#print(data[0:3,::]);
