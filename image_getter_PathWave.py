import re
import urllib.request
url_file = open("C:/Users/rharihar/Desktop/CHDI_PROJECT/Dec_2015_3_tissues_PathWave/Striatum/10_MON_Q140_table.txt","r")                 ##Specify input file to be used                 
local_url_file = url_file.read()
url = re.findall("http.+",local_url_file)
x = 1
for i in url:
    x = str(x)
    ##req = urllib.request.Request(i)
    resp = urllib.request.urlopen(i)
    respdata = resp.read()
    respdata = str(respdata)
    image_url_part2 = re.findall("/tmp/mark_pathway.+png",respdata)
    image_url_part2 = image_url_part2[0]
    image_url_part1 = "http://www.kegg.jp"
    full_image_url = image_url_part1 + image_url_part2
    part_of_outfile_name = re.findall("DEFINITION\s+(\w+\s\w+)",respdata)
    print (part_of_outfile_name)
    if part_of_outfile_name:
        urllib.request.urlretrieve(full_image_url,"C:/Users/rharihar/Desktop/CHDI_PROJECT/Dec_2015_3_tissues_PathWave/Striatum/6MON_Q140_FIGURES/"+part_of_outfile_name[0]+".png")    ##Specify target path

    else:
        urllib.request.urlretrieve(full_image_url,"C:/Users/rharihar/Desktop/CHDI_PROJECT/Dec_2015_3_tissues_PathWave/Striatum/6MON_Q140_FIGURES/"+x+".png")
        x = int(x)
        x = x+1
print ("Done")
