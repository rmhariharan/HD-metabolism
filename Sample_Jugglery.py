import pandas as pd

def Sample_Holdout():
    '''From an input csv file with n columns (samples), creates files with n-k columns (where k is the number of samples you want to holdout)'''
    data = pd.read_csv("C:/Users/rharihar/Desktop/Exercises/Sample_Holdout_Test_Data.csv",index_col = 0) ## Input file name
    k =0
    for i in data:
        ColsToDrop = [data.columns[k]]
        newdata = data.drop(ColsToDrop,axis =1) ## Use the drop function to drop a column indexed by column name
        k =k+1
        newdata.to_csv("C:/Users/rharihar/Desktop/Exercises/" + "newdata_minus_" + str(k) + ".csv") ##Output file name
    
