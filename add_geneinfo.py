import csv
                                              #vvvvvvvvvvvvvvvvvv#
# this file was downloaded with a perl script '01_get_geneinfo.pl' obtained from the affiliated page
# https://www.genenames.org/cgi-bin/download?col=gd_app_sym&col=gd_app_name&col=gd_pub_eg_
# id&col=gd_mgd_id&col=gd_pub_refseq_ids&status=Approved&status=Entry+Withdrawn&status_opt=2&where=&order_by=gd_app_sym_sort&format=LWP&limit=&hgnc_dbtag=on&submit=submit
geneinfo_file=open("hs_geneinfo.csv", "r")

# *.id_csv files to be modified
M13_DE=open("./ctrl_vs_mutant.is_csv", "r")

dir="results/"

#make a dictionary with the entire line for a substring of the same line
#potentially, double entries will be overwritten, however, gene symbols should be uniqe in GI
GI=geneinfo_file.readlines()
GI_dict={}
for line in GI:
    l=line.rsplit('\t')
    GI_dict[l[0]] = l
print(GI_dict)
# construct a list of new strings. searches in the dictionary for gene name (info[a[1]][1]) and mouse reference ID. adds to string
def get_geneinfo(genelist_file, info):
    gl = genelist_file.readlines()
    #count = 0
    nlist = []
    for line in gl:
        #print(line)
        #a=line.rstrip()
        a = line.rsplit('\t')
        try:
            #addInfo = line.rstrip() + '\t' + info[a[1]][1]+'\n'
            info_new= a[0] + '\t' + \
                      a[2] + '\t' + \
                      a[1] + '\t' + \
                      "'"+info[a[1]][1] + "'" + '\t' + \
                      info[a[1]][3] + '\t' + \
                      a[3] + '\t' + \
                      a[4] + '\t' + \
                      a[5] + '\t' + \
                      a[6] + '\t' + \
                      a[7] + '\t' + \
                      a[8]
            nlist.append(info_new)
            #print(info_new)
        except:
            info_new = a[0] + '\t' + \
                       a[2] + '\t' + \
                       a[1] + '\t' + \
                       'NA' + '\t' + \
                       'NA' + '\t' + \
                       a[3] + '\t' + \
                       a[4] + '\t' + \
                       a[5] + '\t' + \
                       a[6] + '\t' + \
                       a[7] + '\t' + \
                       a[8]
            nlist.append(info_new)
            continue #the header line will throw an exception, genes present in the subset but not the geneinfo file as well
        #if count > 10: #just for testing, the script is slow
        #    break
        #count += 1
    return(nlist)

# define a function that adds the header line and iterates
def write_csv(directory, name, glist):
    with open(str(directory+name),'w') as resultFile:
        #write first line
        #line_one="ncbi_id\tgene_symbol\tentrez_id\tbaseMean\tlog2FoldChange\tlfcSE\tstat\tpvalue\tpadj\tname\n"
        line_one_new="ncbi_id\tentrez_id\tgene_symbol\tname\tmouse_GDB_ID\tbaseMean\tlog2FoldChange\tlfcSE\tstat\tpvalue\tpadj\n"
        #resultFile.write(line_one)
        resultFile.write(line_one_new)

    #with open(str(directory + name), 'a') as resultFile:
        for row in glist:
            resultFile.write(row)
    return 0
a=get_geneinfo(M13_DE, GI_dict)
write_csv(dir, 'testa.csv', a)


