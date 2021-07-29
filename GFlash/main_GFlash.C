#include "GFlash.h"

int main(){
TChain* TC;

TC = new TChain("g4SimHits/eventTree") ;
TC ->Add("~/SE_UserHome/FastSimCalo/200k//RezaAnalysis_1GeV*");
GFlash GFRezaAnalysis_1GeV(TC);
GFRezaAnalysis_1GeV.Loop("RezaAnalysis_1GeV");
delete TC;

TC = new TChain("g4SimHits/eventTree") ;
TC ->Add("~/SE_UserHome/FastSimCalo/200k//RezaAnalysis_2GeV*");
GFlash GFRezaAnalysis_2GeV(TC);
GFRezaAnalysis_2GeV.Loop("RezaAnalysis_2GeV");
delete TC;

TC = new TChain("g4SimHits/eventTree") ;
TC ->Add("~/SE_UserHome/FastSimCalo/200k//RezaAnalysis_5GeV*");
GFlash GFRezaAnalysis_5GeV(TC);
GFRezaAnalysis_5GeV.Loop("RezaAnalysis_5GeV");
delete TC;

TC = new TChain("g4SimHits/eventTree") ;
TC ->Add("~/SE_UserHome/FastSimCalo/200k//RezaAnalysis_7GeV*");
GFlash GFRezaAnalysis_7GeV(TC);
GFRezaAnalysis_7GeV.Loop("RezaAnalysis_7GeV");
delete TC;

TC = new TChain("g4SimHits/eventTree") ;
TC ->Add("~/SE_UserHome/FastSimCalo/200k//RezaAnalysis_10GeV*");
GFlash GFRezaAnalysis_10GeV(TC);
GFRezaAnalysis_10GeV.Loop("RezaAnalysis_10GeV");
delete TC;

TC = new TChain("g4SimHits/eventTree") ;
TC ->Add("~/SE_UserHome/FastSimCalo/200k//RezaAnalysis_15GeV*");
GFlash GFRezaAnalysis_15GeV(TC);
GFRezaAnalysis_15GeV.Loop("RezaAnalysis_15GeV");
delete TC;

TC = new TChain("g4SimHits/eventTree") ;
TC ->Add("~/SE_UserHome/FastSimCalo/200k//RezaAnalysis_20GeV*");
GFlash GFRezaAnalysis_20GeV(TC);
GFRezaAnalysis_20GeV.Loop("RezaAnalysis_20GeV");
delete TC;

TC = new TChain("g4SimHits/eventTree") ;
TC ->Add("~/SE_UserHome/FastSimCalo/200k//RezaAnalysis_30GeV*");
GFlash GFRezaAnalysis_30GeV(TC);
GFRezaAnalysis_30GeV.Loop("RezaAnalysis_30GeV");
delete TC;

TC = new TChain("g4SimHits/eventTree") ;
TC ->Add("~/SE_UserHome/FastSimCalo/200k//RezaAnalysis_40GeV*");
GFlash GFRezaAnalysis_40GeV(TC);
GFRezaAnalysis_40GeV.Loop("RezaAnalysis_40GeV");
delete TC;

TC = new TChain("g4SimHits/eventTree") ;
TC ->Add("~/SE_UserHome/FastSimCalo/200k//RezaAnalysis_50GeV*");
GFlash GFRezaAnalysis_50GeV(TC);
GFRezaAnalysis_50GeV.Loop("RezaAnalysis_50GeV");
delete TC;

TC = new TChain("g4SimHits/eventTree") ;
TC ->Add("~/SE_UserHome/FastSimCalo/200k//RezaAnalysis_70GeV*");
GFlash GFRezaAnalysis_70GeV(TC);
GFRezaAnalysis_70GeV.Loop("RezaAnalysis_70GeV");
delete TC;

TC = new TChain("g4SimHits/eventTree") ;
TC ->Add("~/SE_UserHome/FastSimCalo/200k//RezaAnalysis_100GeV*");
GFlash GFRezaAnalysis_100GeV(TC);
GFRezaAnalysis_100GeV.Loop("RezaAnalysis_100GeV");
delete TC;

TC = new TChain("g4SimHits/eventTree") ;
TC ->Add("~/SE_UserHome/FastSimCalo/200k//RezaAnalysis_150GeV*");
GFlash GFRezaAnalysis_150GeV(TC);
GFRezaAnalysis_150GeV.Loop("RezaAnalysis_150GeV");
delete TC;

TC = new TChain("g4SimHits/eventTree") ;
TC ->Add("~/SE_UserHome/FastSimCalo/200k//RezaAnalysis_200GeV*");
GFlash GFRezaAnalysis_200GeV(TC);
GFRezaAnalysis_200GeV.Loop("RezaAnalysis_200GeV");
delete TC;

TC = new TChain("g4SimHits/eventTree") ;
TC ->Add("~/SE_UserHome/FastSimCalo/200k//RezaAnalysis_300GeV*");
GFlash GFRezaAnalysis_300GeV(TC);
GFRezaAnalysis_300GeV.Loop("RezaAnalysis_300GeV");
delete TC;

TC = new TChain("g4SimHits/eventTree") ;
TC ->Add("~/SE_UserHome/FastSimCalo/200k//RezaAnalysis_400GeV*");
GFlash GFRezaAnalysis_400GeV(TC);
GFRezaAnalysis_400GeV.Loop("RezaAnalysis_400GeV");
delete TC;

TC = new TChain("g4SimHits/eventTree") ;
TC ->Add("~/SE_UserHome/FastSimCalo/200k//RezaAnalysis_500GeV*");
GFlash GFRezaAnalysis_500GeV(TC);
GFRezaAnalysis_500GeV.Loop("RezaAnalysis_500GeV");
delete TC;

}
