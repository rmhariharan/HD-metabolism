from DataMapper import DataMapper

from FileNameGetter import FileNameGetter

listoffiles = FileNameGetter("C:/Users/rharihar/Desktop/CHDI_PROJECT/Pathway_Gene_Heatmap_Data/KEGG_Pathway_Genes_Exp")
x = str()
myindex = 0
for file in listoffiles[0]:
    x = listoffiles[1][myindex]
    my_object = DataMapper(file,"C:/Users/rharihar/Desktop/CHDI_PROJECT/Pathway_Gene_Heatmap_Data/KEGG_Pathway_Ids/"+x,"entrez","Entrez Id","C:/Users/rharihar/Desktop/CHDI_PROJECT/Pathway_Gene_Heatmap_Data/KEGG_Gene_Mapped_Ids"+"/"+x)
    myindex = myindex +1
    my_object.dataMap()
print('Done')
