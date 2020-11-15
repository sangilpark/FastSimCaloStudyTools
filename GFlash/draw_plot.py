import math
import gc
import sys
import ROOT
import numpy as npi
import collections
import copy
from array import array
import os
ROOT.gROOT.SetBatch(ROOT.kTRUE)
ROOT.gROOT.ProcessLine("gErrorIgnoreLevel = 1;")
ROOT.TH1.AddDirectory(ROOT.kFALSE)
from ROOT import TColor
from ROOT import TGaxis
from ROOT import *
#TGaxis.SetMaxDigits(2)

mean_dict = collections.OrderedDict()

def draw1dHist(hist,variable="fDp", label_name="sample", can_name="can", doFit=False):
    ROOT.gStyle.SetOptStat(1111);
    #ROOT.gStyle.SetOptStat(0);
    if doFit : 
    	ROOT.gStyle.SetOptFit(1)

    a,b = label_name.split("_")
    SampleEnergy = b.replace('.root','')
    print SampleEnergy 
    
    canvas = ROOT.TCanvas(can_name,can_name,1100,600)
    canvas.cd()

    #pad_name = "pad"
    #pad1=ROOT.TPad(pad_name, pad_name, 0.05, 0.05, 1, 0.99 , 0)
    #pad1.Draw()
    if variable == "fDp" :
        legend = TLegend(0.7,0.7,0.9,0.9)
    elif variable=="fPi0" :
        legend = TLegend(0.4,0.7,0.6,0.9)
    elif variable=="fPi0L" :
        legend = TLegend(0.7,0.7,0.9,0.9)
    else : 
        print 'variable not found'
        quit()
    
    
    hist.Scale(1/hist.Integral())
    hist.SetLineColor( 4 )
    hist.SetLineWidth( 2 )
    hist.SetTitle('(E(#pi^{+}) =' + SampleEnergy +')')
    hist.GetXaxis().SetTitle(variable)
    hist.GetYaxis().SetTitle('Normalized')
    hist.GetXaxis().SetTitleSize(0.05)
    hist.GetYaxis().SetTitleSize(0.05)
    hist.SetMaximum(1.5*hist.GetMaximum())
    hist.SetMinimum(0);
    hist.GetYaxis().SetTitleOffset(0.7)
    #hist.Draw("E")
    if doFit :
	if variable == "fDp" :
	    ROOT.gStyle.SetStatY(0.9);                
    	    ROOT.gStyle.SetStatX(0.4);                
    	    ROOT.gStyle.SetStatW(0.15);                
    	    ROOT.gStyle.SetStatH(0.15);                
    	    #ROOT.gStyle.SetOptStat(0)
	    if SampleEnergy == "1GeV":
		f = TF1("triplegaus","gaus(0)+gaus(3)+gaus(6)",0.1,1)
	    	f.SetParName(0,"gaus1.Constant")
	    	f.SetParName(1,"gaus1.Mean")
	    	f.SetParName(2,"gaus1.Sigma")
	    	f.SetParName(3,"gaus2.Constant")
	    	f.SetParName(4,"gaus2.Mean")
	    	f.SetParName(5,"gaus2.Sigma")
	    	f.SetParName(6,"gaus3.Constant")
	    	f.SetParName(7,"gaus3.Mean")
	    	f.SetParName(8,"gaus3.Sigma")
	  
		# Initial value and limit
	    	f.SetParameter(0,0.019)
	    	f.SetParLimits(0,0,0.1)
	    	
		f.SetParameter(1,0.54)
	    	f.SetParLimits(1,0.3,0.7)
	    	
		f.SetParameter(2,0.12)
	    	f.SetParLimits(2,0,0.2)
	    	
		f.SetParameter(3,0.01337)
	    	f.SetParLimits(3,0,0.1)
	    	
		f.SetParameter(4,0.7)
	    	f.SetParLimits(4,0.4,1)
	    	
		f.SetParameter(5,0.078)
	    	f.SetParLimits(5,0,0.1)
	   
		f.SetParameter(6,0.0089)
	    	f.SetParLimits(6,0,0.1)
	    	
		f.SetParameter(7,0.84)
	    	f.SetParLimits(7,0.7,1)
	    	
		f.SetParameter(8,0.043)
	    	f.SetParLimits(8,0,0.1)
	   
		hist.Fit(f,"S",'',0,1.0)
		f1 = TF1("gaus1","gaus",0,1.0)
	    	f2 = TF1("gaus2","gaus",0,1.0)
	    	f3 = TF1("gaus3","gaus",0,1.0)
		
		f1.SetParameter(0,f.GetParameter(0))
	    	f1.SetParameter(1,f.GetParameter(1))
	    	f1.SetParameter(2,f.GetParameter(2))
	    	f2.SetParameter(0,f.GetParameter(3))
	    	f2.SetParameter(1,f.GetParameter(4))
	    	f2.SetParameter(2,f.GetParameter(5))
	    	f3.SetParameter(0,f.GetParameter(6))
	    	f3.SetParameter(1,f.GetParameter(7))
	    	f3.SetParameter(2,f.GetParameter(8))
	    	f1.SetLineColor(6)
	    	f2.SetLineColor(3)
	    	f3.SetLineColor(5)
		legend.SetHeader("Fit range : 0.1 - 1.0","C")
		legend.AddEntry(a,"MC","le")
		legend.AddEntry("f","total func","l")
		legend.AddEntry("f1","gaus1","l")
		legend.AddEntry("f2","gaus2","l")
		legend.AddEntry("f3","gaus3","l")

		rp = TRatioPlot(hist)
		rp.Draw()
		rp.GetUpperPad().cd()
	    	f1.Draw("same")
	    	f2.Draw("same")
	    	f3.Draw("same")
		legend.Draw()
		rp.GetLowerRefGraph().SetMinimum(-5)
		rp.GetLowerRefGraph().SetMaximum(5)


		mean_dict[str(SampleEnergy)+"_"+variable] = hist.GetMean()
	    
	    elif SampleEnergy == "2GeV":
		f = TF1("triplegaus","gaus(0)+gaus(3)+gaus(6)",0.3,1)
	    	f.SetParName(0,"gaus1.Constant")
	    	f.SetParName(1,"gaus1.Mean")
	    	f.SetParName(2,"gaus1.Sigma")
	    	f.SetParName(3,"gaus2.Constant")
	    	f.SetParName(4,"gaus2.Mean")
	    	f.SetParName(5,"gaus2.Sigma")
	    	f.SetParName(6,"gaus3.Constant")
	    	f.SetParName(7,"gaus3.Mean")
	    	f.SetParName(8,"gaus3.Sigma")
	  
		# Initial value and limit
	    	f.SetParameter(0,0.02)
	    	f.SetParLimits(0,0,01)
	    	
		f.SetParameter(1,0.56)
	    	f.SetParLimits(1,0.3,0.7)
	    	
		f.SetParameter(2,0.02)
	    	f.SetParLimits(2,0,0.1)
	    	
		f.SetParameter(3,0.02)
	    	f.SetParLimits(3,0,0.1)
	    	
		f.SetParameter(4,0.71)
	    	f.SetParLimits(4,0.3,1)
	    	
		f.SetParameter(5,0.07)
	    	f.SetParLimits(5,0,0.2)
	   
		f.SetParameter(6,0.006)
	    	f.SetParLimits(6,0,0.1)
	    	
		f.SetParameter(7,0.82)
	    	f.SetParLimits(7,0.6,1)
	    	
		f.SetParameter(8,0.04)
	    	f.SetParLimits(8,0,0.1)
	   
		hist.Fit(f,"S",'',0,1.0)
		f1 = TF1("gaus1","gaus",0,1.0)
	    	f2 = TF1("gaus2","gaus",0,1.0)
	    	f3 = TF1("gaus3","gaus",0,1.0)
		
		f1.SetParameter(0,f.GetParameter(0))
	    	f1.SetParameter(1,f.GetParameter(1))
	    	f1.SetParameter(2,f.GetParameter(2))
	    	f2.SetParameter(0,f.GetParameter(3))
	    	f2.SetParameter(1,f.GetParameter(4))
	    	f2.SetParameter(2,f.GetParameter(5))
	    	f3.SetParameter(0,f.GetParameter(6))
	    	f3.SetParameter(1,f.GetParameter(7))
	    	f3.SetParameter(2,f.GetParameter(8))
	    	f1.SetLineColor(6)
	    	f2.SetLineColor(3)
	    	f3.SetLineColor(5)
		legend.SetHeader("Fit range : 0.3 - 1.0","C")
		legend.AddEntry(a,"MC","le")
		legend.AddEntry("f","total func","l")
		legend.AddEntry("f1","gaus1","l")
		legend.AddEntry("f2","gaus2","l")
		legend.AddEntry("f3","gaus3","l")

		rp = TRatioPlot(hist)
		rp.Draw()
		rp.GetUpperPad().cd()
	    	f1.Draw("same")
	    	f2.Draw("same")
	    	f3.Draw("same")
		legend.Draw()
		rp.GetLowerRefGraph().SetMinimum(-5)
		rp.GetLowerRefGraph().SetMaximum(5)
		
		mean_dict[str(SampleEnergy)+"_"+variable] = hist.GetMean()

	    elif SampleEnergy == "5GeV":
		f = TF1("triplegaus","gaus(0)+gaus(3)+gaus(6)",0.4,1)
	    	f.SetParName(0,"gaus1.Constant")
	    	f.SetParName(1,"gaus1.Mean")
	    	f.SetParName(2,"gaus1.Sigma")
	    	f.SetParName(3,"gaus2.Constant")
	    	f.SetParName(4,"gaus2.Mean")
	    	f.SetParName(5,"gaus2.Sigma")
	    	f.SetParName(6,"gaus3.Constant")
	    	f.SetParName(7,"gaus3.Mean")
	    	f.SetParName(8,"gaus3.Sigma")
	  
		# Initial value and limit
	    	f.SetParameter(0,0.02)
	    	f.SetParLimits(0,0,01)
	    	
		f.SetParameter(1,0.56)
	    	f.SetParLimits(1,0.3,0.7)
	    	
		f.SetParameter(2,0.02)
	    	f.SetParLimits(2,0,0.1)
	    	
		f.SetParameter(3,0.02)
	    	f.SetParLimits(3,0,0.1)
	    	
		f.SetParameter(4,0.71)
	    	f.SetParLimits(4,0.3,1)
	    	
		f.SetParameter(5,0.07)
	    	f.SetParLimits(5,0,0.2)
	   
		f.SetParameter(6,0.006)
	    	f.SetParLimits(6,0,0.1)
	    	
		f.SetParameter(7,0.82)
	    	f.SetParLimits(7,0.6,1)
	    	
		f.SetParameter(8,0.04)
	    	f.SetParLimits(8,0,0.1)
	   
		hist.Fit(f,"S",'',0,1.0)
		f1 = TF1("gaus1","gaus",0,1.0)
	    	f2 = TF1("gaus2","gaus",0,1.0)
	    	f3 = TF1("gaus3","gaus",0,1.0)
		
		f1.SetParameter(0,f.GetParameter(0))
	    	f1.SetParameter(1,f.GetParameter(1))
	    	f1.SetParameter(2,f.GetParameter(2))
	    	f2.SetParameter(0,f.GetParameter(3))
	    	f2.SetParameter(1,f.GetParameter(4))
	    	f2.SetParameter(2,f.GetParameter(5))
	    	f3.SetParameter(0,f.GetParameter(6))
	    	f3.SetParameter(1,f.GetParameter(7))
	    	f3.SetParameter(2,f.GetParameter(8))
	    	f1.SetLineColor(6)
	    	f2.SetLineColor(3)
	    	f3.SetLineColor(5)
		legend.SetHeader("Fit range : 0.4 - 1.0","C")
		legend.AddEntry(a,"MC","le")
		legend.AddEntry("f","total func","l")
		legend.AddEntry("f1","gaus1","l")
		legend.AddEntry("f2","gaus2","l")
		legend.AddEntry("f3","gaus3","l")

		rp = TRatioPlot(hist)
		rp.Draw()
		rp.GetUpperPad().cd()
	    	f1.Draw("same")
	    	f2.Draw("same")
	    	f3.Draw("same")
		legend.Draw()
		rp.GetLowerRefGraph().SetMinimum(-5)
		rp.GetLowerRefGraph().SetMaximum(5)
		
		mean_dict[str(SampleEnergy)+"_"+variable] = hist.GetMean()

	    elif SampleEnergy == "7GeV":
		f = TF1("triplegaus","gaus(0)+gaus(3)+gaus(6)",0.4,1)
	    	f.SetParName(0,"gaus1.Constant")
	    	f.SetParName(1,"gaus1.Mean")
	    	f.SetParName(2,"gaus1.Sigma")
	    	f.SetParName(3,"gaus2.Constant")
	    	f.SetParName(4,"gaus2.Mean")
	    	f.SetParName(5,"gaus2.Sigma")
	    	f.SetParName(6,"gaus3.Constant")
	    	f.SetParName(7,"gaus3.Mean")
	    	f.SetParName(8,"gaus3.Sigma")
	  
		# Initial value and limit
	    	f.SetParameter(0,0.02)
	    	f.SetParLimits(0,0,01)
	    	
		f.SetParameter(1,0.56)
	    	f.SetParLimits(1,0.3,0.7)
	    	
		f.SetParameter(2,0.02)
	    	f.SetParLimits(2,0,0.1)
	    	
		f.SetParameter(3,0.02)
	    	f.SetParLimits(3,0,0.1)
	    	
		f.SetParameter(4,0.71)
	    	f.SetParLimits(4,0.3,1)
	    	
		f.SetParameter(5,0.07)
	    	f.SetParLimits(5,0,0.2)
	   
		f.SetParameter(6,0.006)
	    	f.SetParLimits(6,0,0.1)
	    	
		f.SetParameter(7,0.82)
	    	f.SetParLimits(7,0.6,1)
	    	
		f.SetParameter(8,0.04)
	    	f.SetParLimits(8,0,0.1)
	   
		hist.Fit(f,"S",'',0,1.0)
		f1 = TF1("gaus1","gaus",0,1.0)
	    	f2 = TF1("gaus2","gaus",0,1.0)
	    	f3 = TF1("gaus3","gaus",0,1.0)
		
		f1.SetParameter(0,f.GetParameter(0))
	    	f1.SetParameter(1,f.GetParameter(1))
	    	f1.SetParameter(2,f.GetParameter(2))
	    	f2.SetParameter(0,f.GetParameter(3))
	    	f2.SetParameter(1,f.GetParameter(4))
	    	f2.SetParameter(2,f.GetParameter(5))
	    	f3.SetParameter(0,f.GetParameter(6))
	    	f3.SetParameter(1,f.GetParameter(7))
	    	f3.SetParameter(2,f.GetParameter(8))
	    	f1.SetLineColor(6)
	    	f2.SetLineColor(3)
	    	f3.SetLineColor(5)
		legend.SetHeader("Fit range : 0.4 - 1.0","C")
		legend.AddEntry(a,"MC","le")
		legend.AddEntry("f","total func","l")
		legend.AddEntry("f1","gaus1","l")
		legend.AddEntry("f2","gaus2","l")
		legend.AddEntry("f3","gaus3","l")

		rp = TRatioPlot(hist)
		rp.Draw()
		rp.GetUpperPad().cd()
	    	f1.Draw("same")
	    	f2.Draw("same")
	    	f3.Draw("same")
		legend.Draw()
		rp.GetLowerRefGraph().SetMinimum(-5)
		rp.GetLowerRefGraph().SetMaximum(5)
		
		mean_dict[str(SampleEnergy)+"_"+variable] = hist.GetMean()

	    elif SampleEnergy == "10GeV":
		f = TF1("triplegaus","gaus(0)+gaus(3)+gaus(6)",0.4,1)
	    	f.SetParName(0,"gaus1.Constant")
	    	f.SetParName(1,"gaus1.Mean")
	    	f.SetParName(2,"gaus1.Sigma")
	    	f.SetParName(3,"gaus2.Constant")
	    	f.SetParName(4,"gaus2.Mean")
	    	f.SetParName(5,"gaus2.Sigma")
	    	f.SetParName(6,"gaus3.Constant")
	    	f.SetParName(7,"gaus3.Mean")
	    	f.SetParName(8,"gaus3.Sigma")
	  
		# Initial value and limit
	    	f.SetParameter(0,0.02)
	    	f.SetParLimits(0,0,01)
	    	
		f.SetParameter(1,0.56)
	    	f.SetParLimits(1,0.3,0.7)
	    	
		f.SetParameter(2,0.02)
	    	f.SetParLimits(2,0,0.1)
	    	
		f.SetParameter(3,0.02)
	    	f.SetParLimits(3,0,0.1)
	    	
		f.SetParameter(4,0.71)
	    	f.SetParLimits(4,0.3,1)
	    	
		f.SetParameter(5,0.07)
	    	f.SetParLimits(5,0,0.2)
	   
		f.SetParameter(6,0.006)
	    	f.SetParLimits(6,0,0.1)
	    	
		f.SetParameter(7,0.82)
	    	f.SetParLimits(7,0.6,1)
	    	
		f.SetParameter(8,0.04)
	    	f.SetParLimits(8,0,0.1)
	   
		hist.Fit(f,"S",'',0,1.0)
		f1 = TF1("gaus1","gaus",0,1.0)
	    	f2 = TF1("gaus2","gaus",0,1.0)
	    	f3 = TF1("gaus3","gaus",0,1.0)
		
		f1.SetParameter(0,f.GetParameter(0))
	    	f1.SetParameter(1,f.GetParameter(1))
	    	f1.SetParameter(2,f.GetParameter(2))
	    	f2.SetParameter(0,f.GetParameter(3))
	    	f2.SetParameter(1,f.GetParameter(4))
	    	f2.SetParameter(2,f.GetParameter(5))
	    	f3.SetParameter(0,f.GetParameter(6))
	    	f3.SetParameter(1,f.GetParameter(7))
	    	f3.SetParameter(2,f.GetParameter(8))
	    	f1.SetLineColor(6)
	    	f2.SetLineColor(3)
	    	f3.SetLineColor(5)
		legend.SetHeader("Fit range : 0.4 - 1.0","C")
		legend.AddEntry(a,"MC","le")
		legend.AddEntry("f","total func","l")
		legend.AddEntry("f1","gaus1","l")
		legend.AddEntry("f2","gaus2","l")
		legend.AddEntry("f3","gaus3","l")

		rp = TRatioPlot(hist)
		rp.Draw()
		rp.GetUpperPad().cd()
	    	f1.Draw("same")
	    	f2.Draw("same")
	    	f3.Draw("same")
		legend.Draw()
		rp.GetLowerRefGraph().SetMinimum(-5)
		rp.GetLowerRefGraph().SetMaximum(5)
		
		mean_dict[str(SampleEnergy)+"_"+variable] = hist.GetMean()

	    elif SampleEnergy == "15GeV":
		f = TF1("triplegaus","gaus(0)+gaus(3)+gaus(6)",0.4,1)
	    	f.SetParName(0,"gaus1.Constant")
	    	f.SetParName(1,"gaus1.Mean")
	    	f.SetParName(2,"gaus1.Sigma")
	    	f.SetParName(3,"gaus2.Constant")
	    	f.SetParName(4,"gaus2.Mean")
	    	f.SetParName(5,"gaus2.Sigma")
	    	f.SetParName(6,"gaus3.Constant")
	    	f.SetParName(7,"gaus3.Mean")
	    	f.SetParName(8,"gaus3.Sigma")
	  
		# Initial value and limit
	    	f.SetParameter(0,0.02)
	    	f.SetParLimits(0,0,01)
	    	
		f.SetParameter(1,0.56)
	    	f.SetParLimits(1,0.3,0.7)
	    	
		f.SetParameter(2,0.02)
	    	f.SetParLimits(2,0,0.1)
	    	
		f.SetParameter(3,0.02)
	    	f.SetParLimits(3,0,0.1)
	    	
		f.SetParameter(4,0.71)
	    	f.SetParLimits(4,0.3,1)
	    	
		f.SetParameter(5,0.07)
	    	f.SetParLimits(5,0,0.2)
	   
		f.SetParameter(6,0.006)
	    	f.SetParLimits(6,0,0.1)
	    	
		f.SetParameter(7,0.82)
	    	f.SetParLimits(7,0.6,1)
	    	
		f.SetParameter(8,0.04)
	    	f.SetParLimits(8,0,0.1)
	   
		hist.Fit(f,"S",'',0,1.0)
		f1 = TF1("gaus1","gaus",0,1.0)
	    	f2 = TF1("gaus2","gaus",0,1.0)
	    	f3 = TF1("gaus3","gaus",0,1.0)
		
		f1.SetParameter(0,f.GetParameter(0))
	    	f1.SetParameter(1,f.GetParameter(1))
	    	f1.SetParameter(2,f.GetParameter(2))
	    	f2.SetParameter(0,f.GetParameter(3))
	    	f2.SetParameter(1,f.GetParameter(4))
	    	f2.SetParameter(2,f.GetParameter(5))
	    	f3.SetParameter(0,f.GetParameter(6))
	    	f3.SetParameter(1,f.GetParameter(7))
	    	f3.SetParameter(2,f.GetParameter(8))
	    	f1.SetLineColor(6)
	    	f2.SetLineColor(3)
	    	f3.SetLineColor(5)
		legend.SetHeader("Fit range : 0.4 - 1.0","C")
		legend.AddEntry(a,"MC","le")
		legend.AddEntry("f","total func","l")
		legend.AddEntry("f1","gaus1","l")
		legend.AddEntry("f2","gaus2","l")
		legend.AddEntry("f3","gaus3","l")

		rp = TRatioPlot(hist)
		rp.Draw()
		rp.GetUpperPad().cd()
	    	f1.Draw("same")
	    	f2.Draw("same")
	    	f3.Draw("same")
		legend.Draw()
		rp.GetLowerRefGraph().SetMinimum(-5)
		rp.GetLowerRefGraph().SetMaximum(5)
		
		mean_dict[str(SampleEnergy)+"_"+variable] = hist.GetMean()

	    elif SampleEnergy == "20GeV":
		f = TF1("triplegaus","gaus(0)+gaus(3)+gaus(6)",0.5,1.0)
	    	f.SetParName(0,"gaus1.Constant")
	    	f.SetParName(1,"gaus1.Mean")
	    	f.SetParName(2,"gaus1.Sigma")
	    	f.SetParName(3,"gaus2.Constant")
	    	f.SetParName(4,"gaus2.Mean")
	    	f.SetParName(5,"gaus2.Sigma")
	    	f.SetParName(6,"gaus3.Constant")
	    	f.SetParName(7,"gaus3.Mean")
	    	f.SetParName(8,"gaus3.Sigma")
	  
		# Initial value and limit
	    	f.SetParameter(0,0.01)
	    	f.SetParLimits(0,0,0.1)
	    	
		f.SetParameter(1,0.7)
	    	f.SetParLimits(1,0.3,1)
	    	
		f.SetParameter(2,0.01)
	    	f.SetParLimits(2,0,0.1)
	    	
		f.SetParameter(3,0.01)
	    	f.SetParLimits(3,0.001,0.1)
	    	
		f.SetParameter(4,0.7)
	    	f.SetParLimits(4,0.3,1)
	    	
		f.SetParameter(5,0.01)
	    	f.SetParLimits(5,0,0.5)
	   
		f.SetParameter(6,0.01)
	    	f.SetParLimits(6,0,0.1)
	    	
		f.SetParameter(7,0.8)
	    	f.SetParLimits(7,0.6,1)
	    	
		f.SetParameter(8,0.01)
	    	f.SetParLimits(8,0,0.1)
	   
		hist.Fit(f,"S",'',0,1.0)
		f1 = TF1("gaus1","gaus",0,1.0)
	    	f2 = TF1("gaus2","gaus",0,1.0)
	    	f3 = TF1("gaus3","gaus",0,1.0)
		
		f1.SetParameter(0,f.GetParameter(0))
	    	f1.SetParameter(1,f.GetParameter(1))
	    	f1.SetParameter(2,f.GetParameter(2))
	    	f2.SetParameter(0,f.GetParameter(3))
	    	f2.SetParameter(1,f.GetParameter(4))
	    	f2.SetParameter(2,f.GetParameter(5))
	    	f3.SetParameter(0,f.GetParameter(6))
	    	f3.SetParameter(1,f.GetParameter(7))
	    	f3.SetParameter(2,f.GetParameter(8))
	    	f1.SetLineColor(6)
	    	f2.SetLineColor(3)
	    	f3.SetLineColor(5)
		legend.SetHeader("Fit range : 0.5 - 1.0","C")
		legend.AddEntry(a,"MC","le")
		legend.AddEntry("f","total func","l")
		legend.AddEntry("f1","gaus1","l")
		legend.AddEntry("f2","gaus2","l")
		legend.AddEntry("f3","gaus3","l")
		
		rp = TRatioPlot(hist)
		rp.Draw()
		rp.GetUpperPad().cd()
	    	f1.Draw("same")
	    	f2.Draw("same")
	    	f3.Draw("same")
		legend.Draw()
		rp.GetLowerRefGraph().SetMinimum(-5)
		rp.GetLowerRefGraph().SetMaximum(5)
		
		mean_dict[str(SampleEnergy)+"_"+variable] = hist.GetMean()

	    elif SampleEnergy == "30GeV":
		f = TF1("triplegaus","gaus(0)+gaus(3)+gaus(6)",0.5,1.0)
	    	f.SetParName(0,"gaus1.Constant")
	    	f.SetParName(1,"gaus1.Mean")
	    	f.SetParName(2,"gaus1.Sigma")
	    	f.SetParName(3,"gaus2.Constant")
	    	f.SetParName(4,"gaus2.Mean")
	    	f.SetParName(5,"gaus2.Sigma")
	    	f.SetParName(6,"gaus3.Constant")
	    	f.SetParName(7,"gaus3.Mean")
	    	f.SetParName(8,"gaus3.Sigma")
	  
		# Initial value and limit
	    	f.SetParameter(0,0.01)
	    	f.SetParLimits(0,0,0.1)
	    	
		f.SetParameter(1,0.7)
	    	f.SetParLimits(1,0.3,1)
	    	
		f.SetParameter(2,0.01)
	    	f.SetParLimits(2,0,0.1)
	    	
		f.SetParameter(3,0.01)
	    	f.SetParLimits(3,0.001,0.1)
	    	
		f.SetParameter(4,0.7)
	    	f.SetParLimits(4,0.3,1)
	    	
		f.SetParameter(5,0.01)
	    	f.SetParLimits(5,0,0.5)
	   
		f.SetParameter(6,0.01)
	    	f.SetParLimits(6,0,0.1)
	    	
		f.SetParameter(7,0.8)
	    	f.SetParLimits(7,0.6,1)
	    	
		f.SetParameter(8,0.01)
	    	f.SetParLimits(8,0,0.1)
	   
		hist.Fit(f,"S",'',0,1.0)
		f1 = TF1("gaus1","gaus",0,1.0)
	    	f2 = TF1("gaus2","gaus",0,1.0)
	    	f3 = TF1("gaus3","gaus",0,1.0)
		
		f1.SetParameter(0,f.GetParameter(0))
	    	f1.SetParameter(1,f.GetParameter(1))
	    	f1.SetParameter(2,f.GetParameter(2))
	    	f2.SetParameter(0,f.GetParameter(3))
	    	f2.SetParameter(1,f.GetParameter(4))
	    	f2.SetParameter(2,f.GetParameter(5))
	    	f3.SetParameter(0,f.GetParameter(6))
	    	f3.SetParameter(1,f.GetParameter(7))
	    	f3.SetParameter(2,f.GetParameter(8))
	    	f1.SetLineColor(6)
	    	f2.SetLineColor(3)
	    	f3.SetLineColor(5)
		legend.SetHeader("Fit range : 0.5 - 1.0","C")
		legend.AddEntry(a,"MC","le")
		legend.AddEntry("f","total func","l")
		legend.AddEntry("f1","gaus1","l")
		legend.AddEntry("f2","gaus2","l")
		legend.AddEntry("f3","gaus3","l")
		
		rp = TRatioPlot(hist)
		rp.Draw()
		rp.GetUpperPad().cd()
	    	f1.Draw("same")
	    	f2.Draw("same")
	    	f3.Draw("same")
		legend.Draw()
		rp.GetLowerRefGraph().SetMinimum(-5)
		rp.GetLowerRefGraph().SetMaximum(5)
		
		mean_dict[str(SampleEnergy)+"_"+variable] = hist.GetMean()

	    elif SampleEnergy == "40GeV":
		f = TF1("triplegaus","gaus(0)+gaus(3)+gaus(6)",0.5,1.0)
	    	f.SetParName(0,"gaus1.Constant")
	    	f.SetParName(1,"gaus1.Mean")
	    	f.SetParName(2,"gaus1.Sigma")
	    	f.SetParName(3,"gaus2.Constant")
	    	f.SetParName(4,"gaus2.Mean")
	    	f.SetParName(5,"gaus2.Sigma")
	    	f.SetParName(6,"gaus3.Constant")
	    	f.SetParName(7,"gaus3.Mean")
	    	f.SetParName(8,"gaus3.Sigma")
	  
		# Initial value and limit
	    	f.SetParameter(0,0.01)
	    	f.SetParLimits(0,0,0.1)
	    	
		f.SetParameter(1,0.7)
	    	f.SetParLimits(1,0.3,1)
	    	
		f.SetParameter(2,0.01)
	    	f.SetParLimits(2,0,0.1)
	    	
		f.SetParameter(3,0.01)
	    	f.SetParLimits(3,0.001,0.1)
	    	
		f.SetParameter(4,0.7)
	    	f.SetParLimits(4,0.3,1)
	    	
		f.SetParameter(5,0.01)
	    	f.SetParLimits(5,0,0.5)
	   
		f.SetParameter(6,0.01)
	    	f.SetParLimits(6,0,0.1)
	    	
		f.SetParameter(7,0.8)
	    	f.SetParLimits(7,0.6,1)
	    	
		f.SetParameter(8,0.01)
	    	f.SetParLimits(8,0,0.1)
	   
		hist.Fit(f,"S",'',0,1.0)
		f1 = TF1("gaus1","gaus",0,1.0)
	    	f2 = TF1("gaus2","gaus",0,1.0)
	    	f3 = TF1("gaus3","gaus",0,1.0)
		
		f1.SetParameter(0,f.GetParameter(0))
	    	f1.SetParameter(1,f.GetParameter(1))
	    	f1.SetParameter(2,f.GetParameter(2))
	    	f2.SetParameter(0,f.GetParameter(3))
	    	f2.SetParameter(1,f.GetParameter(4))
	    	f2.SetParameter(2,f.GetParameter(5))
	    	f3.SetParameter(0,f.GetParameter(6))
	    	f3.SetParameter(1,f.GetParameter(7))
	    	f3.SetParameter(2,f.GetParameter(8))
	    	f1.SetLineColor(6)
	    	f2.SetLineColor(3)
	    	f3.SetLineColor(5)
		legend.SetHeader("Fit range : 0.5 - 1.0","C")
		legend.AddEntry(a,"MC","le")
		legend.AddEntry("f","total func","l")
		legend.AddEntry("f1","gaus1","l")
		legend.AddEntry("f2","gaus2","l")
		legend.AddEntry("f3","gaus3","l")
		
		rp = TRatioPlot(hist)
		rp.Draw()
		rp.GetUpperPad().cd()
	    	f1.Draw("same")
	    	f2.Draw("same")
	    	f3.Draw("same")
		legend.Draw()
		rp.GetLowerRefGraph().SetMinimum(-5)
		rp.GetLowerRefGraph().SetMaximum(5)
		
		mean_dict[str(SampleEnergy)+"_"+variable] = hist.GetMean()

	    elif SampleEnergy == "50GeV":
		f = TF1("triplegaus","gaus(0)+gaus(3)+gaus(6)",0.4,1)
	    	f.SetParName(0,"gaus1.Constant")
	    	f.SetParName(1,"gaus1.Mean")
	    	f.SetParName(2,"gaus1.Sigma")
	    	f.SetParName(3,"gaus2.Constant")
	    	f.SetParName(4,"gaus2.Mean")
	    	f.SetParName(5,"gaus2.Sigma")
	    	f.SetParName(6,"gaus3.Constant")
	    	f.SetParName(7,"gaus3.Mean")
	    	f.SetParName(8,"gaus3.Sigma")
	  
		# Initial value and limit
	    	f.SetParameter(0,0.02)
	    	f.SetParLimits(0,0,01)
	    	
		f.SetParameter(1,0.7)
	    	f.SetParLimits(1,0.6,0.9)
	    	
		f.SetParameter(2,0.02)
	    	f.SetParLimits(2,0,0.1)
	    	
		f.SetParameter(3,0.02)
	    	f.SetParLimits(3,0,0.1)
	    	
		f.SetParameter(4,0.71)
	    	f.SetParLimits(4,0.3,1)
	    	
		f.SetParameter(5,0.07)
	    	f.SetParLimits(5,0,0.2)
	   
		f.SetParameter(6,0.006)
	    	f.SetParLimits(6,0,0.1)
	    	
		f.SetParameter(7,0.82)
	    	f.SetParLimits(7,0.6,1)
	    	
		f.SetParameter(8,0.04)
	    	f.SetParLimits(8,0,0.1)
	   
		hist.Fit(f,"S",'',0,1.0)
		f1 = TF1("gaus1","gaus",0,1.0)
	    	f2 = TF1("gaus2","gaus",0,1.0)
	    	f3 = TF1("gaus3","gaus",0,1.0)
		
		f1.SetParameter(0,f.GetParameter(0))
	    	f1.SetParameter(1,f.GetParameter(1))
	    	f1.SetParameter(2,f.GetParameter(2))
	    	f2.SetParameter(0,f.GetParameter(3))
	    	f2.SetParameter(1,f.GetParameter(4))
	    	f2.SetParameter(2,f.GetParameter(5))
	    	f3.SetParameter(0,f.GetParameter(6))
	    	f3.SetParameter(1,f.GetParameter(7))
	    	f3.SetParameter(2,f.GetParameter(8))
	    	f1.SetLineColor(6)
	    	f2.SetLineColor(3)
	    	f3.SetLineColor(5)
		legend.SetHeader("Fit range : 0.4 - 1.0","C")
		legend.AddEntry(a,"MC","le")
		legend.AddEntry("f","total func","l")
		legend.AddEntry("f1","gaus1","l")
		legend.AddEntry("f2","gaus2","l")
		legend.AddEntry("f3","gaus3","l")
		
		rp = TRatioPlot(hist)
		rp.Draw()
		rp.GetUpperPad().cd()
	    	f1.Draw("same")
	    	f2.Draw("same")
	    	f3.Draw("same")
		legend.Draw()
		rp.GetLowerRefGraph().SetMinimum(-5)
		rp.GetLowerRefGraph().SetMaximum(5)
		
		mean_dict[str(SampleEnergy)+"_"+variable] = hist.GetMean()

	    elif SampleEnergy == "70GeV":
		f = TF1("triplegaus","gaus(0)+gaus(3)+gaus(6)",0.4,1)
	    	f.SetParName(0,"gaus1.Constant")
	    	f.SetParName(1,"gaus1.Mean")
	    	f.SetParName(2,"gaus1.Sigma")
	    	f.SetParName(3,"gaus2.Constant")
	    	f.SetParName(4,"gaus2.Mean")
	    	f.SetParName(5,"gaus2.Sigma")
	    	f.SetParName(6,"gaus3.Constant")
	    	f.SetParName(7,"gaus3.Mean")
	    	f.SetParName(8,"gaus3.Sigma")
	  
		# Initial value and limit
	    	f.SetParameter(0,0.02)
	    	f.SetParLimits(0,0,01)
	    	
		f.SetParameter(1,0.7)
	    	f.SetParLimits(1,0.5,0.9)
	    	
		f.SetParameter(2,0.02)
	    	f.SetParLimits(2,0,0.1)
	    	
		f.SetParameter(3,0.02)
	    	f.SetParLimits(3,0,0.1)
	    	
		f.SetParameter(4,0.71)
	    	f.SetParLimits(4,0.3,1)
	    	
		f.SetParameter(5,0.07)
	    	f.SetParLimits(5,0,0.2)
	   
		f.SetParameter(6,0.006)
	    	f.SetParLimits(6,0,0.1)
	    	
		f.SetParameter(7,0.82)
	    	f.SetParLimits(7,0.6,1)
	    	
		f.SetParameter(8,0.04)
	    	f.SetParLimits(8,0,0.1)
	   
		hist.Fit(f,"S",'',0,1.0)
		f1 = TF1("gaus1","gaus",0,1.0)
	    	f2 = TF1("gaus2","gaus",0,1.0)
	    	f3 = TF1("gaus3","gaus",0,1.0)
		
		f1.SetParameter(0,f.GetParameter(0))
	    	f1.SetParameter(1,f.GetParameter(1))
	    	f1.SetParameter(2,f.GetParameter(2))
	    	f2.SetParameter(0,f.GetParameter(3))
	    	f2.SetParameter(1,f.GetParameter(4))
	    	f2.SetParameter(2,f.GetParameter(5))
	    	f3.SetParameter(0,f.GetParameter(6))
	    	f3.SetParameter(1,f.GetParameter(7))
	    	f3.SetParameter(2,f.GetParameter(8))
	    	f1.SetLineColor(6)
	    	f2.SetLineColor(3)
	    	f3.SetLineColor(5)
		legend.SetHeader("Fit range : 0.4 - 1.0","C")
		legend.AddEntry(a,"MC","le")
		legend.AddEntry("f","total func","l")
		legend.AddEntry("f1","gaus1","l")
		legend.AddEntry("f2","gaus2","l")
		legend.AddEntry("f3","gaus3","l")
		
		rp = TRatioPlot(hist)
		rp.Draw()
		rp.GetUpperPad().cd()
	    	f1.Draw("same")
	    	f2.Draw("same")
	    	f3.Draw("same")
		legend.Draw()
		rp.GetLowerRefGraph().SetMinimum(-5)
		rp.GetLowerRefGraph().SetMaximum(5)
		
		mean_dict[str(SampleEnergy)+"_"+variable] = hist.GetMean()

	    elif SampleEnergy == "100GeV":
		f = TF1("triplegaus","gaus(0)+gaus(3)+gaus(6)",0.4,1)
	    	f.SetParName(0,"gaus1.Constant")
	    	f.SetParName(1,"gaus1.Mean")
	    	f.SetParName(2,"gaus1.Sigma")
	    	f.SetParName(3,"gaus2.Constant")
	    	f.SetParName(4,"gaus2.Mean")
	    	f.SetParName(5,"gaus2.Sigma")
	    	f.SetParName(6,"gaus3.Constant")
	    	f.SetParName(7,"gaus3.Mean")
	    	f.SetParName(8,"gaus3.Sigma")
	  
		# Initial value and limit
	    	f.SetParameter(0,0.02)
	    	f.SetParLimits(0,0,01)
	    	
		f.SetParameter(1,0.7)
	    	f.SetParLimits(1,0.5,0.9)
	    	
		f.SetParameter(2,0.02)
	    	f.SetParLimits(2,0,0.1)
	    	
		f.SetParameter(3,0.02)
	    	f.SetParLimits(3,0,0.1)
	    	
		f.SetParameter(4,0.71)
	    	f.SetParLimits(4,0.3,1)
	    	
		f.SetParameter(5,0.07)
	    	f.SetParLimits(5,0,0.2)
	   
		f.SetParameter(6,0.006)
	    	f.SetParLimits(6,0,0.1)
	    	
		f.SetParameter(7,0.82)
	    	f.SetParLimits(7,0.6,1)
	    	
		f.SetParameter(8,0.04)
	    	f.SetParLimits(8,0,0.1)
	   
		hist.Fit(f,"S",'',0,1.0)
		f1 = TF1("gaus1","gaus",0,1.0)
	    	f2 = TF1("gaus2","gaus",0,1.0)
	    	f3 = TF1("gaus3","gaus",0,1.0)
		
		f1.SetParameter(0,f.GetParameter(0))
	    	f1.SetParameter(1,f.GetParameter(1))
	    	f1.SetParameter(2,f.GetParameter(2))
	    	f2.SetParameter(0,f.GetParameter(3))
	    	f2.SetParameter(1,f.GetParameter(4))
	    	f2.SetParameter(2,f.GetParameter(5))
	    	f3.SetParameter(0,f.GetParameter(6))
	    	f3.SetParameter(1,f.GetParameter(7))
	    	f3.SetParameter(2,f.GetParameter(8))
	    	f1.SetLineColor(6)
	    	f2.SetLineColor(3)
	    	f3.SetLineColor(5)
		legend.SetHeader("Fit range : 0.4 - 1.0","C")
		legend.AddEntry(a,"MC","le")
		legend.AddEntry("f","total func","l")
		legend.AddEntry("f1","gaus1","l")
		legend.AddEntry("f2","gaus2","l")
		legend.AddEntry("f3","gaus3","l")
		
		rp = TRatioPlot(hist)
		rp.Draw()
		rp.GetUpperPad().cd()
	    	f1.Draw("same")
	    	f2.Draw("same")
	    	f3.Draw("same")
		legend.Draw()
		rp.GetLowerRefGraph().SetMinimum(-5)
		rp.GetLowerRefGraph().SetMaximum(5)
		
		mean_dict[str(SampleEnergy)+"_"+variable] = hist.GetMean()

	    elif SampleEnergy == "150GeV" :
		f = TF1("triplegaus","gaus(0)+gaus(3)+gaus(6)",0.4,1)
	    	f.SetParName(0,"gaus1.Constant")
	    	f.SetParName(1,"gaus1.Mean")
	    	f.SetParName(2,"gaus1.Sigma")
	    	f.SetParName(3,"gaus2.Constant")
	    	f.SetParName(4,"gaus2.Mean")
	    	f.SetParName(5,"gaus2.Sigma")
	    	f.SetParName(6,"gaus3.Constant")
	    	f.SetParName(7,"gaus3.Mean")
	    	f.SetParName(8,"gaus3.Sigma")
	  
		# Initial value and limit
	    	f.SetParameter(0,0.02)
	    	f.SetParLimits(0,0,01)
	    	
		f.SetParameter(1,0.7)
	    	f.SetParLimits(1,0.5,0.9)
	    	
		f.SetParameter(2,0.02)
	    	f.SetParLimits(2,0,0.1)
	    	
		f.SetParameter(3,0.02)
	    	f.SetParLimits(3,0,0.1)
	    	
		f.SetParameter(4,0.71)
	    	f.SetParLimits(4,0.3,1)
	    	
		f.SetParameter(5,0.07)
	    	f.SetParLimits(5,0,0.2)
	   
		f.SetParameter(6,0.006)
	    	f.SetParLimits(6,0,0.1)
	    	
		f.SetParameter(7,0.82)
	    	f.SetParLimits(7,0.6,1)
	    	
		f.SetParameter(8,0.04)
	    	f.SetParLimits(8,0,0.1)
	   
		hist.Fit(f,"S",'',0,1.0)
		f1 = TF1("gaus1","gaus",0,1.0)
	    	f2 = TF1("gaus2","gaus",0,1.0)
	    	f3 = TF1("gaus3","gaus",0,1.0)
		
		f1.SetParameter(0,f.GetParameter(0))
	    	f1.SetParameter(1,f.GetParameter(1))
	    	f1.SetParameter(2,f.GetParameter(2))
	    	f2.SetParameter(0,f.GetParameter(3))
	    	f2.SetParameter(1,f.GetParameter(4))
	    	f2.SetParameter(2,f.GetParameter(5))
	    	f3.SetParameter(0,f.GetParameter(6))
	    	f3.SetParameter(1,f.GetParameter(7))
	    	f3.SetParameter(2,f.GetParameter(8))
	    	f1.SetLineColor(6)
	    	f2.SetLineColor(3)
	    	f3.SetLineColor(5)
		legend.SetHeader("Fit range : 0.4 - 1.0","C")
		legend.AddEntry(a,"MC","le")
		legend.AddEntry("f","total func","l")
		legend.AddEntry("f1","gaus1","l")
		legend.AddEntry("f2","gaus2","l")
		legend.AddEntry("f3","gaus3","l")
		
		rp = TRatioPlot(hist)
		rp.Draw()
		rp.GetUpperPad().cd()
	    	f1.Draw("same")
	    	f2.Draw("same")
	    	f3.Draw("same")
		legend.Draw()
		rp.GetLowerRefGraph().SetMinimum(-5)
		rp.GetLowerRefGraph().SetMaximum(5)
		
		mean_dict[str(SampleEnergy)+"_"+variable] = hist.GetMean()

	    elif SampleEnergy == "200GeV" :
		f = TF1("triplegaus","gaus(0)+gaus(3)+gaus(6)",0.4,1)
	    	f.SetParName(0,"gaus1.Constant")
	    	f.SetParName(1,"gaus1.Mean")
	    	f.SetParName(2,"gaus1.Sigma")
	    	f.SetParName(3,"gaus2.Constant")
	    	f.SetParName(4,"gaus2.Mean")
	    	f.SetParName(5,"gaus2.Sigma")
	    	f.SetParName(6,"gaus3.Constant")
	    	f.SetParName(7,"gaus3.Mean")
	    	f.SetParName(8,"gaus3.Sigma")
	  
		# Initial value and limit
	    	f.SetParameter(0,0.02)
	    	f.SetParLimits(0,0,01)
	    	
		f.SetParameter(1,0.7)
	    	f.SetParLimits(1,0.5,0.9)
	    	
		f.SetParameter(2,0.02)
	    	f.SetParLimits(2,0,0.1)
	    	
		f.SetParameter(3,0.02)
	    	f.SetParLimits(3,0,0.1)
	    	
		f.SetParameter(4,0.71)
	    	f.SetParLimits(4,0.3,1)
	    	
		f.SetParameter(5,0.07)
	    	f.SetParLimits(5,0,0.2)
	   
		f.SetParameter(6,0.006)
	    	f.SetParLimits(6,0,0.1)
	    	
		f.SetParameter(7,0.82)
	    	f.SetParLimits(7,0.6,1)
	    	
		f.SetParameter(8,0.04)
	    	f.SetParLimits(8,0,0.1)
	   
		hist.Fit(f,"S",'',0,1.0)
		f1 = TF1("gaus1","gaus",0,1.0)
	    	f2 = TF1("gaus2","gaus",0,1.0)
	    	f3 = TF1("gaus3","gaus",0,1.0)
		
		f1.SetParameter(0,f.GetParameter(0))
	    	f1.SetParameter(1,f.GetParameter(1))
	    	f1.SetParameter(2,f.GetParameter(2))
	    	f2.SetParameter(0,f.GetParameter(3))
	    	f2.SetParameter(1,f.GetParameter(4))
	    	f2.SetParameter(2,f.GetParameter(5))
	    	f3.SetParameter(0,f.GetParameter(6))
	    	f3.SetParameter(1,f.GetParameter(7))
	    	f3.SetParameter(2,f.GetParameter(8))
	    	f1.SetLineColor(6)
	    	f2.SetLineColor(3)
	    	f3.SetLineColor(5)
		legend.SetHeader("Fit range : 0.4 - 1.0","C")
		legend.AddEntry(a,"MC","le")
		legend.AddEntry("f","total func","l")
		legend.AddEntry("f1","gaus1","l")
		legend.AddEntry("f2","gaus2","l")
		legend.AddEntry("f3","gaus3","l")
		
		rp = TRatioPlot(hist)
		rp.Draw()
		rp.GetUpperPad().cd()
	    	f1.Draw("same")
	    	f2.Draw("same")
	    	f3.Draw("same")
		legend.Draw()
		rp.GetLowerRefGraph().SetMinimum(-5)
		rp.GetLowerRefGraph().SetMaximum(5)
		
		mean_dict[str(SampleEnergy)+"_"+variable] = hist.GetMean()

	    elif SampleEnergy == "300GeV" :
		f = TF1("triplegaus","gaus(0)+gaus(3)+gaus(6)",0.4,1)
	    	f.SetParName(0,"gaus1.Constant")
	    	f.SetParName(1,"gaus1.Mean")
	    	f.SetParName(2,"gaus1.Sigma")
	    	f.SetParName(3,"gaus2.Constant")
	    	f.SetParName(4,"gaus2.Mean")
	    	f.SetParName(5,"gaus2.Sigma")
	    	f.SetParName(6,"gaus3.Constant")
	    	f.SetParName(7,"gaus3.Mean")
	    	f.SetParName(8,"gaus3.Sigma")
	  
		# Initial value and limit
	    	f.SetParameter(0,0.02)
	    	f.SetParLimits(0,0,01)
	    	
		f.SetParameter(1,0.7)
	    	f.SetParLimits(1,0.5,0.9)
	    	
		f.SetParameter(2,0.02)
	    	f.SetParLimits(2,0,0.1)
	    	
		f.SetParameter(3,0.02)
	    	f.SetParLimits(3,0,0.1)
	    	
		f.SetParameter(4,0.71)
	    	f.SetParLimits(4,0.3,1)
	    	
		f.SetParameter(5,0.07)
	    	f.SetParLimits(5,0,0.2)
	   
		f.SetParameter(6,0.006)
	    	f.SetParLimits(6,0,0.1)
	    	
		f.SetParameter(7,0.82)
	    	f.SetParLimits(7,0.6,1)
	    	
		f.SetParameter(8,0.04)
	    	f.SetParLimits(8,0,0.1)
	   
		hist.Fit(f,"S",'',0,1.0)
		f1 = TF1("gaus1","gaus",0,1.0)
	    	f2 = TF1("gaus2","gaus",0,1.0)
	    	f3 = TF1("gaus3","gaus",0,1.0)
		
		f1.SetParameter(0,f.GetParameter(0))
	    	f1.SetParameter(1,f.GetParameter(1))
	    	f1.SetParameter(2,f.GetParameter(2))
	    	f2.SetParameter(0,f.GetParameter(3))
	    	f2.SetParameter(1,f.GetParameter(4))
	    	f2.SetParameter(2,f.GetParameter(5))
	    	f3.SetParameter(0,f.GetParameter(6))
	    	f3.SetParameter(1,f.GetParameter(7))
	    	f3.SetParameter(2,f.GetParameter(8))
	    	f1.SetLineColor(6)
	    	f2.SetLineColor(3)
	    	f3.SetLineColor(5)
		legend.SetHeader("Fit range : 0.4 - 1.0","C")
		legend.AddEntry(a,"MC","le")
		legend.AddEntry("f","total func","l")
		legend.AddEntry("f1","gaus1","l")
		legend.AddEntry("f2","gaus2","l")
		legend.AddEntry("f3","gaus3","l")
		
		rp = TRatioPlot(hist)
		rp.Draw()
		rp.GetUpperPad().cd()
	    	f1.Draw("same")
	    	f2.Draw("same")
	    	f3.Draw("same")
		legend.Draw()
		rp.GetLowerRefGraph().SetMinimum(-5)
		rp.GetLowerRefGraph().SetMaximum(5)
		
		mean_dict[str(SampleEnergy)+"_"+variable] = hist.GetMean()

	    elif SampleEnergy == "400GeV" :
		f = TF1("triplegaus","gaus(0)+gaus(3)+gaus(6)",0.4,1)
	    	f.SetParName(0,"gaus1.Constant")
	    	f.SetParName(1,"gaus1.Mean")
	    	f.SetParName(2,"gaus1.Sigma")
	    	f.SetParName(3,"gaus2.Constant")
	    	f.SetParName(4,"gaus2.Mean")
	    	f.SetParName(5,"gaus2.Sigma")
	    	f.SetParName(6,"gaus3.Constant")
	    	f.SetParName(7,"gaus3.Mean")
	    	f.SetParName(8,"gaus3.Sigma")
	  
		# Initial value and limit
	    	f.SetParameter(0,0.02)
	    	f.SetParLimits(0,0,01)
	    	
		f.SetParameter(1,0.7)
	    	f.SetParLimits(1,0.5,0.9)
	    	
		f.SetParameter(2,0.02)
	    	f.SetParLimits(2,0,0.1)
	    	
		f.SetParameter(3,0.02)
	    	f.SetParLimits(3,0,0.1)
	    	
		f.SetParameter(4,0.71)
	    	f.SetParLimits(4,0.3,1)
	    	
		f.SetParameter(5,0.07)
	    	f.SetParLimits(5,0,0.2)
	   
		f.SetParameter(6,0.006)
	    	f.SetParLimits(6,0,0.1)
	    	
		f.SetParameter(7,0.82)
	    	f.SetParLimits(7,0.6,1)
	    	
		f.SetParameter(8,0.04)
	    	f.SetParLimits(8,0,0.1)
	   
		hist.Fit(f,"S",'',0,1.0)
		f1 = TF1("gaus1","gaus",0,1.0)
	    	f2 = TF1("gaus2","gaus",0,1.0)
	    	f3 = TF1("gaus3","gaus",0,1.0)
		
		f1.SetParameter(0,f.GetParameter(0))
	    	f1.SetParameter(1,f.GetParameter(1))
	    	f1.SetParameter(2,f.GetParameter(2))
	    	f2.SetParameter(0,f.GetParameter(3))
	    	f2.SetParameter(1,f.GetParameter(4))
	    	f2.SetParameter(2,f.GetParameter(5))
	    	f3.SetParameter(0,f.GetParameter(6))
	    	f3.SetParameter(1,f.GetParameter(7))
	    	f3.SetParameter(2,f.GetParameter(8))
	    	f1.SetLineColor(6)
	    	f2.SetLineColor(3)
	    	f3.SetLineColor(5)
		legend.SetHeader("Fit range : 0.4 - 1.0","C")
		legend.AddEntry(a,"MC","le")
		legend.AddEntry("f","total func","l")
		legend.AddEntry("f1","gaus1","l")
		legend.AddEntry("f2","gaus2","l")
		legend.AddEntry("f3","gaus3","l")
		
		rp = TRatioPlot(hist)
		rp.Draw()
		rp.GetUpperPad().cd()
	    	f1.Draw("same")
	    	f2.Draw("same")
	    	f3.Draw("same")
		legend.Draw()
		rp.GetLowerRefGraph().SetMinimum(-5)
		rp.GetLowerRefGraph().SetMaximum(5)
		
		mean_dict[str(SampleEnergy)+"_"+variable] = hist.GetMean()

	    elif SampleEnergy == "500GeV" :
		f = TF1("triplegaus","gaus(0)+gaus(3)+gaus(6)",0.4,1)
	    	f.SetParName(0,"gaus1.Constant")
	    	f.SetParName(1,"gaus1.Mean")
	    	f.SetParName(2,"gaus1.Sigma")
	    	f.SetParName(3,"gaus2.Constant")
	    	f.SetParName(4,"gaus2.Mean")
	    	f.SetParName(5,"gaus2.Sigma")
	    	f.SetParName(6,"gaus3.Constant")
	    	f.SetParName(7,"gaus3.Mean")
	    	f.SetParName(8,"gaus3.Sigma")
	  
		# Initial value and limit
	    	f.SetParameter(0,0.02)
	    	f.SetParLimits(0,0,01)
	    	
		f.SetParameter(1,0.7)
	    	f.SetParLimits(1,0.5,0.9)
	    	
		f.SetParameter(2,0.02)
	    	f.SetParLimits(2,0,0.1)
	    	
		f.SetParameter(3,0.02)
	    	f.SetParLimits(3,0,0.1)
	    	
		f.SetParameter(4,0.71)
	    	f.SetParLimits(4,0.3,1)
	    	
		f.SetParameter(5,0.07)
	    	f.SetParLimits(5,0,0.2)
	   
		f.SetParameter(6,0.006)
	    	f.SetParLimits(6,0,0.1)
	    	
		f.SetParameter(7,0.82)
	    	f.SetParLimits(7,0.6,1)
	    	
		f.SetParameter(8,0.04)
	    	f.SetParLimits(8,0,0.1)
	   
		hist.Fit(f,"S",'',0,1.0)
		f1 = TF1("gaus1","gaus",0,1.0)
	    	f2 = TF1("gaus2","gaus",0,1.0)
	    	f3 = TF1("gaus3","gaus",0,1.0)
		
		f1.SetParameter(0,f.GetParameter(0))
	    	f1.SetParameter(1,f.GetParameter(1))
	    	f1.SetParameter(2,f.GetParameter(2))
	    	f2.SetParameter(0,f.GetParameter(3))
	    	f2.SetParameter(1,f.GetParameter(4))
	    	f2.SetParameter(2,f.GetParameter(5))
	    	f3.SetParameter(0,f.GetParameter(6))
	    	f3.SetParameter(1,f.GetParameter(7))
	    	f3.SetParameter(2,f.GetParameter(8))
	    	f1.SetLineColor(6)
	    	f2.SetLineColor(3)
	    	f3.SetLineColor(5)
		legend.SetHeader("Fit range : 0.4 - 1.0","C")
		legend.AddEntry(a,"MC","le")
		legend.AddEntry("f","total func","l")
		legend.AddEntry("f1","gaus1","l")
		legend.AddEntry("f2","gaus2","l")
		legend.AddEntry("f3","gaus3","l")
		
		rp = TRatioPlot(hist)
		rp.Draw()
		rp.GetUpperPad().cd()
	    	f1.Draw("same")
	    	f2.Draw("same")
	    	f3.Draw("same")
		legend.Draw()
		rp.GetLowerRefGraph().SetMinimum(-5)
		rp.GetLowerRefGraph().SetMaximum(5)
		
		mean_dict[str(SampleEnergy)+"_"+variable] = hist.GetMean()

	    else : 
		print 'Dont have this energy'
		quit()

	elif variable == "fPi0" :
	    ROOT.gStyle.SetStatY(0.9);                
    	    ROOT.gStyle.SetStatX(0.9);                
    	    ROOT.gStyle.SetStatW(0.15);                
    	    ROOT.gStyle.SetStatH(0.15);                
    	    #ROOT.gStyle.SetOptStat(0)
	    if SampleEnergy == "1GeV":
		f = TF1("landaugaus","landau(0)+gaus(3)",0.1,1)
	    	f.SetParName(0,"landau.Constant")
	    	f.SetParName(1,"landau.MPV")
	    	f.SetParName(2,"landau.Sigma")
	    	f.SetParName(3,"gaus.Constant")
	    	f.SetParName(4,"gaus.Mean")
	    	f.SetParName(5,"gaus.Sigma")
	  
		# Initial value and limit
	    	f.SetParameter(0,0.1)
	    	f.SetParLimits(0,0,1)
	    	
		f.SetParameter(1,0.25)
	    	f.SetParLimits(1,0,0.3)
	    	
		f.SetParameter(2,0.1)
	    	f.SetParLimits(2,0,1)
	    	
	    	f.SetParameter(3,0.1)
	    	f.SetParLimits(3,0,0.5)
	    	
		f.SetParameter(4,0.7)
	    	f.SetParLimits(4,0.3,1)
	    	
		f.SetParameter(5,0.1)
	    	f.SetParLimits(5,0,1)
	    	
		hist.Fit(f,"S",'',0.1,1)
		flandau = TF1("landau","landau",0,1.0)
		fgaus = TF1("gaus","gaus",0,1.0)
		
		flandau.SetParameter(0,f.GetParameter(0))
	    	flandau.SetParameter(1,f.GetParameter(1))
	    	flandau.SetParameter(2,f.GetParameter(2))
	    	fgaus.SetParameter(0,f.GetParameter(3))
	    	fgaus.SetParameter(1,f.GetParameter(4))
	    	fgaus.SetParameter(2,f.GetParameter(5))
	    	flandau.SetLineColor(6)
	    	fgaus.SetLineColor(3)
		
                legend.SetHeader("Fit range : 0.1 - 1.0","C")
		legend.AddEntry(a,"MC","le")
		legend.AddEntry("f","total func","l")
		legend.AddEntry("f1","landau","l")
		legend.AddEntry("f2","gaus","l")
	    
		rp = TRatioPlot(hist)
		rp.Draw()
		rp.GetUpperPad().cd()
	    	flandau.Draw("same")
	    	fgaus.Draw("same")
		legend.Draw()
		rp.GetLowerRefGraph().SetMinimum(-5)
		rp.GetLowerRefGraph().SetMaximum(5)
		
	    elif SampleEnergy == "2GeV":
		f = TF1("landaudoublegaus","landau(0)+gaus(3)+gaus(6)",0,1)
	    	f.SetParName(0,"landau.Constant")
	    	f.SetParName(1,"landau.MPV")
	    	f.SetParName(2,"landau.Sigma")
	    	f.SetParName(3,"gaus1.Constant")
	    	f.SetParName(4,"gaus1.Mean")
	    	f.SetParName(5,"gaus1.Sigma")
	    	f.SetParName(6,"gaus2.Constant")
	    	f.SetParName(7,"gaus2.Mean")
	    	f.SetParName(8,"gaus2.Sigma")
	  
		# Initial value and limit
	    	f.SetParameter(0,0.1)
	    	f.SetParLimits(0,0,1)
	    	
		f.SetParameter(1,0.15)
	    	f.SetParLimits(1,0,0.3)
	    	
		f.SetParameter(2,0.03)
	    	f.SetParLimits(2,0,0.1)
	    	
	    	f.SetParameter(3,0.1)
	    	f.SetParLimits(3,0,1)
	    	
		f.SetParameter(4,0.25)
	    	f.SetParLimits(4,0.1,0.4)
	    	
		f.SetParameter(5,0.1)
	    	f.SetParLimits(5,0,1)
	    	
	    	f.SetParameter(6,0.1)
	    	f.SetParLimits(6,0,1)
	    	
		f.SetParameter(7,0.5)
	    	f.SetParLimits(7,0.3,0.7)
	    	
		f.SetParameter(8,0.1)
	    	f.SetParLimits(8,0,1)
		
		hist.Fit(f,"S",'',0,1)
		flandau = TF1("landau","landau",0,1.0)
		fgaus1 = TF1("gaus","gaus",0,1.0)
		fgaus2 = TF1("gaus","gaus",0,1.0)
		
		flandau.SetParameter(0,f.GetParameter(0))
	    	flandau.SetParameter(1,f.GetParameter(1))
	    	flandau.SetParameter(2,f.GetParameter(2))
	    	fgaus1.SetParameter(0,f.GetParameter(3))
	    	fgaus1.SetParameter(1,f.GetParameter(4))
	    	fgaus1.SetParameter(2,f.GetParameter(5))
	    	fgaus2.SetParameter(0,f.GetParameter(6))
	    	fgaus2.SetParameter(1,f.GetParameter(7))
	    	fgaus2.SetParameter(2,f.GetParameter(8))
	    	flandau.SetLineColor(6)
	    	fgaus1.SetLineColor(3)
	    	fgaus2.SetLineColor(5)
	    	flandau.Draw("same")
		
                legend.SetHeader("Fit range : 0.1 - 1.0","C")
		legend.AddEntry(a,"MC","le")
		legend.AddEntry("f","total func","l")
		#legend.AddEntry("f1","landau","l")
		#legend.AddEntry("f2","gaus1","l")
		#legend.AddEntry("f2","gaus2","l")
		
                rp = TRatioPlot(hist)
		rp.Draw()
		rp.GetUpperPad().cd()
	    	flandau.Draw("same")
	    	fgaus1.Draw("same")
	    	fgaus2.Draw("same")
		legend.Draw()
		rp.GetLowerRefGraph().SetMinimum(-5)
		rp.GetLowerRefGraph().SetMaximum(5)
		
	    
	    elif SampleEnergy == "5GeV":
		f = TF1("doublelandaugaus","landau(0)+landau(3)+gaus(6)",0,1)
		#f = TF1("doublegauslandau","landau(0)+gaus(3)+gaus(6)",0,1)
		#f = TF1("triplegaus","gaus(0)+gaus(3)+gaus(6)",0,1)
	    	f.SetParName(0,"landau1.Constant")
	    	f.SetParName(1,"landau1.MPV")
	    	f.SetParName(2,"landau1.Sigma")
	    	f.SetParName(3,"landau2.Constant")
	    	f.SetParName(4,"landau2.MPV")
	    	f.SetParName(5,"landau2.Sigma")
	    	f.SetParName(6,"gaus.Constant")
	    	f.SetParName(7,"gaus.Mean")
	    	f.SetParName(8,"gaus.Sigma")
	  
		
		# Initial value and limit
	    	f.SetParameter(0,0.1)
	    	f.SetParLimits(0,0.01,1)
	    	
		f.SetParameter(1,0.05)
	    	f.SetParLimits(1,0.01,1)
	    	
		f.SetParameter(2,0.1)
	    	f.SetParLimits(2,0.01,1)
	    	
	    	f.SetParameter(3,0.1)
	    	f.SetParLimits(3,0.01,1)
	    	
		f.SetParameter(4,0.1)
	    	f.SetParLimits(4,0.01,1)
	    	
		f.SetParameter(5,0.1)
	    	f.SetParLimits(5,0.01,1)
	    	
	    	f.SetParameter(6,0.1)
	    	f.SetParLimits(6,0.01,1)
	    	
		f.SetParameter(7,0.05)
	    	f.SetParLimits(7,0.01,1)
	    	
		f.SetParameter(8,0.1)
	    	f.SetParLimits(8,0.01,0.2)
		
		hist.Fit(f,"S",'',0,1)
		f1 = TF1("landau1","landau",0,0.1)
		f2 = TF1("landau2","landau",0.05,1.0)
		f3 = TF1("gaus","gaus",0,1.0)
		
		f1.SetParameter(0,f.GetParameter(0))
	    	f1.SetParameter(1,f.GetParameter(1))
	    	f1.SetParameter(2,f.GetParameter(2))
	    	f2.SetParameter(0,f.GetParameter(3))
	    	f2.SetParameter(1,f.GetParameter(4))
	    	f2.SetParameter(2,f.GetParameter(5))
	    	f3.SetParameter(0,f.GetParameter(6))
	    	f3.SetParameter(1,f.GetParameter(7))
	    	f3.SetParameter(2,f.GetParameter(8))
	    	f1.SetLineColor(6)
	    	f2.SetLineColor(3)
	    	f3.SetLineColor(5)
	    
                legend.SetHeader("Fit range : 0.1 - 1.0","C")
		legend.AddEntry(a,"MC","le")
		legend.AddEntry("f","total func","l")
		#legend.AddEntry("f1","landau","l")
		#legend.AddEntry("f2","gaus","l")
		
                rp = TRatioPlot(hist)
		rp.Draw()
		rp.GetUpperPad().cd()
	    	f1.Draw("same")
	    	f2.Draw("same")
	    	f3.Draw("same")
		legend.Draw()
		rp.GetLowerRefGraph().SetMinimum(-5)
		rp.GetLowerRefGraph().SetMaximum(5)
	    
            elif SampleEnergy == "7GeV":
	        f = TF1("doublelandaugaus","landau(0)+landau(3)+gaus(6)",0,1)
	    	f.SetParName(0,"landau1.Constant")
	    	f.SetParName(1,"landau1.MPV")
	    	f.SetParName(2,"landau1.Sigma")
	    	f.SetParName(3,"landau2.Constant")
	    	f.SetParName(4,"landau2.MPV")
	    	f.SetParName(5,"landau2.Sigma")
	    	f.SetParName(6,"gaus2.Constant")
	    	f.SetParName(7,"gaus2.Mean")
	    	f.SetParName(8,"gaus2.Sigma")
	  
	        
	        # Initial value and limit
	    	f.SetParameter(0,0.1)
	    	f.SetParLimits(0,0.01,1)
	    	
	        f.SetParameter(1,0.1)
	    	f.SetParLimits(1,0.01,1)
	    	
	        f.SetParameter(2,0.1)
	    	f.SetParLimits(2,0.01,1)
	    	
	    	f.SetParameter(3,0.1)
	    	f.SetParLimits(3,0.01,1)
	    	
	        f.SetParameter(4,0.1)
	    	f.SetParLimits(4,0.01,1)
	    	
	        f.SetParameter(5,0.1)
	    	f.SetParLimits(5,0.01,1)
	    	
	    	f.SetParameter(6,0.1)
	    	f.SetParLimits(6,0.01,1)
	    	
	        f.SetParameter(7,0.05)
	    	f.SetParLimits(7,0.01,1)
	    	
	        f.SetParameter(8,0.1)
	    	f.SetParLimits(8,0.01,0.2)
	        
                hist.Fit(f,"S",'',0,1)
	        f1 = TF1("landau1","landau",0,1.0)
	        f2 = TF1("landau2","landau",0,1.0)
	        f3 = TF1("gaus","gaus",0,1.0)
	        
	        f1.SetParameter(0,f.GetParameter(0))
	    	f1.SetParameter(1,f.GetParameter(1))
	    	f1.SetParameter(2,f.GetParameter(2))
	    	f2.SetParameter(0,f.GetParameter(3))
	    	f2.SetParameter(1,f.GetParameter(4))
	    	f2.SetParameter(2,f.GetParameter(5))
	    	f3.SetParameter(0,f.GetParameter(6))
	    	f3.SetParameter(1,f.GetParameter(7))
	    	f3.SetParameter(2,f.GetParameter(8))
	    	f1.SetLineColor(6)
	    	f2.SetLineColor(3)
	    	f3.SetLineColor(5)
	    
                legend.SetHeader("Fit range : 0.1 - 1.0","C")
		legend.AddEntry(a,"MC","le")
		legend.AddEntry("f","total func","l")
		#legend.AddEntry("f1","landau","l")
		#legend.AddEntry("f2","gaus","l")
	        
                rp = TRatioPlot(hist)
	        rp.Draw()
	        rp.GetUpperPad().cd()
	    	f1.Draw("same")
	    	f2.Draw("same")
	    	f3.Draw("same")
	        legend.Draw()
	        rp.GetLowerRefGraph().SetMinimum(-5)
	        rp.GetLowerRefGraph().SetMaximum(5)
	    
	#    elif SampleEnergy == "10GeV":
	#	f = TF1("landaugaus","landau(0)+gaus(3)",0,1)
	#    	f.SetParName(0,"landau.Constant")
	#    	f.SetParName(1,"landau.MPV")
	#    	f.SetParName(2,"landau.Sigma")
	#    	f.SetParName(3,"gaus.Constant")
	#    	f.SetParName(4,"gaus.Mean")
	#    	f.SetParName(5,"gaus.Sigma")
	#  
	#	# Initial value and limit
	#    	f.SetParameter(0,0.1)
	#    	f.SetParLimits(0,0.01,1)
	#    	
	#	f.SetParameter(1,0.1)
	#    	f.SetParLimits(1,0.01,1)
	#    	
	#	f.SetParameter(2,0.1)
	#    	f.SetParLimits(2,0.01,1)
	#    	
	#    	f.SetParameter(3,0.1)
	#    	f.SetParLimits(3,0.01,1)
	#    	
	#	f.SetParameter(4,0.1)
	#    	f.SetParLimits(4,0.01,1)
	#    	
	#	f.SetParameter(5,0.1)
	#    	f.SetParLimits(5,0.01,1)
	#    	
	#	hist.Fit(f,"S",'',0,1)
	#	f1 = TF1("landau","landau",0,1.0)
	#	f2 = TF1("gaus","gaus",0,1.0)
	#	
	#	f1.SetParameter(0,f.GetParameter(0))
	#    	f1.SetParameter(1,f.GetParameter(1))
	#    	f1.SetParameter(2,f.GetParameter(2))
	#    	f2.SetParameter(0,f.GetParameter(3))
	#    	f2.SetParameter(1,f.GetParameter(4))
	#    	f2.SetParameter(2,f.GetParameter(5))
	#    	f1.SetLineColor(6)
	#    	f2.SetLineColor(3)
	#    
	#	rp = TRatioPlot(hist)
	#	rp.Draw()
	#	rp.GetUpperPad().cd()
	#    	f1.Draw("same")
	#    	f2.Draw("same")
	#	legend.Draw()
	#	rp.GetLowerRefGraph().SetMinimum(-5)
	#	rp.GetLowerRefGraph().SetMaximum(5)
		
	    elif SampleEnergy == "10GeV":
		#f = TF1("doublelandaugaus","landau(0)+landau(3)+gaus(6)",0,1)
		f = TF1("doublegauslandau","landau(0)+gaus(3)+gaus(6)",0,1)
		#f = TF1("triplegaus","gaus(0)+gaus(3)+gaus(6)",0,1)
	    	f.SetParName(0,"landau1.Constant")
	    	f.SetParName(1,"landau1.MPV")
	    	f.SetParName(2,"landau1.Sigma")
	    	f.SetParName(3,"landau2.Constant")
	    	f.SetParName(4,"landau2.MPV")
	    	f.SetParName(5,"landau2.Sigma")
	    	f.SetParName(6,"gaus.Constant")
	    	f.SetParName(7,"gaus.Mean")
	    	f.SetParName(8,"gaus.Sigma")
	  
		
		# Initial value and limit
	    	f.SetParameter(0,0.1)
	    	f.SetParLimits(0,0.01,1)
	    	
		f.SetParameter(1,0.05)
	    	f.SetParLimits(1,0.01,1)
	    	
		f.SetParameter(2,0.1)
	    	f.SetParLimits(2,0.01,1)
	    	
	    	f.SetParameter(3,0.1)
	    	f.SetParLimits(3,0.01,1)
	    	
		f.SetParameter(4,0.1)
	    	f.SetParLimits(4,0.01,1)
	    	
		f.SetParameter(5,0.1)
	    	f.SetParLimits(5,0.01,1)
	    	
	    	f.SetParameter(6,0.1)
	    	f.SetParLimits(6,0.01,1)
	    	
		f.SetParameter(7,0.05)
	    	f.SetParLimits(7,0.01,1)
	    	
		f.SetParameter(8,0.1)
	    	f.SetParLimits(8,0.01,0.2)
		
		hist.Fit(f,"S",'',0,1)
		f1 = TF1("landau1","landau",0,0.1)
		f2 = TF1("landau2","landau",0.05,1.0)
		f3 = TF1("gaus","gaus",0,1.0)
		
		f1.SetParameter(0,f.GetParameter(0))
	    	f1.SetParameter(1,f.GetParameter(1))
	    	f1.SetParameter(2,f.GetParameter(2))
	    	f2.SetParameter(0,f.GetParameter(3))
	    	f2.SetParameter(1,f.GetParameter(4))
	    	f2.SetParameter(2,f.GetParameter(5))
	    	f3.SetParameter(0,f.GetParameter(6))
	    	f3.SetParameter(1,f.GetParameter(7))
	    	f3.SetParameter(2,f.GetParameter(8))
	    	f1.SetLineColor(6)
	    	f2.SetLineColor(3)
	    	f3.SetLineColor(5)
	    
                legend.SetHeader("Fit range : 0.1 - 1.0","C")
		legend.AddEntry(a,"MC","le")
		legend.AddEntry("f","total func","l")
		#legend.AddEntry("f1","landau","l")
		#legend.AddEntry("f2","gaus","l")
		
                rp = TRatioPlot(hist)
		rp.Draw()
		rp.GetUpperPad().cd()
	    	f1.Draw("same")
	    	f2.Draw("same")
	    	f3.Draw("same")
		legend.Draw()
		rp.GetLowerRefGraph().SetMinimum(-5)
		rp.GetLowerRefGraph().SetMaximum(5)
	    
	    elif SampleEnergy == "15GeV":
		f = TF1("landaugaus","landau(0)+gaus(3)",0,1)
	    	f.SetParName(0,"landau.Constant")
	    	f.SetParName(1,"landau.MPV")
	    	f.SetParName(2,"landau.Sigma")
	    	f.SetParName(3,"gaus.Constant")
	    	f.SetParName(4,"gaus.Mean")
	    	f.SetParName(5,"gaus.Sigma")
	  
		# Initial value and limit
	    	f.SetParameter(0,0.1)
	    	f.SetParLimits(0,0.01,1)
	    	
		f.SetParameter(1,0.1)
	    	f.SetParLimits(1,0.01,1)
	    	
		f.SetParameter(2,0.1)
	    	f.SetParLimits(2,0.01,1)
	    	
	    	f.SetParameter(3,0.1)
	    	f.SetParLimits(3,0.01,1)
	    	
		f.SetParameter(4,0.1)
	    	f.SetParLimits(4,0.01,1)
	    	
		f.SetParameter(5,0.1)
	    	f.SetParLimits(5,0.01,1)
	    	
		hist.Fit(f,"S",'',0,1)
		f1 = TF1("landau","landau",0,1.0)
		f2 = TF1("gaus","gaus",0,1.0)
		
		f1.SetParameter(0,f.GetParameter(0))
	    	f1.SetParameter(1,f.GetParameter(1))
	    	f1.SetParameter(2,f.GetParameter(2))
	    	f2.SetParameter(0,f.GetParameter(3))
	    	f2.SetParameter(1,f.GetParameter(4))
	    	f2.SetParameter(2,f.GetParameter(5))
	    	f1.SetLineColor(6)
	    	f2.SetLineColor(3)
	    
		rp = TRatioPlot(hist)
		rp.Draw()
		rp.GetUpperPad().cd()
	    	f1.Draw("same")
	    	f2.Draw("same")
		legend.Draw()
		rp.GetLowerRefGraph().SetMinimum(-5)
		rp.GetLowerRefGraph().SetMaximum(5)
		
	    elif SampleEnergy == "20GeV":
		f = TF1("doublegaus","gaus(0)+gaus(3)",0,1)
	    	f.SetParName(0,"gaus1.Constant")
	    	f.SetParName(1,"gaus1.Mean")
	    	f.SetParName(2,"gaus1.Sigma")
	    	f.SetParName(3,"gaus2.Constant")
	    	f.SetParName(4,"gaus2.Mean")
	    	f.SetParName(5,"gaus2.Sigma")
		
		# Initial value and limit
	    	f.SetParameter(0,0.1)
	    	f.SetParLimits(0,0.01,1)
	    	
		f.SetParameter(1,0.1)
	    	f.SetParLimits(1,0.01,1)
	    	
		f.SetParameter(2,0.1)
	    	f.SetParLimits(2,0.01,1)
	    	
		f.SetParameter(3,0.1)
	    	f.SetParLimits(3,0.01,1)
	    	
		f.SetParameter(4,0.1)
	    	f.SetParLimits(4,0.01,1)
	    	
		f.SetParameter(5,0.1)
	    	f.SetParLimits(5,0.01,1)
	   
		hist.Fit(f,"S",'',0,1.0)
		f1 = TF1("gaus1","gaus",0,1.0)
	    	f2 = TF1("gaus2","gaus",0,1.0)
		
		f1.SetParameter(0,f.GetParameter(0))
	    	f1.SetParameter(1,f.GetParameter(1))
	    	f1.SetParameter(2,f.GetParameter(2))
	    	f2.SetParameter(0,f.GetParameter(3))
	    	f2.SetParameter(1,f.GetParameter(4))
	    	f2.SetParameter(2,f.GetParameter(5))
	    	f1.SetLineColor(6)
	    	f2.SetLineColor(3)
	    
		rp = TRatioPlot(hist)
		rp.Draw()
		rp.GetUpperPad().cd()
	    	f1.Draw("same")
	    	f2.Draw("same")
		legend.Draw()
		rp.GetLowerRefGraph().SetMinimum(-5)
		rp.GetLowerRefGraph().SetMaximum(5)
		
	    elif SampleEnergy == "30GeV":
		f = TF1("doublegaus","gaus(0)+gaus(3)",0,1)
	    	f.SetParName(0,"gaus1.Constant")
	    	f.SetParName(1,"gaus1.Mean")
	    	f.SetParName(2,"gaus1.Sigma")
	    	f.SetParName(3,"gaus2.Constant")
	    	f.SetParName(4,"gaus2.Mean")
	    	f.SetParName(5,"gaus2.Sigma")
		
		# Initial value and limit
	    	f.SetParameter(0,0.1)
	    	f.SetParLimits(0,0.01,1)
	    	
		f.SetParameter(1,0.1)
	    	f.SetParLimits(1,0.01,1)
	    	
		f.SetParameter(2,0.1)
	    	f.SetParLimits(2,0.01,1)
	    	
		f.SetParameter(3,0.1)
	    	f.SetParLimits(3,0.01,1)
	    	
		f.SetParameter(4,0.1)
	    	f.SetParLimits(4,0.01,1)
	    	
		f.SetParameter(5,0.1)
	    	f.SetParLimits(5,0.01,1)
	   
		hist.Fit(f,"S",'',0,1.0)
		f1 = TF1("gaus1","gaus",0,1.0)
	    	f2 = TF1("gaus2","gaus",0,1.0)
		
		f1.SetParameter(0,f.GetParameter(0))
	    	f1.SetParameter(1,f.GetParameter(1))
	    	f1.SetParameter(2,f.GetParameter(2))
	    	f2.SetParameter(0,f.GetParameter(3))
	    	f2.SetParameter(1,f.GetParameter(4))
	    	f2.SetParameter(2,f.GetParameter(5))
	    	f1.SetLineColor(6)
	    	f2.SetLineColor(3)
	    
		rp = TRatioPlot(hist)
		rp.Draw()
		rp.GetUpperPad().cd()
	    	f1.Draw("same")
	    	f2.Draw("same")
		legend.Draw()
		rp.GetLowerRefGraph().SetMinimum(-5)
		rp.GetLowerRefGraph().SetMaximum(5)
		
	    elif SampleEnergy == "40GeV":
		f = TF1("doublegaus","gaus(0)+gaus(3)",0,1)
	    	f.SetParName(0,"gaus1.Constant")
	    	f.SetParName(1,"gaus1.Mean")
	    	f.SetParName(2,"gaus1.Sigma")
	    	f.SetParName(3,"gaus2.Constant")
	    	f.SetParName(4,"gaus2.Mean")
	    	f.SetParName(5,"gaus2.Sigma")
		
		# Initial value and limit
	    	f.SetParameter(0,0.1)
	    	f.SetParLimits(0,0.01,1)
	    	
		f.SetParameter(1,0.1)
	    	f.SetParLimits(1,0.01,1)
	    	
		f.SetParameter(2,0.1)
	    	f.SetParLimits(2,0.01,1)
	    	
		f.SetParameter(3,0.1)
	    	f.SetParLimits(3,0.01,1)
	    	
		f.SetParameter(4,0.1)
	    	f.SetParLimits(4,0.01,1)
	    	
		f.SetParameter(5,0.1)
	    	f.SetParLimits(5,0.01,1)
	   
		hist.Fit(f,"S",'',0,1.0)
		f1 = TF1("gaus1","gaus",0,1.0)
	    	f2 = TF1("gaus2","gaus",0,1.0)
		
		f1.SetParameter(0,f.GetParameter(0))
	    	f1.SetParameter(1,f.GetParameter(1))
	    	f1.SetParameter(2,f.GetParameter(2))
	    	f2.SetParameter(0,f.GetParameter(3))
	    	f2.SetParameter(1,f.GetParameter(4))
	    	f2.SetParameter(2,f.GetParameter(5))
	    	f1.SetLineColor(6)
	    	f2.SetLineColor(3)
	    
		rp = TRatioPlot(hist)
		rp.Draw()
		rp.GetUpperPad().cd()
	    	f1.Draw("same")
	    	f2.Draw("same")
		legend.Draw()
		rp.GetLowerRefGraph().SetMinimum(-5)
		rp.GetLowerRefGraph().SetMaximum(5)
		
	    elif SampleEnergy == "50GeV":
		f = TF1("doublegaus","gaus(0)+gaus(3)",0,1)
	    	f.SetParName(0,"gaus1.Constant")
	    	f.SetParName(1,"gaus1.Mean")
	    	f.SetParName(2,"gaus1.Sigma")
	    	f.SetParName(3,"gaus2.Constant")
	    	f.SetParName(4,"gaus2.Mean")
	    	f.SetParName(5,"gaus2.Sigma")
		
		# Initial value and limit
	    	f.SetParameter(0,0.1)
	    	f.SetParLimits(0,0.01,1)
	    	
		f.SetParameter(1,0.1)
	    	f.SetParLimits(1,0.01,1)
	    	
		f.SetParameter(2,0.1)
	    	f.SetParLimits(2,0.01,1)
	    	
		f.SetParameter(3,0.1)
	    	f.SetParLimits(3,0.01,1)
	    	
		f.SetParameter(4,0.1)
	    	f.SetParLimits(4,0.01,1)
	    	
		f.SetParameter(5,0.1)
	    	f.SetParLimits(5,0.01,1)
	   
		hist.Fit(f,"S",'',0,1.0)
		f1 = TF1("gaus1","gaus",0,1.0)
	    	f2 = TF1("gaus2","gaus",0,1.0)
		
		f1.SetParameter(0,f.GetParameter(0))
	    	f1.SetParameter(1,f.GetParameter(1))
	    	f1.SetParameter(2,f.GetParameter(2))
	    	f2.SetParameter(0,f.GetParameter(3))
	    	f2.SetParameter(1,f.GetParameter(4))
	    	f2.SetParameter(2,f.GetParameter(5))
	    	f1.SetLineColor(6)
	    	f2.SetLineColor(3)
		
		rp = TRatioPlot(hist)
		rp.Draw()
		rp.GetUpperPad().cd()
	    	f1.Draw("same")
	    	f2.Draw("same")
		legend.Draw()
		rp.GetLowerRefGraph().SetMinimum(-5)
		rp.GetLowerRefGraph().SetMaximum(5)

	    elif SampleEnergy == "70GeV":
		f = TF1("doublegaus","gaus(0)+gaus(3)",0,1)
	    	f.SetParName(0,"gaus1.Constant")
	    	f.SetParName(1,"gaus1.Mean")
	    	f.SetParName(2,"gaus1.Sigma")
	    	f.SetParName(3,"gaus2.Constant")
	    	f.SetParName(4,"gaus2.Mean")
	    	f.SetParName(5,"gaus2.Sigma")
		
		# Initial value and limit
	    	f.SetParameter(0,0.1)
	    	f.SetParLimits(0,0.01,1)
	    	
		f.SetParameter(1,0.1)
	    	f.SetParLimits(1,0.01,1)
	    	
		f.SetParameter(2,0.1)
	    	f.SetParLimits(2,0.01,1)
	    	
		f.SetParameter(3,0.1)
	    	f.SetParLimits(3,0.01,1)
	    	
		f.SetParameter(4,0.1)
	    	f.SetParLimits(4,0.01,1)
	    	
		f.SetParameter(5,0.1)
	    	f.SetParLimits(5,0.01,1)
	   
		hist.Fit(f,"S",'',0,1.0)
		f1 = TF1("gaus1","gaus",0,1.0)
	    	f2 = TF1("gaus2","gaus",0,1.0)
		
		f1.SetParameter(0,f.GetParameter(0))
	    	f1.SetParameter(1,f.GetParameter(1))
	    	f1.SetParameter(2,f.GetParameter(2))
	    	f2.SetParameter(0,f.GetParameter(3))
	    	f2.SetParameter(1,f.GetParameter(4))
	    	f2.SetParameter(2,f.GetParameter(5))
	    	f1.SetLineColor(6)
	    	f2.SetLineColor(3)
		
		rp = TRatioPlot(hist)
		rp.Draw()
		rp.GetUpperPad().cd()
	    	f1.Draw("same")
	    	f2.Draw("same")
		legend.Draw()
		rp.GetLowerRefGraph().SetMinimum(-5)
		rp.GetLowerRefGraph().SetMaximum(5)

	    elif SampleEnergy == "100GeV":
		f = TF1("doublegaus","gaus(0)+gaus(3)",0,1)
	    	f.SetParName(0,"gaus1.Constant")
	    	f.SetParName(1,"gaus1.Mean")
	    	f.SetParName(2,"gaus1.Sigma")
	    	f.SetParName(3,"gaus2.Constant")
	    	f.SetParName(4,"gaus2.Mean")
	    	f.SetParName(5,"gaus2.Sigma")
		
		# Initial value and limit
	    	f.SetParameter(0,0.1)
	    	f.SetParLimits(0,0.01,1)
	    	
		f.SetParameter(1,0.1)
	    	f.SetParLimits(1,0.01,1)
	    	
		f.SetParameter(2,0.1)
	    	f.SetParLimits(2,0.01,1)
	    	
		f.SetParameter(3,0.1)
	    	f.SetParLimits(3,0.01,1)
	    	
		f.SetParameter(4,0.1)
	    	f.SetParLimits(4,0.01,1)
	    	
		f.SetParameter(5,0.1)
	    	f.SetParLimits(5,0.01,1)
		
                hist.Fit(f,"S",'',0,1.0)
		f1 = TF1("gaus1","gaus",0,1.0)
	    	f2 = TF1("gaus2","gaus",0,1.0)
		
		f1.SetParameter(0,f.GetParameter(0))
	    	f1.SetParameter(1,f.GetParameter(1))
	    	f1.SetParameter(2,f.GetParameter(2))
	    	f2.SetParameter(0,f.GetParameter(3))
	    	f2.SetParameter(1,f.GetParameter(4))
	    	f2.SetParameter(2,f.GetParameter(5))
	    	f1.SetLineColor(6)
	    	f2.SetLineColor(3)

		rp = TRatioPlot(hist)
		rp.Draw()
		rp.GetUpperPad().cd()
	    	f1.Draw("same")
	    	f2.Draw("same")
		legend.Draw()
		rp.GetLowerRefGraph().SetMinimum(-5)
		rp.GetLowerRefGraph().SetMaximum(5)


	    elif SampleEnergy == "150GeV":
		f = TF1("doublegaus","gaus(0)+gaus(3)",0,1)
	    	f.SetParName(0,"gaus1.Constant")
	    	f.SetParName(1,"gaus1.Mean")
	    	f.SetParName(2,"gaus1.Sigma")
	    	f.SetParName(3,"gaus2.Constant")
	    	f.SetParName(4,"gaus2.Mean")
	    	f.SetParName(5,"gaus2.Sigma")
		
		# Initial value and limit
	    	f.SetParameter(0,0.1)
	    	f.SetParLimits(0,0.01,1)
	    	
		f.SetParameter(1,0.1)
	    	f.SetParLimits(1,0.01,1)
	    	
		f.SetParameter(2,0.1)
	    	f.SetParLimits(2,0.01,1)
	    	
		f.SetParameter(3,0.1)
	    	f.SetParLimits(3,0.01,1)
	    	
		f.SetParameter(4,0.1)
	    	f.SetParLimits(4,0.01,1)
	    	
		f.SetParameter(5,0.1)
	    	f.SetParLimits(5,0.01,1)
		
		hist.Fit(f,"S",'',0,1.0)
		f1 = TF1("gaus1","gaus",0,1.0)
	    	f2 = TF1("gaus2","gaus",0,1.0)
		
		f1.SetParameter(0,f.GetParameter(0))
	    	f1.SetParameter(1,f.GetParameter(1))
	    	f1.SetParameter(2,f.GetParameter(2))
	    	f2.SetParameter(0,f.GetParameter(3))
	    	f2.SetParameter(1,f.GetParameter(4))
	    	f2.SetParameter(2,f.GetParameter(5))
	    	f1.SetLineColor(6)
	    	f2.SetLineColor(3)

		rp = TRatioPlot(hist)
		rp.Draw()
		rp.GetUpperPad().cd()
	    	f1.Draw("same")
	    	f2.Draw("same")
		legend.Draw()
		rp.GetLowerRefGraph().SetMinimum(-5)
		rp.GetLowerRefGraph().SetMaximum(5)
	    
            elif SampleEnergy == "200GeV" :
		f = TF1("doublegaus","gaus(0)+gaus(3)",0,1)
	    	f.SetParName(0,"gaus1.Constant")
	    	f.SetParName(1,"gaus1.Mean")
	    	f.SetParName(2,"gaus1.Sigma")
	    	f.SetParName(3,"gaus2.Constant")
	    	f.SetParName(4,"gaus2.Mean")
	    	f.SetParName(5,"gaus2.Sigma")
		
		# Initial value and limit
	    	f.SetParameter(0,0.1)
	    	f.SetParLimits(0,0.01,1)
	    	
		f.SetParameter(1,0.1)
	    	f.SetParLimits(1,0.01,1)
	    	
		f.SetParameter(2,0.1)
	    	f.SetParLimits(2,0.01,1)
	    	
		f.SetParameter(3,0.1)
	    	f.SetParLimits(3,0.01,1)
	    	
		f.SetParameter(4,0.1)
	    	f.SetParLimits(4,0.01,1)
	    	
		f.SetParameter(5,0.1)
	    	f.SetParLimits(5,0.01,1)
		
		hist.Fit(f,"S",'',0,1.0)
		f1 = TF1("gaus1","gaus",0,1.0)
	    	f2 = TF1("gaus2","gaus",0,1.0)
		
		f1.SetParameter(0,f.GetParameter(0))
	    	f1.SetParameter(1,f.GetParameter(1))
	    	f1.SetParameter(2,f.GetParameter(2))
	    	f2.SetParameter(0,f.GetParameter(3))
	    	f2.SetParameter(1,f.GetParameter(4))
	    	f2.SetParameter(2,f.GetParameter(5))
	    	f1.SetLineColor(6)
	    	f2.SetLineColor(3)

		rp = TRatioPlot(hist)
		rp.Draw()
		rp.GetUpperPad().cd()
	    	f1.Draw("same")
	    	f2.Draw("same")
		legend.Draw()
		rp.GetLowerRefGraph().SetMinimum(-5)
		rp.GetLowerRefGraph().SetMaximum(5)

            elif SampleEnergy == "300GeV" :
		f = TF1("doublegaus","gaus(0)+gaus(3)",0,1)
	    	f.SetParName(0,"gaus1.Constant")
	    	f.SetParName(1,"gaus1.Mean")
	    	f.SetParName(2,"gaus1.Sigma")
	    	f.SetParName(3,"gaus2.Constant")
	    	f.SetParName(4,"gaus2.Mean")
	    	f.SetParName(5,"gaus2.Sigma")
		
		# Initial value and limit
	    	f.SetParameter(0,0.1)
	    	f.SetParLimits(0,0.01,1)
	    	
		f.SetParameter(1,0.1)
	    	f.SetParLimits(1,0.01,1)
	    	
		f.SetParameter(2,0.1)
	    	f.SetParLimits(2,0.01,1)
	    	
		f.SetParameter(3,0.1)
	    	f.SetParLimits(3,0.01,1)
	    	
		f.SetParameter(4,0.1)
	    	f.SetParLimits(4,0.01,1)
	    	
		f.SetParameter(5,0.1)
	    	f.SetParLimits(5,0.01,1)
		
		hist.Fit(f,"S",'',0,1.0)
		f1 = TF1("gaus1","gaus",0,1.0)
	    	f2 = TF1("gaus2","gaus",0,1.0)
		
		f1.SetParameter(0,f.GetParameter(0))
	    	f1.SetParameter(1,f.GetParameter(1))
	    	f1.SetParameter(2,f.GetParameter(2))
	    	f2.SetParameter(0,f.GetParameter(3))
	    	f2.SetParameter(1,f.GetParameter(4))
	    	f2.SetParameter(2,f.GetParameter(5))
	    	f1.SetLineColor(6)
	    	f2.SetLineColor(3)

		rp = TRatioPlot(hist)
		rp.Draw()
		rp.GetUpperPad().cd()
	    	f1.Draw("same")
	    	f2.Draw("same")
		legend.Draw()
		rp.GetLowerRefGraph().SetMinimum(-5)
		rp.GetLowerRefGraph().SetMaximum(5)

            elif SampleEnergy == "400GeV" :
		f = TF1("doublegaus","gaus(0)+gaus(3)",0,1)
	    	f.SetParName(0,"gaus1.Constant")
	    	f.SetParName(1,"gaus1.Mean")
	    	f.SetParName(2,"gaus1.Sigma")
	    	f.SetParName(3,"gaus2.Constant")
	    	f.SetParName(4,"gaus2.Mean")
	    	f.SetParName(5,"gaus2.Sigma")
		
		# Initial value and limit
	    	f.SetParameter(0,0.1)
	    	f.SetParLimits(0,0.01,1)
	    	
		f.SetParameter(1,0.1)
	    	f.SetParLimits(1,0.01,1)
	    	
		f.SetParameter(2,0.1)
	    	f.SetParLimits(2,0.01,1)
	    	
		f.SetParameter(3,0.1)
	    	f.SetParLimits(3,0.01,1)
	    	
		f.SetParameter(4,0.1)
	    	f.SetParLimits(4,0.01,1)
	    	
		f.SetParameter(5,0.1)
	    	f.SetParLimits(5,0.01,1)
		
		hist.Fit(f,"S",'',0,1.0)
		f1 = TF1("gaus1","gaus",0,1.0)
	    	f2 = TF1("gaus2","gaus",0,1.0)
		
		f1.SetParameter(0,f.GetParameter(0))
	    	f1.SetParameter(1,f.GetParameter(1))
	    	f1.SetParameter(2,f.GetParameter(2))
	    	f2.SetParameter(0,f.GetParameter(3))
	    	f2.SetParameter(1,f.GetParameter(4))
	    	f2.SetParameter(2,f.GetParameter(5))
	    	f1.SetLineColor(6)
	    	f2.SetLineColor(3)

		rp = TRatioPlot(hist)
		rp.Draw()
		rp.GetUpperPad().cd()
	    	f1.Draw("same")
	    	f2.Draw("same")
		legend.Draw()
		rp.GetLowerRefGraph().SetMinimum(-5)
		rp.GetLowerRefGraph().SetMaximum(5)

            elif SampleEnergy == "500GeV" :
		f = TF1("doublegaus","gaus(0)+gaus(3)",0,1)
	    	f.SetParName(0,"gaus1.Constant")
	    	f.SetParName(1,"gaus1.Mean")
	    	f.SetParName(2,"gaus1.Sigma")
	    	f.SetParName(3,"gaus2.Constant")
	    	f.SetParName(4,"gaus2.Mean")
	    	f.SetParName(5,"gaus2.Sigma")
		
		# Initial value and limit
	    	f.SetParameter(0,0.1)
	    	f.SetParLimits(0,0.01,1)
	    	
		f.SetParameter(1,0.1)
	    	f.SetParLimits(1,0.01,1)
	    	
		f.SetParameter(2,0.1)
	    	f.SetParLimits(2,0.01,1)
	    	
		f.SetParameter(3,0.1)
	    	f.SetParLimits(3,0.01,1)
	    	
		f.SetParameter(4,0.1)
	    	f.SetParLimits(4,0.01,1)
	    	
		f.SetParameter(5,0.1)
	    	f.SetParLimits(5,0.01,1)
		
		hist.Fit(f,"S",'',0,1.0)
		f1 = TF1("gaus1","gaus",0,1.0)
	    	f2 = TF1("gaus2","gaus",0,1.0)
		
		f1.SetParameter(0,f.GetParameter(0))
	    	f1.SetParameter(1,f.GetParameter(1))
	    	f1.SetParameter(2,f.GetParameter(2))
	    	f2.SetParameter(0,f.GetParameter(3))
	    	f2.SetParameter(1,f.GetParameter(4))
	    	f2.SetParameter(2,f.GetParameter(5))
	    	f1.SetLineColor(6)
	    	f2.SetLineColor(3)

		rp = TRatioPlot(hist)
		rp.Draw()
		rp.GetUpperPad().cd()
	    	f1.Draw("same")
	    	f2.Draw("same")
		legend.Draw()
		rp.GetLowerRefGraph().SetMinimum(-5)
		rp.GetLowerRefGraph().SetMaximum(5)

	    else : 
		print 'Dont have this energy'
		quit()
	
	elif variable == "fPi0L" :
	    ROOT.gStyle.SetStatY(0.9);                
    	    ROOT.gStyle.SetStatX(0.4);                
    	    ROOT.gStyle.SetStatW(0.15);                
    	    ROOT.gStyle.SetStatH(0.15);                
    	    #ROOT.gStyle.SetOptStat(0)
	    if SampleEnergy == "1GeV":
		f = TF1("doublegaus","gaus(0)+gaus(3)",0,1)
	    	f.SetParName(0,"gaus1.Constant")
	    	f.SetParName(1,"gaus1.Mean")
	    	f.SetParName(2,"gaus1.Sigma")
	    	f.SetParName(3,"gaus2.Constant")
	    	f.SetParName(4,"gaus2.Mean")
	    	f.SetParName(5,"gaus2.Sigma")
		
		# Initial value and limit
	    	f.SetParameter(0,0.1)
	    	f.SetParLimits(0,0.01,1)
	    	
		f.SetParameter(1,0.4)
	    	f.SetParLimits(1,0.01,1)
	    	
		f.SetParameter(2,0.1)
	    	f.SetParLimits(2,0.01,1)
	    	
		f.SetParameter(3,0.1)
	    	f.SetParLimits(3,0.01,1)
	    	
		f.SetParameter(4,0.5)
	    	f.SetParLimits(4,0.01,1)
	    	
		f.SetParameter(5,0.1)
	    	f.SetParLimits(5,0.01,1)
		
		hist.Fit(f,"S",'',0,1.0)
		f1 = TF1("gaus1","gaus",0,1.0)
	    	f2 = TF1("gaus2","gaus",0,1.0)
		
		f1.SetParameter(0,f.GetParameter(0))
	    	f1.SetParameter(1,f.GetParameter(1))
	    	f1.SetParameter(2,f.GetParameter(2))
	    	f2.SetParameter(0,f.GetParameter(3))
	    	f2.SetParameter(1,f.GetParameter(4))
	    	f2.SetParameter(2,f.GetParameter(5))
	    	f1.SetLineColor(6)
	    	f2.SetLineColor(3)
		
                legend.SetHeader("Fit range : 0.1 - 1.0","C")
		legend.AddEntry(a,"MC","le")
		legend.AddEntry("f","total func","l")
		legend.AddEntry("f1","gaus1","l")
		legend.AddEntry("f2","gaus2","l")

		rp = TRatioPlot(hist)
		rp.Draw()
		rp.GetUpperPad().cd()
	    	f1.Draw("same")
	    	f2.Draw("same")
		legend.Draw()
		rp.GetLowerRefGraph().SetMinimum(-5)
		rp.GetLowerRefGraph().SetMaximum(5)

	    elif SampleEnergy == "2GeV":
	        ROOT.gStyle.SetStatY(0.9);                
    	        ROOT.gStyle.SetStatX(0.3);                
    	        ROOT.gStyle.SetStatW(0.10);                
    	        ROOT.gStyle.SetStatH(0.10);                
    	        #ROOT.gStyle.SetOptStat(0)
		f = TF1("doublegaus","gaus(0)+gaus(3)",0,1)
	    	f.SetParName(0,"gaus1.Constant")
	    	f.SetParName(1,"gaus1.Mean")
	    	f.SetParName(2,"gaus1.Sigma")
	    	f.SetParName(3,"gaus2.Constant")
	    	f.SetParName(4,"gaus2.Mean")
	    	f.SetParName(5,"gaus2.Sigma")
		
		# Initial value and limit
	    	f.SetParameter(0,0.1)
	    	f.SetParLimits(0,0.01,1)
	    	
		f.SetParameter(1,0.4)
	    	f.SetParLimits(1,0.01,1)
	    	
		f.SetParameter(2,0.1)
	    	f.SetParLimits(2,0.01,1)
	    	
		f.SetParameter(3,0.1)
	    	f.SetParLimits(3,0.01,1)
	    	
		f.SetParameter(4,0.5)
	    	f.SetParLimits(4,0.01,1)
	    	
		f.SetParameter(5,0.1)
	    	f.SetParLimits(5,0.01,1)
		
		hist.Fit(f,"S",'',0,1)
		f1 = TF1("gaus1","gaus",0,1)
	    	f2 = TF1("gaus2","gaus",0,1)
		
		f1.SetParameter(0,f.GetParameter(0))
	    	f1.SetParameter(1,f.GetParameter(1))
	    	f1.SetParameter(2,f.GetParameter(2))
	    	f2.SetParameter(0,f.GetParameter(3))
	    	f2.SetParameter(1,f.GetParameter(4))
	    	f2.SetParameter(2,f.GetParameter(5))
	    	f1.SetLineColor(6)
	    	f2.SetLineColor(3)
                
                legend.SetHeader("Fit range : 0.1 - 1.0","C")
		legend.AddEntry(a,"MC","le")
		legend.AddEntry("f","total func","l")
		legend.AddEntry("f1","gaus1","l")
		legend.AddEntry("f2","gaus2","l")

		rp = TRatioPlot(hist)
		rp.Draw()
		rp.GetUpperPad().cd()
	    	f1.Draw("same")
	    	f2.Draw("same")
		legend.Draw()
		rp.GetLowerRefGraph().SetMinimum(-5)
		rp.GetLowerRefGraph().SetMaximum(5)
	    
	    elif SampleEnergy == "5GeV":
	        ROOT.gStyle.SetStatY(0.9);                
    	        ROOT.gStyle.SetStatX(0.9);                
    	        ROOT.gStyle.SetStatW(0.15);                
    	        ROOT.gStyle.SetStatH(0.15);                
    	        #ROOT.gStyle.SetOptStat(0)
		f = TF1("landaugaus","landau(0)+gaus(3)",0,1)
	    	f.SetParName(0,"landau.Constant")
	    	f.SetParName(1,"landau.MPV")
	    	f.SetParName(2,"landau.Sigma")
	    	f.SetParName(3,"gaus.Constant")
	    	f.SetParName(4,"gaus.Mean")
	    	f.SetParName(5,"gaus.Sigma")
	  
		# Initial value and limit
	    	f.SetParameter(0,0.1)
	    	f.SetParLimits(0,0.01,1)
	    	
		f.SetParameter(1,0.3)
	    	f.SetParLimits(1,0.01,1)
	    	
		f.SetParameter(2,0.1)
	    	f.SetParLimits(2,0.01,1)
	    	
		f.SetParameter(3,0.1)
	    	f.SetParLimits(3,0.01,1)
	    	
		f.SetParameter(4,0.5)
	    	f.SetParLimits(4,0.01,1)
	    	
		f.SetParameter(5,0.1)
	    	f.SetParLimits(5,0.01,1)
	    	
		hist.Fit(f,"S",'',0,1)
		f1 = TF1("landau","landau",0,1.0)
		f2 = TF1("gaus","gaus",0,1.0)
		
		f1.SetParameter(0,f.GetParameter(0))
	    	f1.SetParameter(1,f.GetParameter(1))
	    	f1.SetParameter(2,f.GetParameter(2))
	    	f2.SetParameter(0,f.GetParameter(3))
	    	f2.SetParameter(1,f.GetParameter(4))
	    	f2.SetParameter(2,f.GetParameter(5))
	    	f1.SetLineColor(6)
	    	f2.SetLineColor(3)
                
                legend = TLegend(0.4,0.7,0.6,0.9)
                legend.SetHeader("Fit range : 0.1 - 1.0","C")
		legend.AddEntry(a,"MC","le")
		legend.AddEntry("f","total func","l")
		#legend.AddEntry("f1","gaus1","l")
		#legend.AddEntry("f2","gaus2","l")

		rp = TRatioPlot(hist)
		rp.Draw()
		rp.GetUpperPad().cd()
	    	f1.Draw("same")
	    	f2.Draw("same")
		legend.Draw()
		rp.GetLowerRefGraph().SetMinimum(-5)
		rp.GetLowerRefGraph().SetMaximum(5)
	    
	    elif SampleEnergy == "7GeV":
	        ROOT.gStyle.SetStatY(0.9);                
    	        ROOT.gStyle.SetStatX(0.9);                
    	        ROOT.gStyle.SetStatW(0.15);                
    	        ROOT.gStyle.SetStatH(0.15);                
    	        #ROOT.gStyle.SetOptStat(0)
		f = TF1("landaugaus","landau(0)+gaus(3)",0,1)
	    	f.SetParName(0,"landau.Constant")
	    	f.SetParName(1,"landau.MPV")
	    	f.SetParName(2,"landau.Sigma")
	    	f.SetParName(3,"gaus.Constant")
	    	f.SetParName(4,"gaus.Mean")
	    	f.SetParName(5,"gaus.Sigma")
	  
		# Initial value and limit
	    	f.SetParameter(0,0.1)
	    	f.SetParLimits(0,0.01,1)
	    	
		f.SetParameter(1,0.3)
	    	f.SetParLimits(1,0.01,1)
	    	
		f.SetParameter(2,0.1)
	    	f.SetParLimits(2,0.01,1)
	    	
		f.SetParameter(3,0.1)
	    	f.SetParLimits(3,0.01,1)
	    	
		f.SetParameter(4,0.5)
	    	f.SetParLimits(4,0.01,1)
	    	
		f.SetParameter(5,0.1)
	    	f.SetParLimits(5,0.01,1)
	    	
		hist.Fit(f,"S",'',0,1)
		f1 = TF1("landau","landau",0,1.0)
		f2 = TF1("gaus","gaus",0,1.0)
		
		f1.SetParameter(0,f.GetParameter(0))
	    	f1.SetParameter(1,f.GetParameter(1))
	    	f1.SetParameter(2,f.GetParameter(2))
	    	f2.SetParameter(0,f.GetParameter(3))
	    	f2.SetParameter(1,f.GetParameter(4))
	    	f2.SetParameter(2,f.GetParameter(5))
	    	f1.SetLineColor(6)
	    	f2.SetLineColor(3)
                
                legend = TLegend(0.4,0.7,0.6,0.9)
                legend.SetHeader("Fit range : 0.1 - 1.0","C")
		legend.AddEntry(a,"MC","le")
		legend.AddEntry("f","total func","l")
		#legend.AddEntry("f1","gaus1","l")
		#legend.AddEntry("f2","gaus2","l")

		rp = TRatioPlot(hist)
		rp.Draw()
		rp.GetUpperPad().cd()
	    	f1.Draw("same")
	    	f2.Draw("same")
		legend.Draw()
		rp.GetLowerRefGraph().SetMinimum(-5)
		rp.GetLowerRefGraph().SetMaximum(5)
	    
	    elif SampleEnergy == "10GeV":
		f = TF1("gauspolgaus","gaus(0)+pol1(3)+gaus(5)",0,1)
	    	f.SetParName(0,"gaus1.Constant")
	    	f.SetParName(1,"gaus1.Mean")
	    	f.SetParName(2,"gaus1.Sigma")
	    	f.SetParName(3,"pol1.a")
	    	f.SetParName(4,"pol1.b")
	    	f.SetParName(5,"gaus.Constant")
	    	f.SetParName(6,"gaus.Mean")
	    	f.SetParName(7,"gaus.Sigma")
		
		# Initial value and limit
	    	f.SetParameter(0,1000)
	    	f.SetParLimits(0,0,2000)
	    	
		f.SetParameter(1,0.01)
	    	f.SetParLimits(1,0,0.1)
	    	
		f.SetParameter(2,0.1)
	    	f.SetParLimits(2,0,1)
	    	
	    	f.SetParameter(3,700)
	    	f.SetParLimits(3,0,2000)
	    	
		f.SetParameter(4,0)
	    	f.SetParLimits(4,-1000,1000)
	    	
	    	f.SetParameter(5,1000)
	    	f.SetParLimits(5,0,2000)
	    	
		f.SetParameter(6,0.7)
	    	f.SetParLimits(6,0.5,1)
		
		f.SetParameter(7,0.1)
	    	f.SetParLimits(7,0,1)
	    	
		hist.Fit(f,"S",'',0,1)
		f1 = TF1("gaus","gaus",0,1.0)
		f2 = TF1("pol1","pol1",0,1.0)
		f3 = TF1("gaus","gaus",0,1.0)
		
		f1.SetParameter(0,f.GetParameter(0))
	    	f1.SetParameter(1,f.GetParameter(1))
	    	f1.SetParameter(2,f.GetParameter(2))
	    	f2.SetParameter(0,f.GetParameter(3))
	    	f2.SetParameter(1,f.GetParameter(4))
		f3.SetParameter(0,f.GetParameter(5))
	    	f3.SetParameter(1,f.GetParameter(6))
	    	f3.SetParameter(2,f.GetParameter(7))
	    	f1.SetLineColor(6)
	    	f2.SetLineColor(3)
	    	f3.SetLineColor(5)
	    	f1.Draw("same")
	    	f2.Draw("same")
	    	f3.Draw("same")
	    
	    #elif b == "20GeV":
	    #elif b == "50GeV":
	    #elif b == "100GeV":
	    #elif b == "200GeV" :
	    else : 
		print 'Dont have this energy'
		quit()
    else : 
        hist.Draw("E")
	
    canvas.Print("./plots/"+variable+"/"+ SampleEnergy +"_"+ variable + ".png")
    del canvas
    gc.collect()

