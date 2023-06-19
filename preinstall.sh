#!/bin/bash
clear
echo "###############################"
echo ""
echo "      PRECONFIGURATION"
echo ""
echo "###############################"
echo ""
echo ""
echo "Building Marketplace Client Docker image"
echo ""

cd client
docker build -t client:scientist --target scientist .
docker build -t client:owner --target owner .
cd ..