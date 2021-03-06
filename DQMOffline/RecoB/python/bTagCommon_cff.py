import FWCore.ParameterSet.Config as cms

# BTagPerformanceAnalyzer configuration                                                                                                                                              
from DQMOffline.RecoB.bTagCombinedSVVariables_cff import *
from DQMOffline.RecoB.bTagTrackIPAnalysis_cff import *
from DQMOffline.RecoB.bTagCombinedSVAnalysis_cff import *
from DQMOffline.RecoB.bTagSymmetricAnalysis_cff import *
from DQMOffline.RecoB.bTagTrackCountingAnalysis_cff import *
from DQMOffline.RecoB.bTagTrackProbabilityAnalysis_cff import *
from DQMOffline.RecoB.bTagTrackBProbabilityAnalysis_cff import *
from DQMOffline.RecoB.bTagGenericAnalysis_cff import *
from DQMOffline.RecoB.bTagSimpleSVAnalysis_cff import *
from DQMOffline.RecoB.bTagSoftLeptonAnalysis_cff import *
from DQMOffline.RecoB.cTagGenericAnalysis_cff import *
from DQMOffline.RecoB.cTagCombinedSVVariables_cff import *
from DQMOffline.RecoB.cTagCombinedSVAnalysis_cff import *
from DQMOffline.RecoB.cTagCorrelationAnalysis_cff import *
from DQMOffline.RecoB.bTagGhostTrackAnalysis_cff import *
from DQMOffline.RecoB.bTagGhostTrackVariables_cff import *