def drawCombine(H = [], HN=[]):
    ROOT.gStyle.SetOptStat(0)
    canvas = ROOT.TCanvas("can_name","can_name",10,10,1100,628)
    canvas.cd()
    pad_name = "pad"
    pad1=ROOT.TPad(pad_name, pad_name, 0.05, 0.05, 1, 0.99 , 0)
    pad1.Draw()
    legend = ROOT.TLegend(0.3,0.6,0.4,0.87)
    legend.SetBorderSize(0)
    legend.SetTextFont(42)
    legend.SetTextSize(0.03)
    for i in range(len(H)):
        a,b,c =HN[i].split("_")
        H[i].SetLineColor( i+1 )
        if i==0:
            H[i].SetTitle('')
            H[i].GetXaxis().SetTitle(c)
            H[i].GetYaxis().SetTitle('Fraction')
            H[i].GetXaxis().SetTitleSize(0.05)
            H[i].GetYaxis().SetTitleSize(0.05)
            H[i].SetMaximum(1.5*H[i].GetMaximum())
            H[i].SetMinimum(0);
            H[i].GetYaxis().SetTitleOffset(0.7)
            H[i].Draw()   
        H[i].Draw("Same")
        legend.AddEntry(H[i] ,b,'l')
    legend.Draw("same")
    canvas.Print("./plots/ND_" + c + ".png")
    del canvas
    gc.collect()

