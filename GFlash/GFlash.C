#define GFlash_cxx
#include "GFlash.h"
#include <TH2.h>
#include <TStyle.h>
#include <TCanvas.h>
#include <cstdlib>
#include <vector>
#include <iostream>
#include <string>
#include <sstream>
#include <fstream>
#include <map>
#include <string>
#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
#include "TH1F.h"
#include "TH2F.h"
#include "TFile.h"
#include "TStyle.h"
#include "TCanvas.h"
#include "TLegend.h"
#include "TPad.h"
#include "TFile.h"
#include "TTree.h"
#include "TChain.h"
#include "TString.h"
#include "TSystem.h"
#include "TROOT.h"
#include "TLine.h"
#include "TStopwatch.h"
#include "THStack.h"
#include "TPaveText.h"
#include "TGraphAsymmErrors.h"
#include <cmath>
#include "TLorentzVector.h"
#include "TPaveText.h"
#include "TPie.h"
#include "TF1.h"
#include "TVector3.h"
#include <TSystemDirectory.h>
#include <TSystemFile.h>
#include "TRandom3.h"

void displayProgress(long current, long max){
  using std::cerr;
  if (max<1000) return;
  if (current%(max/1000)!=0 && current<max-1) return;

  int width = 52; // Hope the terminal is at least that wide.
  int barWidth = width - 2;
  cerr << "\x1B[2K"; // Clear line
  cerr << "\x1B[2000D"; // Cursor left
  cerr << '[';
  for(int i=0 ; i<barWidth ; ++i){ if(i<barWidth*current/max){ cerr << '=' ; }else{ cerr << ' ' ; } }
  cerr << ']';
  cerr << " " << Form("%8d/%8d (%5.2f%%)", (int)current, (int)max, 100.0*current/max) ;
  cerr.flush();
}

