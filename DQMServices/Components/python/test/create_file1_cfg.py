import FWCore.ParameterSet.Config as cms
import DQMTools.Tests.checkBooking as booking
import DQMTools.Tests.createElements as c
import sys

process = cms.Process("TEST")

b = booking.BookingParams(sys.argv)
b.doCheck(testOnly=False)

process.source = cms.Source("EmptySource", numberEventsInRun = cms.untracked.uint32(100),
                            firstLuminosityBlock = cms.untracked.uint32(1),
                            firstEvent = cms.untracked.uint32(1),
                            numberEventsInLuminosityBlock = cms.untracked.uint32(1))

elements = c.createElements()
readRunElements = c.createReadRunElements()
readLumiElements = c.createReadLumiElements()

process.filler = cms.EDAnalyzer("DummyBookFillDQMStore",
                                folder    = cms.untracked.string("TestFolder/"),
                                elements  = cms.untracked.VPSet(*elements),
                                fillRuns  = cms.untracked.bool(True),
                                fillLumis = cms.untracked.bool(True),
                                book_at_constructor = cms.untracked.bool(b.getBookLogic('CTOR')),
                                book_at_beginJob = cms.untracked.bool(b.getBookLogic('BJ')),
                                book_at_beginRun = cms.untracked.bool(b.getBookLogic('BR')))

process.reader = cms.EDAnalyzer("DummyTestReadDQMStore",
                                folder = cms.untracked.string("TestFolder/"),
                                runElements = cms.untracked.VPSet(*readRunElements),
                                lumiElements = cms.untracked.VPSet(*readLumiElements) )

process.out = cms.OutputModule("DQMRootOutputModule",
                               fileName = cms.untracked.string("dqm_file1.root"))


process.p = cms.Path(process.filler)
process.o = cms.EndPath(process.out+process.reader)

process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(10))

process.add_(cms.Service("DQMStore"))
#process.add_(cms.Service("Tracer"))

