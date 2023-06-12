#!/usr/bin/bash
for index in {0..10} 
do
	filename="${index}-main.js"
	touch "$filename"
	chmod +x "$filename"
	echo "#!/usr/bin/node" >> "$filename"
	echo "import sys" >> "$filename"
	echo "sys.path.append('../')" >> "$filename"
done
