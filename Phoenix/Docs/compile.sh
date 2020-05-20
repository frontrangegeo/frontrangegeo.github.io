#! /usr/bin/env bash

for var in "$@"
do
    input="$var"
    replace="html"
    rb=""
    pandoc --quiet --mathjax -c Resources/github.css -s --title-prefix="${input}" "$input" -o "${input/md/$replace}"
    echo "Created ${input/md/$replace} from ${input}"
done
