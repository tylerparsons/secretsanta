#!/bin/bash

familyFile=families.csv
oldConnFile=oldConns.csv
newConnFile=newConns.csv
allConnFile=allConns.csv

rotate $newConnFile
rotate $allConnFile

python ss.py $familyFile $oldConnFile $newConnFile
rc=$?
if [ $rc -ne 0 ]
then
    echo ss.py $familyFile $oldConnFile $newConnFile failed rc: $rc
    rm $newConnFile $allConnFile
    exit $rc 
fi

cp $newConnFile $allConnFile
cat $oldConnFile >> $allConnFile

