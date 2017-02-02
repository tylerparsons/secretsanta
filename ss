#!/bin/bash

if [ $# -eq 1 ]
then
    connYear=$1
elif [ $# -ne 0 ]
then
    echo "usage: ss [<connYear>]"
    exit 1
fi

familyFile=families.csv
oldConnFile=oldConns.csv
newConnFile=newConns.csv

python ss.py $familyFile $oldConnFile $newConnFile $connYear
rc=$?
if [ $rc -ne 0 ]
then
    echo ss.py $familyFile $oldConnFile $newConnFile failed rc: $rc
    rm $newConnFile $allConnFile 2>&1 > /dev/null
    exit $rc 
fi

