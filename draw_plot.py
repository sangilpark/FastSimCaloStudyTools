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
################################## MY SIGNAL AND SM BG ################################

mean_dict = collections.OrderedDict()

#def draw1dHist(A,textA="A", label_name="sample", can_name="can"):
def draw1dHist(A,textA="A", label_name="sample", can_name="can", doFit=True):
    ROOT.gStyle.SetOptStat(1111);
    #ROOT.gStyle.SetOptStat(0);
    if doFit : 
    	ROOT.gStyle.SetOptFit(1)

    a,b = label_name.split("_")
    canvas = ROOT.TCanvas(can_name,can_name,1100,600)
    canvas.cd()

    pad_name = "pad"
    pad1=ROOT.TPad(pad_name, pad_name, 0.05, 0.05, 1, 0.99 , 0)
    pad1.Draw()

    legend = TLegend(0.7,0.7,0.9,0.9)
    
    
    A.Scale(1/A.Integral())
    A.SetLineColor( 4 )
    A.SetLineWidth( 2 )
    A.SetTitle('(E(#pi^{+}) =' + b +')')
    A.GetXaxis().SetTitle(textA)
    A.GetYaxis().SetTitle('Normalized')
    A.GetXaxis().SetTitleSize(0.05)
    A.GetYaxis().SetTitleSize(0.05)
    A.SetMaximum(1.5*A.GetMaximum())
    A.SetMinimum(0);
    A.GetYaxis().SetTitleOffset(0.7)
    A.Draw("E")
    if doFit :
	if textA == "fDp" :
	    ROOT.gStyle.SetStatY(0.9);                
    	    ROOT.gStyle.SetStatX(0.4);                
    	    ROOT.gStyle.SetStatW(0.15);                
    	    ROOT.gStyle.SetStatH(0.15);                
    	    #ROOT.gStyle.SetOptStat(0)
	    if b == "1GeV":
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
	   
		A.Fit(f,"S",'',0,1.0)
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
	    	f1.Draw("same")
	    	f2.Draw("same")
	    	f3.Draw("same")
		legend.SetHeader("Fit range : 0.1 - 1.0","C")
		legend.AddEntry(a,"MC","le")
		legend.AddEntry("f","total func","l")
		legend.AddEntry("f1","gaus1","l")
		legend.AddEntry("f2","gaus2","l")
		legend.AddEntry("f3","gaus3","l")
		legend.Draw()

		mean_dict[str(b)+"_"+textA] = A.GetMean()
	    
	    elif b == "2GeV":
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
	   
		A.Fit(f,"S",'',0,1.0)
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
	    	f1.Draw("same")
	    	f2.Draw("same")
	    	f3.Draw("same")
		legend.SetHeader("Fit range : 0.3 - 1.0","C")
		legend.AddEntry(a,"MC","le")
		legend.AddEntry("f","total func","l")
		legend.AddEntry("f1","gaus1","l")
		legend.AddEntry("f2","gaus2","l")
		legend.AddEntry("f3","gaus3","l")
		legend.Draw()

		mean_dict[str(b)+"_"+textA] = A.GetMean()

	    elif b == "5GeV":
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
	   
		A.Fit(f,"S",'',0,1.0)
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
	    	f1.Draw("same")
	    	f2.Draw("same")
	    	f3.Draw("same")
		legend.SetHeader("Fit range : 0.4 - 1.0","C")
		legend.AddEntry(a,"MC","le")
		legend.AddEntry("f","total func","l")
		legend.AddEntry("f1","gaus1","l")
		legend.AddEntry("f2","gaus2","l")
		legend.AddEntry("f3","gaus3","l")
		legend.Draw()

		mean_dict[str(b)+"_"+textA] = A.GetMean()

	    elif b == "10GeV":
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
	   
		A.Fit(f,"S",'',0,1.0)
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
	    	f1.Draw("same")
	    	f2.Draw("same")
	    	f3.Draw("same")
		legend.SetHeader("Fit range : 0.4 - 1.0","C")
		legend.AddEntry(a,"MC","le")
		legend.AddEntry("f","total func","l")
		legend.AddEntry("f1","gaus1","l")
		legend.AddEntry("f2","gaus2","l")
		legend.AddEntry("f3","gaus3","l")
		legend.Draw()

		mean_dict[str(b)+"_"+textA] = A.GetMean()

	    elif b == "20GeV":
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
	   
		A.Fit(f,"S",'',0,1.0)
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
	    	f1.Draw("same")
	    	f2.Draw("same")
	    	f3.Draw("same")
		legend.SetHeader("Fit range : 0.5 - 1.0","C")
		legend.AddEntry(a,"MC","le")
		legend.AddEntry("f","total func","l")
		legend.AddEntry("f1","gaus1","l")
		legend.AddEntry("f2","gaus2","l")
		legend.AddEntry("f3","gaus3","l")
		legend.Draw()
		
		mean_dict[str(b)+"_"+textA] = A.GetMean()

	    elif b == "50GeV":
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
	   
		A.Fit(f,"S",'',0,1.0)
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
	    	f1.Draw("same")
	    	f2.Draw("same")
	    	f3.Draw("same")
		legend.SetHeader("Fit range : 0.4 - 1.0","C")
		legend.AddEntry(a,"MC","le")
		legend.AddEntry("f","total func","l")
		legend.AddEntry("f1","gaus1","l")
		legend.AddEntry("f2","gaus2","l")
		legend.AddEntry("f3","gaus3","l")
		legend.Draw()
		
		mean_dict[str(b)+"_"+textA] = A.GetMean()

	    elif b == "100GeV":
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
	   
		A.Fit(f,"S",'',0,1.0)
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
	    	f1.Draw("same")
	    	f2.Draw("same")
	    	f3.Draw("same")
		legend.SetHeader("Fit range : 0.4 - 1.0","C")
		legend.AddEntry(a,"MC","le")
		legend.AddEntry("f","total func","l")
		legend.AddEntry("f1","gaus1","l")
		legend.AddEntry("f2","gaus2","l")
		legend.AddEntry("f3","gaus3","l")
		legend.Draw()
		
		mean_dict[str(b)+"_"+textA] = A.GetMean()

	    elif b == "200GeV" :
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
	   
		A.Fit(f,"S",'',0,1.0)
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
	    	f1.Draw("same")
	    	f2.Draw("same")
	    	f3.Draw("same")
		legend.SetHeader("Fit range : 0.4 - 1.0","C")
		legend.AddEntry(a,"MC","le")
		legend.AddEntry("f","total func","l")
		legend.AddEntry("f1","gaus1","l")
		legend.AddEntry("f2","gaus2","l")
		legend.AddEntry("f3","gaus3","l")
		legend.Draw()
		
		mean_dict[str(b)+"_"+textA] = A.GetMean()

	    else : 
		print 'Dont have this energy'
		quit()

	elif textA == "fPi0" :
	    if b == "1GeV":
		f = TF1("landaugaus","landau(0)+gaus(3)",0.1,1)
	    	f.SetParName(0,"landau.Constant")
	    	f.SetParName(1,"landau.MPV")
	    	f.SetParName(2,"landau.Sigma")
	    	f.SetParName(3,"gaus.Constant")
	    	f.SetParName(4,"gaus.Mean")
	    	f.SetParName(5,"gaus.Sigma")
	  
		# Initial value and limit
	    	f.SetParameter(0,1000)
	    	f.SetParLimits(0,0,5000)
	    	
		f.SetParameter(1,0.5)
	    	f.SetParLimits(1,0,0.5)
	    	
		f.SetParameter(2,0.1)
	    	f.SetParLimits(2,0,1)
	    	
	    	f.SetParameter(3,300)
	    	f.SetParLimits(3,0,1000)
	    	
		f.SetParameter(4,0.5)
	    	f.SetParLimits(4,0.3,0.7)
	    	
		f.SetParameter(5,0.1)
	    	f.SetParLimits(5,0,1)
	    	
		A.Fit(f,"S",'',0.1,1)
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
	    	flandau.Draw("same")
	    	fgaus.Draw("same")
	    
	    elif b == "2GeV":
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
	    	f.SetParameter(0,5000)
	    	f.SetParLimits(0,0,10000)
	    	
		f.SetParameter(1,0.15)
	    	f.SetParLimits(1,0,0.2)
	    	
		f.SetParameter(2,0.03)
	    	f.SetParLimits(2,0,0.1)
	    	
	    	f.SetParameter(3,300)
	    	f.SetParLimits(3,0,1000)
	    	
		f.SetParameter(4,0.2)
	    	f.SetParLimits(4,0.1,0.4)
	    	
		f.SetParameter(5,0.1)
	    	f.SetParLimits(5,0,1)
	    	
	    	f.SetParameter(6,300)
	    	f.SetParLimits(6,0,1000)
	    	
		f.SetParameter(7,0.5)
	    	f.SetParLimits(7,0.3,0.7)
	    	
		f.SetParameter(8,0.1)
	    	f.SetParLimits(8,0,1)
		
		A.Fit(f,"S",'',0,1)
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
	    	fgaus1.Draw("same")
	    	fgaus2.Draw("same")
	    
	    elif b == "5GeV":
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
	    	f.SetParameter(0,5000)
	    	f.SetParLimits(0,0,10000)
	    	
		f.SetParameter(1,0.05)
	    	f.SetParLimits(1,0,0.1)
	    	
		f.SetParameter(2,0.03)
	    	f.SetParLimits(2,0,0.1)
	    	
	    	f.SetParameter(3,1000)
	    	f.SetParLimits(3,0,10000)
	    	
		f.SetParameter(4,0.1)
	    	f.SetParLimits(4,0.05,0.25)
	    	
		f.SetParameter(5,0.1)
	    	f.SetParLimits(5,0,1)
	    	
	    	f.SetParameter(6,300)
	    	f.SetParLimits(6,0,1000)
	    	
		f.SetParameter(7,0.5)
	    	f.SetParLimits(7,0.3,0.7)
	    	
		f.SetParameter(8,0.1)
	    	f.SetParLimits(8,0,1)
		
		A.Fit(f,"S",'',0,1)
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
	    	f1.Draw("same")
	    	f2.Draw("same")
	    	f3.Draw("same")
	    
	    elif b == "10GeV":
		f = TF1("landaugaus","landau(0)+gaus(3)",0,1)
	    	f.SetParName(0,"landau.Constant")
	    	f.SetParName(1,"landau.MPV")
	    	f.SetParName(2,"landau.Sigma")
	    	f.SetParName(3,"gaus.Constant")
	    	f.SetParName(4,"gaus.Mean")
	    	f.SetParName(5,"gaus.Sigma")
	  
		# Initial value and limit
	    	f.SetParameter(0,3000)
	    	f.SetParLimits(0,0,10000)
	    	
		f.SetParameter(1,0.1)
	    	f.SetParLimits(1,0,1)
	    	
		f.SetParameter(2,0.1)
	    	f.SetParLimits(2,0,1)
	    	
	    	f.SetParameter(3,1000)
	    	f.SetParLimits(3,0,10000)
	    	
		f.SetParameter(4,0.5)
	    	f.SetParLimits(4,0,1)
	    	
		f.SetParameter(5,0.1)
	    	f.SetParLimits(5,0,1)
	    	
		A.Fit(f,"S",'',0,1)
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
	    	f1.Draw("same")
	    	f2.Draw("same")
	    
	    elif b == "20GeV":
		f = TF1("doublegaus","gaus(0)+gaus(3)",0,1)
	    	f.SetParName(0,"gaus1.Constant")
	    	f.SetParName(1,"gaus1.Mean")
	    	f.SetParName(2,"gaus1.Sigma")
	    	f.SetParName(3,"gaus2.Constant")
	    	f.SetParName(4,"gaus2.Mean")
	    	f.SetParName(5,"gaus2.Sigma")
		
		# Initial value and limit
	    	f.SetParameter(0,1000)
	    	f.SetParLimits(0,0,10000)
	    	
		f.SetParameter(1,0.5)
	    	f.SetParLimits(1,0.3,1)
	    	
		f.SetParameter(2,0.1)
	    	f.SetParLimits(2,0,1)
	    	
		f.SetParameter(3,1000)
	    	f.SetParLimits(3,0,3000)
	    	
		f.SetParameter(4,0.7)
	    	f.SetParLimits(4,0.3,1)
	    	
		f.SetParameter(5,0.1)
	    	f.SetParLimits(5,0,1)
	   
		A.Fit(f,"S",'',0,1.0)
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
	    	f1.Draw("same")
	    	f2.Draw("same")
	    
	    elif b == "50GeV":
		f = TF1("doublegaus","gaus(0)+gaus(3)",0,1)
	    	f.SetParName(0,"gaus1.Constant")
	    	f.SetParName(1,"gaus1.Mean")
	    	f.SetParName(2,"gaus1.Sigma")
	    	f.SetParName(3,"gaus2.Constant")
	    	f.SetParName(4,"gaus2.Mean")
	    	f.SetParName(5,"gaus2.Sigma")
		
		# Initial value and limit
	    	f.SetParameter(0,1000)
	    	f.SetParLimits(0,0,10000)
	    	
		f.SetParameter(1,0.5)
	    	f.SetParLimits(1,0.3,1)
	    	
		f.SetParameter(2,0.1)
	    	f.SetParLimits(2,0,1)
	    	
		f.SetParameter(3,1000)
	    	f.SetParLimits(3,0,3000)
	    	
		f.SetParameter(4,0.7)
	    	f.SetParLimits(4,0.3,1)
	    	
		f.SetParameter(5,0.1)
	    	f.SetParLimits(5,0,1)
	   
		A.Fit(f,"S",'',0,1.0)
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
	    	f1.Draw("same")
	    	f2.Draw("same")

	    elif b == "100GeV":
		f = TF1("doublegaus","gaus(0)+gaus(3)",0,1)
	    	f.SetParName(0,"gaus1.Constant")
	    	f.SetParName(1,"gaus1.Mean")
	    	f.SetParName(2,"gaus1.Sigma")
	    	f.SetParName(3,"gaus2.Constant")
	    	f.SetParName(4,"gaus2.Mean")
	    	f.SetParName(5,"gaus2.Sigma")
		
		# Initial value and limit
	    	f.SetParameter(0,1000)
	    	f.SetParLimits(0,0,10000)
	    	
		f.SetParameter(1,0.5)
	    	f.SetParLimits(1,0.3,1)
	    	
		f.SetParameter(2,0.1)
	    	f.SetParLimits(2,0,1)
	    	
		f.SetParameter(3,1000)
	    	f.SetParLimits(3,0,3000)
	    	
		f.SetParameter(4,0.7)
	    	f.SetParLimits(4,0.3,1)
	    	
		f.SetParameter(5,0.1)
	    	f.SetParLimits(5,0,1)
	   
		A.Fit(f,"S",'',0,1.0)
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
	    	f1.Draw("same")
	    	f2.Draw("same")

	    elif b == "200GeV" :
		f = TF1("doublegaus","gaus(0)+gaus(3)",0,1)
	    	f.SetParName(0,"gaus1.Constant")
	    	f.SetParName(1,"gaus1.Mean")
	    	f.SetParName(2,"gaus1.Sigma")
	    	f.SetParName(3,"gaus2.Constant")
	    	f.SetParName(4,"gaus2.Mean")
	    	f.SetParName(5,"gaus2.Sigma")
		
		# Initial value and limit
	    	f.SetParameter(0,1000)
	    	f.SetParLimits(0,0,10000)
	    	
		f.SetParameter(1,0.5)
	    	f.SetParLimits(1,0.3,1)
	    	
		f.SetParameter(2,0.1)
	    	f.SetParLimits(2,0,1)
	    	
		f.SetParameter(3,1000)
	    	f.SetParLimits(3,0,3000)
	    	
		f.SetParameter(4,0.7)
	    	f.SetParLimits(4,0.3,1)
	    	
		f.SetParameter(5,0.1)
	    	f.SetParLimits(5,0,1)
	   
		A.Fit(f,"S",'',0,1.0)
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
	    	f1.Draw("same")
	    	f2.Draw("same")

	    else : 
		print 'Dont have this energy'
		quit()
	
	elif textA == "fPi0L" :
	    if b == "1GeV":
		f = TF1("doublegaus","gaus(0)+gaus(3)",0,1)
	    	f.SetParName(0,"gaus1.Constant")
	    	f.SetParName(1,"gaus1.Mean")
	    	f.SetParName(2,"gaus1.Sigma")
	    	f.SetParName(3,"gaus2.Constant")
	    	f.SetParName(4,"gaus2.Mean")
	    	f.SetParName(5,"gaus2.Sigma")
		
		# Initial value and limit
	    	f.SetParameter(0,300)
	    	f.SetParLimits(0,0,1000)
	    	
		f.SetParameter(1,0.5)
	    	f.SetParLimits(1,0,1)
	    	
		f.SetParameter(2,0.1)
	    	f.SetParLimits(2,0,1)
	    	
		f.SetParameter(3,100)
	    	f.SetParLimits(3,0,1000)
	    	
		f.SetParameter(4,0.5)
	    	f.SetParLimits(4,0,1)
	    	
		f.SetParameter(5,0.1)
	    	f.SetParLimits(5,0,1)
	   
		A.Fit(f,"S",'',0,1)
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
	    	f1.Draw("same")
	    	f2.Draw("same")
	    
	    elif b == "2GeV":
		f = TF1("doublegaus","gaus(0)+gaus(3)",0,1)
	    	f.SetParName(0,"gaus1.Constant")
	    	f.SetParName(1,"gaus1.Mean")
	    	f.SetParName(2,"gaus1.Sigma")
	    	f.SetParName(3,"gaus2.Constant")
	    	f.SetParName(4,"gaus2.Mean")
	    	f.SetParName(5,"gaus2.Sigma")
		
		# Initial value and limit
	    	f.SetParameter(0,300)
	    	f.SetParLimits(0,0,1000)
	    	
		f.SetParameter(1,0.5)
	    	f.SetParLimits(1,0,1)
	    	
		f.SetParameter(2,0.1)
	    	f.SetParLimits(2,0,1)
	    	
		f.SetParameter(3,100)
	    	f.SetParLimits(3,0,1000)
	    	
		f.SetParameter(4,0.5)
	    	f.SetParLimits(4,0,1)
	    	
		f.SetParameter(5,0.1)
	    	f.SetParLimits(5,0,1)
	   
		A.Fit(f,"S",'',0,1)
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
	    	f1.Draw("same")
	    	f2.Draw("same")
	    
	    elif b == "5GeV":
		f = TF1("landaugaus","landau(0)+gaus(3)",0,1)
	    	f.SetParName(0,"landau.Constant")
	    	f.SetParName(1,"landau.MPV")
	    	f.SetParName(2,"landau.Sigma")
	    	f.SetParName(3,"gaus.Constant")
	    	f.SetParName(4,"gaus.Mean")
	    	f.SetParName(5,"gaus.Sigma")
	  
		# Initial value and limit
	    	f.SetParameter(0,3000)
	    	f.SetParLimits(0,0,10000)
	    	
		f.SetParameter(1,0.1)
	    	f.SetParLimits(1,0,1)
	    	
		f.SetParameter(2,0.1)
	    	f.SetParLimits(2,0,1)
	    	
	    	f.SetParameter(3,1000)
	    	f.SetParLimits(3,0,10000)
	    	
		f.SetParameter(4,0.5)
	    	f.SetParLimits(4,0,1)
	    	
		f.SetParameter(5,0.1)
	    	f.SetParLimits(5,0,1)
	    	
		A.Fit(f,"S",'',0,1)
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
	    	f1.Draw("same")
	    	f2.Draw("same")
	    
	    elif b == "10GeV":
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
	    	
		A.Fit(f,"S",'',0,1)
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
	


    canvas.Print("./plots/1D_" + b +"_"+ textA + ".png")
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
'RezaAnalysis_200GeV',
'RezaAnalysis_100GeV',
'RezaAnalysis_50GeV',
'RezaAnalysis_20GeV',
'RezaAnalysis_10GeV',
'RezaAnalysis_5GeV',
'RezaAnalysis_2GeV',
'RezaAnalysis_1GeV',
]

#variable = ['fDp','fPi0','fPi0L', 'Class']
variable = ['fDp']
#variable = ['fPi0']
#variable = ['fPi0L']

if not os.path.exists('./plots'):
    os.system('mkdir -p plots')

for num, sample in enumerate(samples):
    for v in variable:
        file1 = ROOT.TFile.Open('Hist'+sample+'.root')
        if v not in  [file1.GetListOfKeys()[ih].GetName() for ih in range(file1.GetListOfKeys().GetSize())]:
            print('do not find the hist')
            continue
        histA = file1.Get(v)
        print sample + v
        draw1dHist(histA, v, sample, doFit=True)
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
drawLinearityCheck()
