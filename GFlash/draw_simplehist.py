import os as os_
import sys
from glob import glob
from ROOT import *

gROOT.SetBatch(True)
gStyle.SetOptStat(True)

rebin = 1

def main(inputfile, hist, outputdir, outputfile):
    if not os_.path.exists(inputfile) : print('Cannot found input file : {}, quit'.format(inputfile)); quit()
    
    infile = TFile(inputfile)

    outputdir = outputdir
    if not os_.path.exists(outputdir) : os_.system('mkdir -p '+outputdir)
   
    h = infile.Get(hist)
    
    c = TCanvas('c','',800,600)
    
    c.cd()
    h.Draw('HIST E SAME')
    c.SaveAs(outputdir+'/'+outputfile)


if __name__ == '__main__' :

    hists=[ 
            'fDp','fDp_SPbeforeECAL','fDp_SPinECAL','fDp_SPinHCAL',
            'fPi0','fPi0_SPbeforeECAL','fPi0_SPinECAL','fPi0_SPinHCAL',	
            'fPi0L','fPi0L_SPbeforeECAL','fPi0L_SPinECAL','fPi0L_SPinHCAL',
            'Class', 'Class_SPbeforeECAL', 'Class_SPinECAL', 'Class_SPinHCAL',
            ]
    
    # Run
    for hist in hists:
        main(inputfile='./HistRezaAnalysis_1GeV.root', hist=hist, outputdir='./plots_1GeV', outputfile=hist+'.png')
        main(inputfile='./HistRezaAnalysis_2GeV.root', hist=hist, outputdir='./plots_2GeV', outputfile=hist+'.png')
        main(inputfile='./HistRezaAnalysis_5GeV.root', hist=hist, outputdir='./plots_5GeV', outputfile=hist+'.png')
        main(inputfile='./HistRezaAnalysis_7GeV.root', hist=hist, outputdir='./plots_7GeV', outputfile=hist+'.png')
        main(inputfile='./HistRezaAnalysis_10GeV.root', hist=hist, outputdir='./plots_10GeV', outputfile=hist+'.png')
        main(inputfile='./HistRezaAnalysis_15GeV.root', hist=hist, outputdir='./plots_15GeV', outputfile=hist+'.png')
        main(inputfile='./HistRezaAnalysis_20GeV.root', hist=hist, outputdir='./plots_20GeV', outputfile=hist+'.png')
        main(inputfile='./HistRezaAnalysis_30GeV.root', hist=hist, outputdir='./plots_30GeV', outputfile=hist+'.png')
        main(inputfile='./HistRezaAnalysis_40GeV.root', hist=hist, outputdir='./plots_40GeV', outputfile=hist+'.png')
        main(inputfile='./HistRezaAnalysis_50GeV.root', hist=hist, outputdir='./plots_50GeV', outputfile=hist+'.png')
        main(inputfile='./HistRezaAnalysis_70GeV.root', hist=hist, outputdir='./plots_70GeV', outputfile=hist+'.png')
        main(inputfile='./HistRezaAnalysis_100GeV.root', hist=hist, outputdir='./plots_100GeV', outputfile=hist+'.png')
        main(inputfile='./HistRezaAnalysis_150GeV.root', hist=hist, outputdir='./plots_150GeV', outputfile=hist+'.png')
        main(inputfile='./HistRezaAnalysis_200GeV.root', hist=hist, outputdir='./plots_200GeV', outputfile=hist+'.png')
        main(inputfile='./HistRezaAnalysis_300GeV.root', hist=hist, outputdir='./plots_300GeV', outputfile=hist+'.png')
        main(inputfile='./HistRezaAnalysis_400GeV.root', hist=hist, outputdir='./plots_400GeV', outputfile=hist+'.png')
        main(inputfile='./HistRezaAnalysis_500GeV.root', hist=hist, outputdir='./plots_500GeV', outputfile=hist+'.png')
