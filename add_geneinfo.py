import csv
import bisect
class GeneInfo(object):
    def __init__(self, symbol, name, entrezID, mouseGDB_ID, refseq_ID):
        self.name = name
        self.symbol = symbol
        self.entrezID = entrezID
        self.mouseGDB_ID = mouseGDB_ID
        self.refseqID = refseq_ID


geneinfo_file=open("/proj/MLL-AF9_Frank/betti_star/07_DeSeq2_alt/GUNNING/hs_geneinfo.csv", "r")
M13_DE=open("/proj/MLL-AF9_Frank/betti_star/07_DeSeq2_alt/GUNNING/DE_genes_P_0_01_M13_DMSO_B_vs_M13_JP4_094.id_csv", "r")
MV4_DE=open("/proj/MLL-AF9_Frank/betti_star/07_DeSeq2_alt/GUNNING/DE_genes_P_0_01_MV4_DMSO_B_vs_MV4_JP4_094.id_csv", "r")
M13_all=open("/proj/MLL-AF9_Frank/betti_star/07_DeSeq2_alt/GUNNING/M13_DMSO_B_vs_M13_JP4_094.id_csv", "r")
MV4_all=open("/proj/MLL-AF9_Frank/betti_star/07_DeSeq2_alt/GUNNING/MV4_DMSO_B_vs_MV4_JP4_094.id_csv", "r")
dir="/proj/MLL-AF9_Frank/betti_star/07_DeSeq2_alt/GUNNING/"
#gl=genelist_file.readlines()
GI=geneinfo_file.readlines()
GI_dict={}
for line in GI:
    l=line.rsplit('\t')
    GI_dict[l[0]] = l

#print(GI_dict)
'''
count=0
nlist=[]
tmp=list()
for line in gl:
    a=line.rsplit('\t')
    try:
        addInfo=line + GI_dict[a[1]][1]
        nlist.append(addInfo)
    except:
        continue
    if count>10:
        break
    count+=1
'''

def get_geneinfo(genelist_file, info):
    gl = genelist_file.readlines()
    count = 0
    nlist = []
    for line in gl:
        #a=line.rstrip()
        a = line.rsplit('\t')
        try:
            addInfo = line.rstrip() + '\t' + info[a[1]][1]+'\n'
            info_new= a[0] + '\t' + \
                      a[2] + '\t' + \
                      a[1] + '\t' + \
                      info[a[1]][1] + '\t' + \
                      info[a[1]][3] + '\t' + \
                      a[3] + '\t' + \
                      a[4] + '\t' + \
                      a[5] + '\t' + \
                      a[6] + '\t' + \
                      a[7] + '\t' + \
                      a[8]
            nlist.append(info_new)
        except:
            continue
        if count > 10:
            break
        #count += 1
    return(nlist)

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
write_csv(dir, 'M13_JP4_094_DE_p_0_01.csv', a)

b=get_geneinfo(MV4_DE, GI_dict)
write_csv(dir, 'MV4_JP4_094_DE_p_0_01.csv', b)

c=get_geneinfo(M13_all, GI_dict)
write_csv(dir, 'M13_JP4_094_all_genes.csv', c)

d=get_geneinfo(MV4_all, GI_dict)
write_csv(dir, 'MV4_JP4_094_all_genes.csv', d)



