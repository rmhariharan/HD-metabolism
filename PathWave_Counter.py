import pandas as pd

count_list = list()
name_var =1
for filename in range (0,23):
    data = pd.read_csv("C:/Users/rharihar/Desktop/CHDI_PROJECT/Dec_2015_3_tissues_PathWave/Liver/HOLD_OUT/10_MON/Q175/minus_row"+str(name_var)+"table.csv",index_col =0,sep =',')
    row_num = 0
    count =0
    for row in data.index:
        if data.iloc[row_num,1] < 0.05 and data.iloc[row_num,0] != 'Metabolic pathways':
            ##print (data.iloc[row_num,0], len((data.iloc[row_num,0])))
            row_num = row_num+1
            count = count+1
        elif data.iloc[row_num,1] < 0.05 and data.iloc[row_num,0] == 'Metabolic pathways':
            row_num = row_num+1
    count_list.append(count)
    name_var = name_var+1
print(count_list)
