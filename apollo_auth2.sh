#!/bin/bash

SCRIPT_PATH="apolloSearchCompanyByDomain.py"

while true
do
    source "venv/bin/activate"
    python "$SCRIPT_PATH"
    echo "Sleep 2m"
    sleep 120
done

