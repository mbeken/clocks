#!/bin/bash
###########################################################
# Script Name: clock_angle_input.sh                       #
# Usage:  bash clock_angle_input.sh hour min              #
# Description: This script will take nd will save it to a #
#              text file                                  #
# Developed By: Neha Bondade                              #
###########################################################

echo "Input values are:"

$hour = $0
$min=$1

$hour $min > /srcfile/time.txt

