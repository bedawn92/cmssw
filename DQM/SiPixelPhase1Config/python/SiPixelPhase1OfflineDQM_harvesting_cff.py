
import FWCore.ParameterSet.Config as cms

from  DQM.SiPixelPhase1Config.SiPixelPhase1OfflineDQM_source_cff import *

siPixelPhase1OfflineDQM_harvesting = cms.Sequence(SiPixelPhase1RawDataHarvester 
                                                + SiPixelPhase1DigisHarvester 
                                                + SiPixelPhase1ClustersHarvester
                                                + SiPixelPhase1RecHitsHarvester
                                                + SiPixelPhase1TrackResidualsHarvester
                                                + SiPixelPhase1TrackClustersHarvester
                                                + SiPixelPhase1TrackEfficiencyHarvester
                                                + SiPixelPhase1RawDataHarvester
                                                + RunQTests_offline
                                                + SiPixelPhase1Summary_Offline
                                                  )

siPixelPhase1OfflineDQM_harvesting_cosmics = siPixelPhase1OfflineDQM_harvesting.copyAndExclude([
   SiPixelPhase1TrackEfficiencyHarvester,
])

siPixelPhase1OfflineDQM_harvesting_hi = siPixelPhase1OfflineDQM_harvesting.copyAndExclude([
   SiPixelPhase1RecHitsHarvester,
   SiPixelPhase1TrackResidualsHarvester
])

siPixelPhase1OfflineDQM_harvesting_cosmics.replace(RunQTests_offline, RunQTests_cosmics)
siPixelPhase1OfflineDQM_harvesting_cosmics.replace(SiPixelPhase1Summary_Offline, SiPixelPhase1Summary_Cosmics)
