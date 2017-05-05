from Seaborn_Heatmap import heatmapmaker
import os
import pandas as pd

samplenames = "C:/Users/rharihar/Desktop/CHDI_PROJECT/Pathway_Gene_Heatmap_Data/Sample_Ids.txt"

fileslist = os.listdir("C:/Users/rharihar/Desktop/CHDI_PROJECT/Pathway_Gene_Heatmap_Data/KEGG_Pathway_Genes_Exp")
fullpath = str()
for file in fileslist:
    #Path to heatmapdata file
    fullpath = os.path.join("C:/Users/rharihar/Desktop/CHDI_PROJECT/Pathway_Gene_Heatmap_Data/KEGG_Pathway_Genes_Exp/",file)
    outputfilepath = os.path.join("C:/Users/rharihar/Desktop/CHDI_PROJECT/Pathway_Gene_Heatmap_Data/KEGG_Gene_Heatmaps/",file)+".png"
    genenames_df = pd.read_csv(os.path.join("C:/Users/rharihar/Desktop/CHDI_PROJECT/Pathway_Gene_Heatmap_Data/KEGG_Gene_Mapped_Ids",file))
    genenames = list(genenames_df['Gene symbol'])
    heatmapmaker(samplenames,genenames,fullpath,outputfilepath, Font_Size = 1.00)
    
    
