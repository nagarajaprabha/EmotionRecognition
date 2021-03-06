# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 09:36:39 2016

@author: Nagaraja
"""

import arff,numpy as np , pandas as pd
from sklearn.ensemble import RandomForestClassifier

trainingDataset = "";
testDataset = "";
trainingData = "";
testData="";
#data_train = '';
#data_result = '';

#cleaning the data if necessary


def loadFile():
    # TODO add the logic to loop through list of generated arff files;
    #trainingDataset = arff.load(open('input\emo_large.arff','r'));
    trainingDataset = arff.load(open('input\\rftrainingdata.arff','r'));
    testDataset = arff.load(open('input\\rfdataresultset2.arff','r'));

    print("*******************");
    #print(trainingDataset['attributes']);

    #dataset contains two arrays namely 'attributes' and 'data'.'data' is
    #  a multidimensional array..
    trainingData=np.array(trainingDataset['data']);
    testData = np.array(testDataset['data']);

    print('shape');
    print(testData.shape);
    #Output log;accessing data elements
    #print(data[0][1]);

    #accessing attributes
 #   print(len(dataset['attributes']));
    parse(trainingData,testData);



def parse(data,testingData):
    #remove string element from the data array as first element is name
    #TODO either we can remove the attribute 'name' from generating the
    #arff file itself.

   # print(data);

#(10, 6555)
    print(data.shape);

   # print(data[0:2,1:3]);

    #print(data[0:2, 0]);

    #print(data[0:3, 6554]);
    #data=np.array(dataset['data']);
    #data = np.delete(data[::,0])
    #print(data.shape);
    #print(data[0]);
    print('line 57')
    data_train = data[::,1:6554]
    data_result = data[::, 6554]

    print('line 68');
    #print(testingData);
    test_data = testingData[::,1:6554];
    #print(test_data);

    #data_result[0:5] = 'amgry';
    #data_result[5:10] = 'sad'
    #data_result[5] = 'happy';

    data_result[0:18] = "angry";
    data_result[18:37] = "happy";
    data_result[37:55]="unhappy";

    print (data_result)
    #print (data_train.shape);
    print (data_result.shape);
    forest = RandomForestClassifier(n_estimators = 100);
    print ('ready for RF');
    forest = forest.fit(data_train, data_result);
    output = forest.predict(test_data);
    print(output);
    #TODO Pass the parsed input data elements to the algorithm

loadFile();

