import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import csv

dataset = pd.read_csv('train_final.csv');
X = dataset.iloc[: ,  : 25].values;
y = dataset.iloc[: , 25 ].values;


#####################################################

from sklearn.ensemble import RandomForestRegressor
reg = RandomForestRegressor( n_estimators=10 ,  random_state=0)
reg.fit(X , y);



##################################################
test_data = pd.read_csv('test_final.csv');
XX = test_data.iloc[: ,  : 25].values;



###########################################
                                          #
yyPred = reg.predict( XX )                #
                                          #
###################################
                                          
ids=[];                                         
with open('test_final.csv','r') as f:
    c_reader=csv.reader(f)
    for line in c_reader:
        ids.append(line[24]);
        #print(line[24])


                                          
c=0;
for i in yyPred:
    print( str(ids[c]) +  " "+ str(i))
    c=c+1;




