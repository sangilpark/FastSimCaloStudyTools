import os as os_
import sys
from glob import glob
from ROOT import *
from array import array

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
   
    gaus = TF1('gaus','gaus',0.05,0.75) # for 20 GeV
    expo = TF1('expo','expo',0.75,0.95) # for 20 GeV

    #gaus = TF1('gaus','gaus',0.05,0.7) # for 30 GeV
    #expo = TF1('expo','expo',0.85,0.96) # for 30 GeV

    #gaus = TF1('gaus','gaus',0.05,0.85) # for 40 GeV
    #expo = TF1('expo','expo',0.85,0.97) # for 40 GeV

    #gaus = TF1('gaus','gaus',0.05,0.90) # for >40 GeV
    #expo = TF1('expo','expo',0.90,0.99) # for >40 GeV

    total = TF1('total','gaus(0)+expo(3)',0.05,0.99)

    h.Fit(gaus,'R')
    h.Fit(expo,'R+')
    
    par = array( 'd', 5*[0.] )
    par1 = gaus.GetParameters()
    par2 = expo.GetParameters()
    par[0], par[1], par[2] = par1[0], par1[1], par1[2]
    par[3], par[4] = par2[0], par2[1]
    total.SetParameters( par )
    h.Fit(total,'R+','',0.05,0.99)
    
    c = TCanvas('c','',800,600)
    
    c.cd()
    h.Draw('HIST E SAME')
    total.Draw('SAME')
    #gaus.Draw('SAME')
    #expo.Draw('SAME')
    c.SaveAs(outputdir+'/'+outputfile)


if __name__ == '__main__' :

    hists=[ 
            #'fDp','fDp_SPbeforeECAL','fDp_SPinECAL','fDp_SPinHCAL',
            #'fPi0','fPi0_SPbeforeECAL','fPi0_SPinECAL','fPi0_SPinHCAL',	
            #'fPi0L','fPi0L_SPbeforeECAL','fPi0L_SPinECAL','fPi0L_SPinHCAL',
            #'Class', 'Class_SPbeforeECAL', 'Class_SPinECAL', 'Class_SPinHCAL',
            'fPi0L_SPinECAL',
            ]
    
    outputdir = 'fitresult_fPi0L_gausexpo_total'
    
    # Run
    for hist in hists:
        main(inputfile='histos/HistRezaAnalysis_20GeV.root',
            hist=hist,
            outputdir=outputdir,
            outputfile=hist+'_20GeV.png')
        #main(inputfile='histos/HistRezaAnalysis_30GeV.root',
        #    hist=hist,
        #    outputdir=outputdir,
        #    outputfile=hist+'_30GeV.png')
        #main(inputfile='histos/HistRezaAnalysis_40GeV.root',
        #    hist=hist,
        #    outputdir=outputdir,
        #    outputfile=hist+'_40GeV.png')
        #main(inputfile='histos/HistRezaAnalysis_50GeV.root',
        #    hist=hist,
        #    outputdir=outputdir,
        #    outputfile=hist+'_50GeV.png')
        #main(inputfile='histos/HistRezaAnalysis_70GeV.root',
        #    hist=hist,
        #    outputdir=outputdir,
        #    outputfile=hist+'_70GeV.png')
        #main(inputfile='histos/HistRezaAnalysis_100GeV.root',
        #    hist=hist,
        #    outputdir=outputdir,
        #    outputfile=hist+'_100GeV.png')
        #main(inputfile='histos/HistRezaAnalysis_150GeV.root',
        #    hist=hist,
        #    outputdir=outputdir,
        #    outputfile=hist+'_150GeV.png')
        #main(inputfile='histos/HistRezaAnalysis_200GeV.root',
        #    hist=hist,
        #    outputdir=outputdir,
        #    outputfile=hist+'_200GeV.png')
