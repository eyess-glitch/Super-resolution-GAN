#!/bin/sh
FILES="anime_faces"
id=1
for file in $FILES/*; do
	mkdir $FILES"_organized"/$id
	python3 downsample.py $file $FILES"_organized"/$id
	mv $file $FILES"_organized"/$id
	id=$((id +1))
done

