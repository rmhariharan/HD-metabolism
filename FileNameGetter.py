def FileNameGetter(Path_To_Folder):
    '''Retrieves the absolute paths to all files in a folder. Takes as input full path to the folder.Outputs two lists: (1) list of file names in the folder and (2)fullpaths for these files'''

    import os

    files = os.listdir(Path_To_Folder)
    file_list = list()
    file_name_list = list()
    
    for file in files:
        full_path = os.path.join(Path_To_Folder+"/",file)
        file_list.append(full_path)
        file_name_list.append(file)
    return file_list,file_name_list

    