def drawLinearityCheck():
    ROOT.gStyle.SetOptStat(0)
    canvas = ROOT.TCanvas("can_name","can_name",10,10,800,600)
    canvas.cd()
    
    frame = canvas.DrawFrame(0,0.5,250,1)
    frame.SetTitle("fDp")
    frame.GetXaxis().SetTitle("GeV")
    frame.GetYaxis().SetTitle("fDp_mean")
    
    tg_mean = TGraph()
    
    for key, value in mean_dict.items():
	tg_mean.SetPoint(tg_mean.GetN(),    1,	    mean_dict["1GeV_fDp"])
	tg_mean.SetPoint(tg_mean.GetN(),    2,	    mean_dict["2GeV_fDp"])
	tg_mean.SetPoint(tg_mean.GetN(),    5,	    mean_dict["5GeV_fDp"])
	tg_mean.SetPoint(tg_mean.GetN(),    10,    mean_dict["10GeV_fDp"])
	tg_mean.SetPoint(tg_mean.GetN(),    20,    mean_dict["20GeV_fDp"])
	tg_mean.SetPoint(tg_mean.GetN(),    50,    mean_dict["50GeV_fDp"])
	tg_mean.SetPoint(tg_mean.GetN(),    100,   mean_dict["100GeV_fDp"])
	tg_mean.SetPoint(tg_mean.GetN(),    200,   mean_dict["200GeV_fDp"])
	print key, value

    tg_mean.SetMarkerSize(1)
    tg_mean.SetMarkerStyle(8)
    tg_mean.Draw("P")
    
    canvas.Print("hmean.png")
    canvas.SetLogx()
    canvas.Update()
    canvas.Print("hmean_log.png")

    del canvas
    gc.collect()

