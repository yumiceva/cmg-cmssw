//
// Package:         RecoTracker/RoadSearchHelixMaker/test
// Class:           RoadSearchTrackReader
// 
// Description:     calls RoadSearchTrackReaderAlgorithm to
//                  read and analyze Tracks
//
// Original Author: Oliver Gutsche, gutsche@fnal.gov
// Created:         Wed Mar 29 20:00:00 UTC 2006
//
// $Author: wmtan $
// $Date: 2011/05/20 17:17:32 $
// $Revision: 1.3 $
//

#ifndef RoadSearchTrackReader_h
#define RoadSearchTrackReader_h

#include "FWCore/Framework/interface/EDAnalyzer.h"
#include "FWCore/Framework/interface/Event.h"
#include "DataFormats/Common/interface/Handle.h"
#include "FWCore/Framework/interface/EventSetup.h"


#include "FWCore/ParameterSet/interface/ParameterSet.h"

#include "RecoTracker/RoadSearchHelixMaker/test/RoadSearchTrackReaderAlgorithm.h"

namespace cms
{
  class RoadSearchTrackReader : public edm::EDAnalyzer
  {
  public:

    explicit RoadSearchTrackReader(const edm::ParameterSet& conf);

    virtual ~RoadSearchTrackReader();

    virtual void analyze(const edm::Event& e, const edm::EventSetup& c);

  private:
    RoadSearchTrackReaderAlgorithm readTrackAlgorithm_;
    edm::ParameterSet conf_;

  };
}


#endif
