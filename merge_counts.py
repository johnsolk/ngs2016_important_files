


import os
from os import path
import pandas as pd


txp_file = "quantification/txp_to_gene.tsv"
# get txp names as index
listofsamples = os.listdir("quantification/quants")
quants = {}
data = None
for sample in listofsamples:
    if os.path.isdir("quantification/quants/"+sample):
        if os.path.isfile("quantification/quants/"+sample+"/quant.sf"):
            quant_file = "quantification/quants/"+sample+"/quant.sf"
            data=pd.DataFrame.from_csv(quant_file,sep='\t')
            tpm = data['TPM']
            quants[sample] = tpm

counts = pd.DataFrame.from_dict(quants)
counts.set_index(data.index,inplace=True)
counts.to_csv("counts.csv")
