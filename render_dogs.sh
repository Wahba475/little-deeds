#!/bin/bash
cd /home/claude/work/vid
for L in dog_en dog_ar; do
  PAGE=dog.html python3 -u render.py $L video 2>&1 | grep --line-buffered -v -E "GL Driver|PCFSoft|404"
  cd out/$L && ls shot*.mp4 | sort -V | sed "s/.*/file '&'/" > list.txt && ffmpeg -y -loglevel error -f concat -safe 0 -i list.txt -c copy tmp_s.mp4 && mv tmp_s.mp4 ${L}_silent.mp4 && echo ${L}_CONCAT_OK; cd /home/claude/work/vid
done
