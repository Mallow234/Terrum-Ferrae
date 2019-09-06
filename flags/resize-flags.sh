#!/bin/sh
# resizes images in folder named orig to sizes:
# 82x52
# 41x26
# 10x7
# how do use: put this file in folder, put inside this folder a folder called orig, put images in ./orig/, run script
# these filesizes are HOI4 compatible, hence the odd sizing

mkdir -p 82x52 41x26 10x7

for image in ./orig/*
  do
    filename="$(echo $image | cut --delimiter=/ -f 3 -)"
    filename2="$(echo $filename | cut --delimiter=. -f 1 -)"
    echo $filename
    convert ./orig/$filename -scale 82x52^ -gravity SouthWest -extent 82x52 ./82x52/$filename2.tga
    convert ./orig/$filename -scale 41x26^ -gravity SouthWest -extent 41x26 ./41x26/$filename2.tga
    convert ./orig/$filename -scale 10x7^  -gravity SouthWest -extent 10x7  ./10x7/$filename2.tga
  done

#EOF