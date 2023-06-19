#!/bin/bash
clear
echo "###############################"
echo ""
echo "      START MARKETPLACE"
echo ""
echo "###############################"
echo ""
echo ""
echo "Initializing components:"
echo ""

docker-compose -f docker-compose-bck.yml up -d

echo ""
echo "Creating token contract"
echo ""

cd marketplace
truffle migrate --network ethereum
cd ..

echo ""
echo "Subscribing eventeum to the contract's events:"
echo ""

sleep 10
cd eventeum-consumer
python3 events_poster.py
cd ..

echo ""
echo "Contract addresses"
echo ""

cd marketplace
truffle networks --network ethereum
cd ..

