def heatmapmaker(Sample_Names,Entity_Names,Heatmap_Data,Output_File, Resolution = 300,Font_Size = 1.05,Color_Map = "bwr"):
    '''A function for making heatmap, Sample names on x-axis, entity names on y-axis. Takes as input two text files:
       one containing tab separated sample names, the other containing newline separated Entity names (e.g.Gene names).
       Data for the heatmap is input as a .csv file. Output file path needs to be specified, format is currently png.
       other default values can be changed. Assumes a dataframe with row and column names. Number of columns to be used
       needs to be changed in the code for different input files'''
    
    import pandas as pd
    import seaborn as sns
    sns.set(font_scale = Font_Size)

    ## Read in variable names and sample names, and convert to list
    collection_file_1 = open(Sample_Names,'r+')
    pre_list_1 = collection_file_1.read()
    sample_ids= pre_list_1.split()


##    collection_file_2 = open(Entity_Names,'r+')
##    pre_list_2 = collection_file_2.read()
##    entity_names= pre_list_2.split()


    #Read in data
    df = pd.read_csv(Heatmap_Data, header = None, skiprows = [0], usecols = [1,2,3,4,5,6,7,8,9,10,11,12] )
    
    g = sns.heatmap(df,xticklabels = sample_ids,yticklabels = Entity_Names,label = 'small',robust = False,cmap = Color_Map,cbar = True,vmin = -0.8,vmax = 0.8)
    sns.plt.xticks(rotation = 0)

    ##from matplotlib.patches import Rectangle
    ##ax1 = g.add_patch(Rectangle((0, 59), 37, 0, fill=False, edgecolor='orange', lw=0.6))
   
    sns.plt.savefig(Output_File,format = 'png',bbox_inches = 'tight',dpi = Resolution)
    sns.plt.clf()
    ##sns.plt.show()
    return "Done"
