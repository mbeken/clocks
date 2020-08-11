############################################################
# Script Name: clock_angle_calc_dag.py                     #
# Description: This script will trigger DAG for calculation#
#              between Hour and minute hand of a clock.    #
# Developed By: Neha Bondade                               #
############################################################

import airflow
from airflow import DAG
from airflow.operators.bash_operator import BashOperator

dag = DAG(clock_angle_calc_dag)

clock_angle_input = BashOperator(
	task_id='clock_angle_input',
	bash command="/scripts/clock_angle_input.sh"
)

clock_angle_calc = BashOperator(
	task_id='clock_angle_calc',
	bash command="/scripts/clock_angle_calc.sh"
)

clock_angle_input >> clock_angle_calc