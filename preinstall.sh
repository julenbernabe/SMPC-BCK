#!/bin/bash
clear
echo "###############################"
echo ""
echo "      PRECONFIGURATION"
echo ""
echo "###############################"
echo ""
echo ""
echo "Building MPC Agent Docker image"
echo ""

cd client
docker build -t agent .
cd ..