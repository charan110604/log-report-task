#!/bin/bash

set +e

pytest /tests/test_outputs.py -rA
STATUS=$?

if [ $STATUS -eq 0 ]
then
    echo "1.0" > /app/reward.txt
else
    echo "0.0" > /app/reward.txt
fi

exit 0