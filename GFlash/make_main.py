import sys
import os
import subprocess
import readline
import string

#path = '/eos/cms/store/group/comm_fastsim/'
path = '~/SE_UserHome/FastSimCalo/200k/'
samples = [
'RezaAnalysis_1GeV',
'RezaAnalysis_2GeV',
'RezaAnalysis_5GeV',
'RezaAnalysis_7GeV',
'RezaAnalysis_10GeV',
'RezaAnalysis_15GeV',
'RezaAnalysis_20GeV',
'RezaAnalysis_30GeV',
'RezaAnalysis_40GeV',
'RezaAnalysis_50GeV',
'RezaAnalysis_70GeV',
'RezaAnalysis_100GeV',
'RezaAnalysis_150GeV',
'RezaAnalysis_200GeV',
'RezaAnalysis_300GeV',
'RezaAnalysis_400GeV',
'RezaAnalysis_500GeV',
]


text = ''
for num, sample in enumerate(samples):
    text += 'TC = new TChain("g4SimHits/eventTree") ;\n' +\
    'TC ->Add("'+ path +'/'+ sample +'*");\n' +\
    'GFlash GF' + sample +'(TC);\n' +\
    'GF'+ sample + '.Loop("' + sample + '");\n' +\
    'delete TC;\n' +\
    '\n' +\
    ''


SHNAME = 'main_GFlash.C'
SHFILE='#include "GFlash.h"\n' +\
'int main(){\n' +\
'TChain* TC;\n' +\
text +\
'}'

open(SHNAME, 'wt').write(SHFILE)
os.system("chmod +x "+SHNAME)
