#!/bin/bash
###########################################################
# Script Name: clock_angle_calc.sh                        #
# Description: This script will calculate angle           #
#              between Hour and minute hand of a clock.   #
# Developed By: Neha Bondade                              #
###########################################################

hour=cat /srcfile/time.txt | cut -d " " -f1
min=cat /srcfile/time.txt | cut -d " " -f1

if [ $hour == 12 ]
	then export hour=0;
elif [ $min == 60 ]
	then 
		export min=0;
		export hour=$hour+1;
elif [ $hour > 12 ]
	then
		export hour_angle=`expr 0.5 \* (`expr $hour \*60 + $min`)`
		export min_angle=`expr 6 \* $min`;
		export angle=`expr $hour_angle - $min_angle`
		echo "Angle Difference: $angle"
end if
