#!/usr/bin/bash
for index in {1..6} 
do
	filename="${index}-main.py"
	touch "$filename"
	chmod +x "$filename"
	echo "#!usr/bin/python3" >> "$filename"
	echo "import sys" >> "$filename"
	echo "sys.path.append('../')" >> "$filename"
done
