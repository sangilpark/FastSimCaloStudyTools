#!/bin/sh

Energy="1 2 5 7 10 15 20 30 40 50 70 100 150 200 300 400 500"
#Energy="150 200"
nJobs=200
NevPerJob=1000
outputDest=/store/user/spak/FastSimCalo/200k/
#outputDest=/store/user/spak/FastSimCalo/test/
saveHits=False

for energy in $Energy
do
    echo "create-batch2 cmsRun --cfg runTestWithGun_cfg.py --jobName job_$energy --nJobs $nJobs --maxEvent $NevPerJob --transferDest $outputDest --args 'energy=$energy saveHits=$saveHits'"
    create-batch2 cmsRun --cfg runTestWithGun_cfg.py --jobName job_$energy --nJobs $nJobs --maxEvent $NevPerJob --transferDest $outputDest --args "energy=$energy saveHits=$saveHits"
done
