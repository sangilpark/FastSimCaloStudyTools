#!/bin/sh

# Usage : $ source setup_FastsimCalo.sh

cmsswVer=CMSSW_10_2_6

#export SCRAM_ARCH=slc6_amd64_gcc700
export SCRAM_ARCH=slc7_amd64_gcc700
echo 'Installing ' $cmsswVer

scramv1 project $cmsswVer

cd $cmsswVer/src
eval `scramv1 runtime -sh` #cmsenv

if [ -z $CMSSW_BASE ]; then
    echo "======================================="
    echo "No CMS environment detected; stopping..."
    echo "======================================="
    exit 1
fi

git cms-init
git cms-merge-topic rgoldouz:Hadronic-shower-profile

scramv1 b -j 8