void GFlash::Loop(TString fname)
{
//   In a ROOT session, you can do:
//      root> .L GFlash.C
//      root> GFlash t
//      root> t.GetEntry(12); // Fill t data members with entry number 12
//      root> t.Show();       // Show values of entry 12
//      root> t.Show(16);     // Read and show values of entry 16
//      root> t.Loop();       // Loop on all entries
//

//     This is the loop skeleton where:
//    jentry is the global entry number in the chain
//    ientry is the entry number in the current Tree
//  Note that the argument to GetEntry must be:
//    jentry for TChain::GetEntry
//    ientry for TTree::GetEntry and TBranch::GetEntry
//
//       To read only selected branches, Insert statements like:
// METHOD1:
//    fChain->SetBranchStatus("*",0);  // disable all branches
//    fChain->SetBranchStatus("branchname",1);  // activate branchname
// METHOD2: replace line
//    fChain->GetEntry(jentry);       //read all branches
//by  b_branchname->GetEntry(ientry); //read only this branch

   TFile *f = new TFile("Hist"+fname+".root","RECREATE");
   f->cd();

   double hcalradlen =14.3;
   double hcalintlen =185;
   TH1F *fDp, *fDp_SPbeforeECAL, *fDp_SPinECAL, *fDp_SPinHCAL;
   TH1F *fPi0, *fPi0_SPbeforeECAL, *fPi0_SPinECAL, *fPi0_SPinHCAL;
   TH1F *fPi0L, *fPi0L_SPbeforeECAL, *fPi0L_SPinECAL, *fPi0L_SPinHCAL;
   TH1F *HADshapeIL;
   TH1F *Class, *Class_SPbeforeECAL, *Class_SPinECAL, *Class_SPinHCAL;
   fDp = new TH1F( "fDp", "fDp" ,   100, 0  , 1    );
   fDp_SPbeforeECAL = new TH1F( "fDp_SPbeforeECAL", "fDp_SPbeforeECAL" ,   100, 0  , 1    );
   fDp_SPinECAL = new TH1F( "fDp_SPinECAL", "fDp_SPinECAL" ,   100, 0  , 1    );
   fDp_SPinHCAL = new TH1F( "fDp_SPinHCAL", "fDp_SPinHCAL" ,   100, 0  , 1    );
   
   fPi0 = new TH1F( "fPi0", "fPi0" ,   100, 0  , 1    );
   fPi0_SPbeforeECAL = new TH1F( "fPi0_SPbeforeECAL", "fPi0_SPbeforeECAL" ,   100, 0  , 1    );
   fPi0_SPinECAL = new TH1F( "fPi0_SPinECAL", "fPi0_SPinECAL" ,   100, 0  , 1    );
   fPi0_SPinHCAL = new TH1F( "fPi0_SPinHCAL", "fPi0_SPinHCAL" ,   100, 0  , 1    );
   
   fPi0L = new TH1F( "fPi0L", "fPi0L" ,   100, 0  , 1    );
   fPi0L_SPbeforeECAL = new TH1F( "fPi0L_SPbeforeECAL", "fPi0L_SPbeforeECAL" ,   100, 0  , 1    );
   fPi0L_SPinECAL = new TH1F( "fPi0L_SPinECAL", "fPi0L_SPinECAL" ,   100, 0  , 1    );
   fPi0L_SPinHCAL = new TH1F( "fPi0L_SPinHCAL", "fPi0L_SPinHCAL" ,   100, 0  , 1    );
   
   Class = new TH1F( "Class", "Class" ,   4, 0  , 4    );
   Class_SPbeforeECAL = new TH1F( "Class_SPbeforeECAL", "Class_SPbeforeECAL" ,   4, 0  , 4    );
   Class_SPinECAL = new TH1F( "Class_SPinECAL", "Class_SPinECAL" ,   4, 0  , 4    );
   Class_SPinHCAL = new TH1F( "Class_SPinHCAL", "Class_SPinHCAL" ,   4, 0  , 4    );

   if (fChain == 0) return;

   Int_t nentries = (Int_t) fChain->GetEntries();
   float N = float(nentries);

   Long64_t nbytes = 0, nb = 0;
   TCanvas *c1;
   stringstream ss;
   stringstream Intgral;
   for (Long64_t jentry=0; jentry<nentries;jentry++) {
//   for (Long64_t jentry=0; jentry<10;jentry++) {
      Long64_t ientry = LoadTree(jentry);
      if (ientry < 0) break;
      nb = fChain->GetEntry(jentry);   nbytes += nb;
    displayProgress(jentry, nentries) ;

      HADshapeIL = new TH1F( "had","had" ,   60, 0  , 20    );
      for (int b = 1; b < h_eHadronic->GetNbinsX(); ++b){
          HADshapeIL->Fill((h_eHadronic->GetXaxis()->GetBinCenter(b) - sim_pvIneInt_z)/hcalintlen, h_eHadronic->GetBinContent(b));
      }

      delete HADshapeIL;

      fDp->Fill(sim_eTotal/p_E);
      if(sim_ePi0First+sim_ePi0Late !=0) fPi0->Fill((sim_ePi0First+sim_ePi0Late)/sim_eTotal);
      if(sim_ePi0First!=0 && sim_ePi0Late !=0) fPi0L->Fill(sim_ePi0Late/(sim_ePi0First+sim_ePi0Late));

      if(sim_ePi0First+sim_ePi0Late ==0) Class->Fill(0.5,1/N);
      if(sim_ePi0First!=0 && sim_ePi0Late ==0) Class->Fill(1.5,1/N);   
      if(sim_ePi0First==0 && sim_ePi0Late !=0) Class->Fill(2.5,1/N);
      if(sim_ePi0First!=0 && sim_ePi0Late !=0) Class->Fill(3.5,1/N);
	
      // SP before ECAL
      if(sim_pvIneInt_z<1290){
	fDp_SPbeforeECAL->Fill(sim_eTotal/p_E);
      	if(sim_ePi0First+sim_ePi0Late !=0) fPi0_SPbeforeECAL->Fill((sim_ePi0First+sim_ePi0Late)/sim_eTotal);
      	if(sim_ePi0First!=0 && sim_ePi0Late !=0) fPi0L_SPbeforeECAL->Fill(sim_ePi0Late/(sim_ePi0First+sim_ePi0Late));
        if(sim_ePi0First+sim_ePi0Late ==0) Class_SPbeforeECAL->Fill(0.5,1/N);
        if(sim_ePi0First!=0 && sim_ePi0Late ==0) Class_SPbeforeECAL->Fill(1.5,1/N);   
        if(sim_ePi0First==0 && sim_ePi0Late !=0) Class_SPbeforeECAL->Fill(2.5,1/N);
        if(sim_ePi0First!=0 && sim_ePi0Late !=0) Class_SPbeforeECAL->Fill(3.5,1/N);
      };

      // SP in ECAL
      if(sim_pvIneInt_z>1290 && sim_pvIneInt_z<1790){
	fDp_SPinECAL->Fill(sim_eTotal/p_E);
      	if(sim_ePi0First+sim_ePi0Late !=0) fPi0_SPinECAL->Fill((sim_ePi0First+sim_ePi0Late)/sim_eTotal);
      	if(sim_ePi0First!=0 && sim_ePi0Late !=0) fPi0L_SPinECAL->Fill(sim_ePi0Late/(sim_ePi0First+sim_ePi0Late));
        if(sim_ePi0First+sim_ePi0Late ==0) Class_SPinECAL->Fill(0.5,1/N);
        if(sim_ePi0First!=0 && sim_ePi0Late ==0) Class_SPinECAL->Fill(1.5,1/N);   
        if(sim_ePi0First==0 && sim_ePi0Late !=0) Class_SPinECAL->Fill(2.5,1/N);
        if(sim_ePi0First!=0 && sim_ePi0Late !=0) Class_SPinECAL->Fill(3.5,1/N);
	// SP in ECAL, Edep in ECAL
	
      };
      
      // SP in HCAL
      if(sim_pvIneInt_z>1790 && sim_pvIneInt_z<2950){
	fDp_SPinHCAL->Fill(sim_eTotal/p_E);
      	if(sim_ePi0First+sim_ePi0Late !=0) fPi0_SPinHCAL->Fill((sim_ePi0First+sim_ePi0Late)/sim_eTotal);
      	if(sim_ePi0First!=0 && sim_ePi0Late !=0) fPi0L_SPinHCAL->Fill(sim_ePi0Late/(sim_ePi0First+sim_ePi0Late));
        if(sim_ePi0First+sim_ePi0Late ==0) Class_SPinHCAL->Fill(0.5,1/N);
        if(sim_ePi0First!=0 && sim_ePi0Late ==0) Class_SPinHCAL->Fill(1.5,1/N);   
        if(sim_ePi0First==0 && sim_ePi0Late !=0) Class_SPinHCAL->Fill(2.5,1/N);
        if(sim_ePi0First!=0 && sim_ePi0Late !=0) Class_SPinHCAL->Fill(3.5,1/N);
      };

      //if(sim_pvIneInt_z>2950){
      //};




  }
  const Int_t nx = 4;
  const char *type[nx] = {"H","H+#pi_{0}^{f}","H+#pi_{0}^{l}","H+#pi_{0}^{f}+#pi_{0}^{l}"};

  Int_t i;
  for (i=1;i<=nx;i++) {
     Class->GetXaxis()->SetBinLabel(i,type[i-1]);
     Class->GetXaxis()->SetLabelSize(0.07);
  }

  fPi0->Write("",TObject::kOverwrite);
  fPi0_SPbeforeECAL->Write("",TObject::kOverwrite);
  fPi0_SPinECAL->Write("",TObject::kOverwrite);
  fPi0_SPinHCAL->Write("",TObject::kOverwrite);
  fDp->Write("",TObject::kOverwrite);
  fDp_SPbeforeECAL->Write("",TObject::kOverwrite);
  fDp_SPinECAL->Write("",TObject::kOverwrite);
  fDp_SPinHCAL->Write("",TObject::kOverwrite);
  fPi0L->Write("",TObject::kOverwrite);
  fPi0L_SPbeforeECAL->Write("",TObject::kOverwrite);
  fPi0L_SPinECAL->Write("",TObject::kOverwrite);
  fPi0L_SPinHCAL->Write("",TObject::kOverwrite);
  Class->Write("",TObject::kOverwrite);
  Class_SPbeforeECAL->Write("",TObject::kOverwrite);
  Class_SPinECAL->Write("",TObject::kOverwrite);
  Class_SPinHCAL->Write("",TObject::kOverwrite);
  
  delete fPi0;
  delete fPi0_SPbeforeECAL;
  delete fPi0_SPinECAL;
  delete fPi0_SPinHCAL;
  delete fDp;
  delete fDp_SPbeforeECAL;
  delete fDp_SPinECAL;
  delete fDp_SPinHCAL;
  delete fPi0L;
  delete fPi0L_SPbeforeECAL;
  delete fPi0L_SPinECAL;
  delete fPi0L_SPinHCAL;
  delete Class;
  delete Class_SPbeforeECAL;
  delete Class_SPinECAL;
  delete Class_SPinHCAL;
  f->Close();
}
