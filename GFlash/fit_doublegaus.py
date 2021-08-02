import os as os_
import sys
from glob import glob
from ROOT import *

gROOT.SetBatch(True)
gStyle.SetOptStat(True)
gStyle.SetOptStat(False)
#gStyle.SetOptFit(111111)

rebin = 1

def main(inputfile, hist, outputdir='plots', outputfile='output.png'):
    if not os_.path.exists(inputfile) : print('Cannot found input file : {}, quit'.format(inputfile)); quit()
    
    infile = TFile(inputfile)

    outputdir = outputdir
    if not os_.path.exists(outputdir) : os_.system('mkdir -p '+outputdir)
   
    h = infile.Get(hist)
    
    if h.Integral()==0 : print('no entry.'); pass
    h.Scale(1/h.Integral())
   
 
    gaus1 = TF1('gaus1','gaus',0,0.9)
    gaus2 = TF1('gaus2','gaus',0.9,1)

    h.Fit(gaus1,'R')
    h.Fit(gaus2,'R+')
    
    c = TCanvas('c','',800,600)
    
    c.cd()
    h.Draw('HIST E SAME')
    gaus1.Draw('SAME')
    gaus2.Draw('SAME')
    c.SaveAs(outputdir+'/'+outputfile)


if __name__ == '__main__' :

    hists=[ 
            #'fDp','fDp_SPbeforeECAL','fDp_SPinECAL','fDp_SPinHCAL',
            #'fPi0','fPi0_SPbeforeECAL','fPi0_SPinECAL','fPi0_SPinHCAL',	
            #'fPi0L','fPi0L_SPbeforeECAL','fPi0L_SPinECAL','fPi0L_SPinHCAL',
            #'Class', 'Class_SPbeforeECAL', 'Class_SPinECAL', 'Class_SPinHCAL',
            'fPi0L_SPinECAL',
            ]
    
    # Run
    for hist in hists:
        main(inputfile='histos/HistRezaAnalysis_20GeV.root',
            hist=hist,
            outputdir='./fitresult_20GeV',
            outputfile=hist+'.png')
        main(inputfile='histos/HistRezaAnalysis_30GeV.root',
            hist=hist,
            outputdir='./fitresult_30GeV',
            outputfile=hist+'.png')
        main(inputfile='histos/HistRezaAnalysis_40GeV.root',
            hist=hist,
            outputdir='./fitresult_40GeV',
            outputfile=hist+'.png')
        main(inputfile='histos/HistRezaAnalysis_50GeV.root',
            hist=hist,
            outputdir='./fitresult_50GeV',
            outputfile=hist+'.png')
        main(inputfile='histos/HistRezaAnalysis_70GeV.root',
            hist=hist,
            outputdir='./fitresult_70GeV',
            outputfile=hist+'.png')
        main(inputfile='histos/HistRezaAnalysis_100GeV.root',
            hist=hist,
            outputdir='./fitresult_100GeV',
            outputfile=hist+'.png')
        main(inputfile='histos/HistRezaAnalysis_150GeV.root',
            hist=hist,
            outputdir='./fitresult_150GeV',
            outputfile=hist+'.png')
        main(inputfile='histos/HistRezaAnalysis_200GeV.root',
            hist=hist,
            outputdir='./fitresult_200GeV',
            outputfile=hist+'.png')
