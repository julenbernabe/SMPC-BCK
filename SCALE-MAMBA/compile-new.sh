#!/bin/bash

# This is the main compilation command for the new compilation
# pipeline

# Portably find the directory containing this script.
HERE=$(cd `dirname $0`; pwd)
# Assuming it lives in root directory of the project,
# set ROOT to the root directory of the project.
ROOT=$HERE

# Now set the PYTHONPATH so we don't have to worry about the CWD
# whenever we invoke python scripts.
export PYTHONPATH=$ROOT:$PYTHONPATH

shift $[OPTIND-1]

ARGS=("$@")
# Get first argument
target=${ARGS[0]}
echo $target
prime=${ARGS[-1]}
echo $prime
# Drop it from the array
unset ARGS[${#ARGS[@]}-1]
unset ARGS[${#ARGS[@]}-1]

rm $target/*.asm
rm $target/*.bc
rm $target/*.sch
printf "Running \n\t ./compile-mamba.py -A -n -r -M -D -u -s %s %s\n\n" $target $prime
./compile-mamba.py -A -n -r -M -D -u -s $target $prime  || exit 1
printf "\nNow running \n\t./scasm %s\n\n" $target
#./scasm --verbose $1 -- --optimizations start_stop_open nop_removal || exit 1
#./scasm --verbose $1 -- --optimizations nop_removal || exit 1
#./scasm --verbose $1 -- --optimizations start_stop_open || exit 1
#./scasm --verbose $1 -- --optimizations register_coloring || exit 1
#./scasm --verbose $1 -- --optimizations nop_removal register_coloring || exit 1
#./scasm --verbose $1 -- --dump-optimizations=temp || exit 1
./scasm --verbose $target -- --hide-warnings "${ARGS[@]}" || exit 1
printf "\n\n"
