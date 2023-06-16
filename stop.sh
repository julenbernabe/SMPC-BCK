#!/bin/bash
clear
echo "###############################"
echo ""
echo "      STOP MARKETPLACE"
echo ""
echo "###############################"
echo ""
echo ""
echo "Removing all previous repositories:"
echo ""

docker-compose -f docker-compose-bck.yml down
docker-compose -f docker-compose-client.yml down