samples = [
#'histos/HistRezaAnalysis_500GeV.root',
#'histos/HistRezaAnalysis_400GeV.root',
#'histos/HistRezaAnalysis_300GeV.root',
#'histos/HistRezaAnalysis_200GeV.root',
#'histos/HistRezaAnalysis_150GeV.root',
#'histos/HistRezaAnalysis_100GeV.root',
#'histos/HistRezaAnalysis_70GeV.root',
#'histos/HistRezaAnalysis_50GeV.root',
#'histos/HistRezaAnalysis_40GeV.root',
#'histos/HistRezaAnalysis_30GeV.root',
#'histos/HistRezaAnalysis_20GeV.root',
#'histos/HistRezaAnalysis_15GeV.root',
#'histos/HistRezaAnalysis_10GeV.root',
'histos/HistRezaAnalysis_7GeV.root',
'histos/HistRezaAnalysis_5GeV.root',
'histos/HistRezaAnalysis_2GeV.root',
'histos/HistRezaAnalysis_1GeV.root',
]

#variables = ['fDp','fPi0','fPi0L', 'Class']
#variables = ['fDp','fPi0']
#variables = ['fDp']
#variables = ['fPi0']
variables = ['fPi0L']

for num, sample in enumerate(samples):
    for variable in variables:
        if not os.path.exists('./plots/'+variable):os.system('mkdir -p plots/'+variable)
        file1 = ROOT.TFile.Open(sample)
        if variable not in  [file1.GetListOfKeys()[ih].GetName() for ih in range(file1.GetListOfKeys().GetSize())]:
            print('do not find the hist')
            continue
        histA = file1.Get(variable)
	print 'sample:{}, variable:{}'.format(sample, variable)
        draw1dHist(histA, variable, sample, doFit=True)
        #draw1dHist(histA, variable, sample, doFit=False)
        del histA


Hist=[]
HistName=[]

#for v in variable:
#    for num, sample in enumerate(samples):
#        file1 = ROOT.TFile.Open('Hist'+sample+'.root')
#        if v not in  [file1.GetListOfKeys()[ih].GetName() for ih in range(file1.GetListOfKeys().GetSize())]:
#            print('do not find the hist')
#            continue     
#        Hist.append(file1.Get(v))
#        HistName.append(sample+'_'+v)
#    drawCombine(Hist,HistName)
#    del Hist[:] 
#    del HistName[:]
#
#drawLinearityCheck()
