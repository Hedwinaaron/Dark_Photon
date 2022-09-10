#!/usr/bin/python3
import os, sys
import ROOT
import numpy as np
import array as arr

# Open a file
path = "/eos/user/h/hencinas/MSSMD_mH_125_mN1_60_mGammaD_0p7_cT_0p1_TuneCP5_13TeV-madgraph-pythia8/private-trial-Darkphoton-MiniAOD/220709_031737/0000/"
files = os.listdir( path )
#create and fill the histogram


h1 = ROOT.TH1D("h1", "Down dGl", 3, 0.0, 3)
h2 = ROOT.TH1D("h2", "Up dGl", 1000, 0.0, 1000.0)
h3= ROOT.TH1D("h3", "Resolution hist", 200, -1, 1)
h4= ROOT.TH1D("h4", "p_T 30-40", 100, -0.3, 0.3)
h5= ROOT.TH1D("h5", "p_T 40-50", 100, -0.3, 0.3)
h6= ROOT.TH1D("h6", "p_T 50-70 ", 100, -0.3, 0.3)
h7= ROOT.TH1D("h7", "p_T 70-100", 100, -0.3, 0.3)
h8= ROOT.TH1D("h8", "p_T 100-150", 100, -0.3, 0.3)
h9= ROOT.TH1D("h9", "p_T 150-200", 100, -0.3, 0.3)
h10= ROOT.TH1D("h10", "p_T 200-350", 100, -0.3, 0.3)
h11= ROOT.TH1D("h11", "p_T 350-500", 100, -0.3, 0.3)
h32= ROOT.TH1D("h132", "p_T 500-1000", 100, -0.3, 0.3)
h12= ROOT.TH1D("h12", "Up |dz|", 400, 0, 400)
h13= ROOT.TH1D("h13", "Up |dxy|", 400, 0, 120)
h14= ROOT.TH1D("h14", "Down |dz|", 400, 0, 400)
h15= ROOT.TH1D("h15", "Down |dxy|", 400, 0, 120)





#relevant variables
entry_down=0
entry_up=0
downdgl_pt=0
updgl_pt=0
k=-1
inv_Uppt=0
inv_Downpt=0
res=0
pt_bin=np.array([30,40,50,70,100,150,200,350,500,1000])
dxy_bin=np.array([0,5,10,15,20,30,40,50,80])
dz_bin=np.array([0,5,10,20,30,45,60,80,150])
pass_HL=0.0
pass_cut1=0.0
pass_cut2=0.0
# This would print all the files and directories
#for file in files:
    
    #input the name of the root file
inFileName = "out_ana_1_1.root"
    
#Open root file and get branch
inFile = ROOT.TFile.Open( inFileName ," READ ")
tree = inFile.Get ("cutFlowAnalyzerPXBL4PXFL3/Events")
print("Reading from ", inFileName)    
Entries=tree.GetEntries()
    
print("Entries ",Entries)
    
for i in range(0,Entries):
    tree.GetEntry(i)
    abs_eta=abs(tree.reco4mu_eta)
    print("Event ID",i)
    print ("isSignalHLT_0_Fired",tree.isSignalHLT_0_Fired)
    h1.Fill(tree.isSignalHLT_0_Fired)
    if tree.isSignalHLT_0_Fired==1:
        pass_HL=pass_HL+1
    
        if  (tree.selMu0_SA==1 or  tree.selMu1_SA==1  or tree.selMu2_SA==1 or  tree.selMu3_SA==1):
        
            #Events selection and histogram fillin
            pass_cut1=pass_cut1+1
        if tree.reco4mu_pt>8 and abs_eta<2.4:
            pass_cut2=pass_cut2+1
rel_change1=pass_cut1/pass_HL 
rel_change2=pass_cut2/pass_cut1
print("┌───────────────────────────────────────────────────────────────────────────────────┐")
print("│Applied cut                                 │ Passing events |Relative change      │")
print("├───────────────────────────────────────────────────────────────────────────────────┤")
print("│Passing HL0                                 │",pass_HL,"        │","                 ","  │")  
print("│Passing cut <= 1 SA muon                    │",pass_cut1,"        │",rel_change1," │")
print("│Passing cut 4 muons |eta|<2.4 and pt>8 GeV  │",pass_cut2,"         │",rel_change2,"│")
print("└───────────────────────────────────────────────────────────────────────────────────┘")


#c=ROOT.TCanvas("c","c",1000,700)
#h1.Draw()
#c.SaveAs("wefWFW


    
        
        
        
        
    
        
        
        
        
        
        
        
        
        
        
        
