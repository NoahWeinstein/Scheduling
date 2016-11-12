#!/bin/sh
echo 'Experiment 1 has 10 time slots, 12 rooms,  100 classes, and 1000 students'
./make_random_input.pl 12 100 10 1000 constraints_1.txt prefs_1.txt
time python make_schedule.py constraints_1.txt prefs_1.txt schedule_1.txt
./is_valid.pl constraints_1.txt prefs_1.txt schedule_1.txt
echo ' out of 4000 \n'

rm constraints_1.txt
rm prefs_1.txt
rm schedule_1.txt

echo 'Experiment 2 has 10 time slots, 100 rooms,  1000 classes, and 15000 students'
./make_random_input.pl 100 1000 10 15000 constraints_2.txt prefs_2.txt
time python make_schedule.py constraints_2.txt prefs_2.txt schedule_2.txt
./is_valid.pl constraints_2.txt prefs_2.txt schedule_2.txt
echo ' out of 60000 \n'

rm constraints_2.txt
rm prefs_2.txt
rm schedule_2.txt

echo 'Experiment 3 has 10 time slots, 100 rooms,  1000 classes, and 25000 students'
./make_random_input.pl 100 1000 10 25000 constraints_3.txt prefs_3.txt
time python make_schedule.py constraints_3.txt prefs_3.txt schedule_3.txt
./is_valid.pl constraints_3.txt prefs_3.txt schedule_3.txt
echo ' out of 100000 \n'

rm constraints_3.txt
rm prefs_3.txt
rm schedule_3.txt

echo 'Experiment 4 has 10 time slots, 200 rooms,  2000 classes, and 15000 students'
./make_random_input.pl 200 2000 10 15000 constraints_4.txt prefs_4.txt
time python make_schedule.py constraints_4.txt prefs_4.txt schedule_4.txt
./is_valid.pl constraints_4.txt prefs_4.txt schedule_4.txt
echo ' out of 60000 \n'

rm constraints_4.txt
rm prefs_4.txt
rm schedule_4.txt



