#!/bin/bash
clear
echo "###############################"
echo ""
echo "      STARTING SETUP"
echo ""
echo "###############################"
echo ""
echo ""

echo ""
echo "Removing all previous repositories:"
echo ""

docker-compose down

echo ""
echo "Initializing the necessary repositories:"
echo ""

docker-compose up -d

