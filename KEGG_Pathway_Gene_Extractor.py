'''This is a script for scraping gene symbols and gene Entrez ids from KEGG pathway web pages.
    Input is a csv file with at least two columns. One column has the KEGG Ids for pathways (here "KEGG ID")
    while the other (here 'Pathway Name') has corresponding pathway names. The code does webscraping and retrieves
    gene lists (Entrez Ids, and Gene symbols) for all pathways (here, 45 pathways) listed in the input file.
    It then writes the genes lists per pathway as separate .csv files to a specified local disk'''

import pandas as pd
import urllib.request
import re

mydata = pd.read_csv("C:/Users/rharihar/Desktop/CHDI_PROJECT/Pathway_Gene_Heatmap_Data/My_Pathway_Ids.csv")
url_base = "http://www.genome.jp/dbget-bin/www_bget?pathway+mmu"
x = 0
row_index = 0
Pathway = ""

for i in range (0,44):
    x = mydata['KEGG ID'][row_index]
    pathway = mydata['Pathway Name'][row_index]
    x = str(x)
    if len(x) == 2:
        x = "000"+x
    elif len(x) == 3:
        x = "00"+x
    row_index = row_index+1

    
# Access the webpage using urllib

    full_url = url_base+x
     
    web_page = urllib.request.urlopen(full_url)

    my_webpage_data = str(web_page.read())

    pattern_list = re.findall("mmu:(\d+)",my_webpage_data)
    pattern_list_2 = re.findall("<div>(\w+\s*\w*);\s",my_webpage_data)
    if len(pattern_list) == len(pattern_list_2):
        
        mydataframe = pd.DataFrame()
        mydataframe['Entrez Id'] = pattern_list
        mydataframe['Gene symbol'] = pattern_list_2
        pathway = pathway.replace("/","")
        mydataframe.to_csv("C:/Users/rharihar/Desktop/CHDI_PROJECT/Pathway_Gene_Heatmap_Data/KEGG_Pathway_Ids/"+pathway+".csv",index = False)
        print("progressing")
    full_url = ""
    








