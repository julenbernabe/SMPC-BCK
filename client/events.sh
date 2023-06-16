#!/bin/bash
clear
echo "###############################"
echo ""
echo "      EVENTS SUBSCRIPTION"
echo ""
echo "###############################"
echo ""
echo ""


echo ""
echo "Deleting previous events:"
echo ""

cd eventeum-consumer
python3 events_eraser.py

echo "DONE."
echo ""

echo ""
echo "Subscribing to the contract's events:"
echo ""

python3 events_poster.py
cd ..