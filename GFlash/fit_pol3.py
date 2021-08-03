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
  
    pol3 = TF1('pol3','pol3',0.05,1.00)

    h.Fit(pol3,'R')
    
    c = TCanvas('c','',800,600)
    
    c.cd()
    h.Draw('HIST E SAME')
    pol3.Draw('SAME')
    c.SaveAs(outputdir+'/'+outputfile)


if __name__ == '__main__' :

    hists=[ 
            #'fDp','fDp_SPbeforeECAL','fDp_SPinECAL','fDp_SPinHCAL',
            #'fPi0','fPi0_SPbeforeECAL','fPi0_SPinECAL','fPi0_SPinHCAL',	
            #'fPi0L','fPi0L_SPbeforeECAL','fPi0L_SPinECAL','fPi0L_SPinHCAL',
            #'Class', 'Class_SPbeforeECAL', 'Class_SPinECAL', 'Class_SPinHCAL',
            'fPi0L_SPinECAL',
            ]
    outputdir = 'fitresult_fPi0L_pol3'
    
    # Run
    for hist in hists:
        #main(inputfile='histos/HistRezaAnalysis_20GeV.root',
        #    hist=hist,
        #    outputdir=outputdir,
        #    outputfile=hist+'_20GeV.png')
        #main(inputfile='histos/HistRezaAnalysis_30GeV.root',
        #    hist=hist,
        #    outputdir=outputdir,
        #    outputfile=hist+'_30GeV.png')
        #main(inputfile='histos/HistRezaAnalysis_40GeV.root',
        #    hist=hist,
        #    outputdir=outputdir,
        #    outputfile=hist+'_40GeV.png')
        main(inputfile='histos/HistRezaAnalysis_50GeV.root',
            hist=hist,
            outputdir=outputdir,
            outputfile=hist+'_50GeV.png')
        main(inputfile='histos/HistRezaAnalysis_70GeV.root',
            hist=hist,
            outputdir=outputdir,
            outputfile=hist+'_70GeV.png')
        main(inputfile='histos/HistRezaAnalysis_100GeV.root',
            hist=hist,
            outputdir=outputdir,
            outputfile=hist+'_100GeV.png')
        main(inputfile='histos/HistRezaAnalysis_150GeV.root',
            hist=hist,
            outputdir=outputdir,
            outputfile=hist+'_150GeV.png')
        main(inputfile='histos/HistRezaAnalysis_200GeV.root',
            hist=hist,
            outputdir=outputdir,
            outputfile=hist+'_200GeV.png')