bTagCommonBlock = cms.PSet(
    # use pre-computed jet flavour identification
    # new default is to use genparticles - and it is the only option
    # Parameters which are common to all tagger algorithms
    # rec. jet
    ptRecJetMin = cms.double(30.0),
    ptRecJetMax = cms.double(40000.0),
    # eta
    etaMin = cms.double(0.0),
    etaMax = cms.double(2.4),
    # lepton momentum to jet energy ratio, if you use caloJets put ratioMin to -1.0 and ratioMax to 0.8
    ratioMin = cms.double(-9999.0),
    ratioMax = cms.double(9999.0),
    softLeptonInfo = cms.InputTag("softPFElectronsTagInfos"),
    # Section for the jet flavour identification
    jetMCSrc = cms.InputTag("mcJetFlavour"),
    caloJetMCSrc = cms.InputTag(""), #To define only if you use the old flavour tool
    useOldFlavourTool = cms.bool(False), #Recommended only for CaloJets, if True then define caloJetMCSrc and ignore jetMCSrc
    # eta and pt ranges
    ptRanges = cms.vdouble(50.0, 80.0, 120.0),
    etaRanges = cms.vdouble(0.0, 1.4, 2.4),
    #Jet ID and EnergyCorr.
    doJetID = cms.bool(False),
    doJEC = cms.bool(False),
    JECsourceMC = cms.InputTag("ak4PFCHSL1FastL2L3Corrector"),
    JECsourceData = cms.InputTag("ak4PFCHSL1FastL2L3ResidualCorrector"),
    #tagger configuration
    tagConfig = cms.VPSet(
        cms.PSet(
            bTagTrackIPAnalysisBlock,
            type = cms.string('CandIP'),
            label = cms.InputTag("pfImpactParameterTagInfos"),
            folder = cms.string("IPTag")
        ),
        cms.PSet(
            bTagCombinedSVAnalysisBlock,
            listTagInfos = cms.VInputTag(
                cms.InputTag("pfImpactParameterTagInfos"),
                cms.InputTag("pfInclusiveSecondaryVertexFinderTagInfos")
            ),
            type = cms.string('GenericMVA'),
            label = cms.InputTag("candidateCombinedSecondaryVertexV2Computer"),
            folder = cms.string("CSVTag")
        ),
        cms.PSet(
            bTagTrackCountingAnalysisBlock,
            label = cms.InputTag("pfTrackCountingHighEffBJetTags"),
            folder = cms.string("TCHE")
        ),
        cms.PSet(
            bTagProbabilityAnalysisBlock,
            label = cms.InputTag("pfJetProbabilityBJetTags"),
            folder = cms.string("JP")
        ),
        cms.PSet(
            bTagBProbabilityAnalysisBlock,
            label = cms.InputTag("pfJetBProbabilityBJetTags"),
            folder = cms.string("JBP")
        ),
        cms.PSet(
            bTagSimpleSVAnalysisBlock,
            label = cms.InputTag("pfSimpleSecondaryVertexHighEffBJetTags"),
            folder = cms.string("SSVHE")
        ),
        cms.PSet(
            bTagSimpleSVAnalysisBlock,
            label = cms.InputTag("pfSimpleInclusiveSecondaryVertexHighEffBJetTags"),
            folder = cms.string("SISVHE")
        ),
        cms.PSet(
            bTagGenericAnalysisBlock,
            label = cms.InputTag("pfCombinedInclusiveSecondaryVertexV2BJetTags"),
            folder = cms.string("CSVv2"),
            differentialPlots = cms.bool(True),
            discrCut = cms.double(0.5426)
        ),
        cms.PSet(
            bTagSymmetricAnalysisBlock,
            label = cms.InputTag("pfCombinedMVAV2BJetTags"),
            folder = cms.string("combMVAv2"),
            differentialPlots = cms.bool(True),
            discrCut = cms.double(-0.5884)
        ), 
        cms.PSet(
            bTagGenericAnalysisBlock,
            label = cms.InputTag("pfDeepCSVJetTags:probb"),
            folder = cms.string("deepCSV_probb")
        ),
        cms.PSet(
            bTagGenericAnalysisBlock,
            label = cms.InputTag("pfDeepCSVJetTags:probc"),
            folder = cms.string("deepCSV_probc")
        ),
        cms.PSet(
            bTagGenericAnalysisBlock,
            label = cms.InputTag("pfDeepCSVJetTags:probudsg"),
            folder = cms.string("deepCSV_probudsg")
        ),
        cms.PSet(
            bTagGenericAnalysisBlock,
            label = cms.InputTag("pfDeepCSVJetTags:probbb"),
            folder = cms.string("deepCSV_probbb")
        ),
        #cms.PSet(
        #    bTagGenericAnalysisBlock,
        #    label = cms.InputTag("pfDeepCMVAJetTags:probb"),
        #    folder = cms.string("deepCMVA_probb")
        #),
        #cms.PSet(
        #    bTagGenericAnalysisBlock,
        #    label = cms.InputTag("pfDeepCMVAJetTags:probc"),
        #    folder = cms.string("deepCMVA_probc")
        #),
        #cms.PSet(
        #    bTagGenericAnalysisBlock,
        #    label = cms.InputTag("pfDeepCMVAJetTags:probudsg"),
        #    folder = cms.string("deepCMVA_probudsg")
        #),
        #cms.PSet(
        #    bTagGenericAnalysisBlock,
        #    label = cms.InputTag("pfDeepCMVAJetTags:probbb"),
        #    folder = cms.string("deepCMVA_probbb")
        #),
       cms.PSet(
            bTagSoftLeptonAnalysisBlock,
            label = cms.InputTag("softPFMuonBJetTags"),
            folder = cms.string("SMT")
        ),
        cms.PSet(
            bTagSoftLeptonAnalysisBlock,
            label = cms.InputTag("softPFElectronBJetTags"),
            folder = cms.string("SET")
        ),
        cms.PSet(
           cTagCombinedSVAnalysisBlock,
           listTagInfos = cms.VInputTag(
               cms.InputTag("pfImpactParameterTagInfos"),
               cms.InputTag("pfInclusiveSecondaryVertexFinderCvsLTagInfos"),                
               cms.InputTag("softPFMuonsTagInfos"),
               cms.InputTag("softPFElectronsTagInfos")
           ),
           type = cms.string('GenericMVA'),
           label = cms.InputTag("candidateCombinedSecondaryVertexSoftLeptonCvsLComputer"),
           folder = cms.string("CtaggerTag")
        ),
        cms.PSet(
            cTagGenericAnalysisBlock,
            label = cms.InputTag("pfCombinedCvsLJetTags"),
            folder = cms.string("Ctagger_CvsL"),
            doCTagPlots = cms.bool(True),
            differentialPlots = cms.bool(True),
            discrCut = cms.double(-0.48)
        ),
        cms.PSet(
            cTagGenericAnalysisBlock,
            label = cms.InputTag("pfCombinedCvsBJetTags"),
            folder = cms.string("Ctagger_CvsB"),
            doCTagPlots = cms.bool(True),
            differentialPlots = cms.bool(True),
            discrCut = cms.double(-0.17)
        ),
        cms.PSet(
            cTagCorrelationAnalysisBlock,
            type = cms.string('TagCorrelation'),
            label1 = cms.InputTag("pfCombinedCvsLJetTags"),
            label2 = cms.InputTag("pfCombinedCvsBJetTags"),
            folder = cms.string("Ctagger_TagCorrelation"),
            doCTagPlots = cms.bool(True)
        )
    )    
)


