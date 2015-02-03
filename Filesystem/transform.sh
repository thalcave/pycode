cat tmp.txt  | grep . | awk -F "=" '{print $2}' | cut -f 1 -d \> | sort | cut -f 2 -d \" > strlist.txt
