#!/bin/bash

x=$(python3 m.py)

echo $x

if [ $x == 1 ]
then
echo "Your plant is gonna die -.-"

bash 1.sh

else

echo "Your plant is ok (for now)!"
bash 0.sh

fi 
