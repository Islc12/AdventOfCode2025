#!/usr/bin/env bash

dial=50
count=0

while read -r line; do
    dir=${line:0:1}
    dist=${line:1}

    case "$dir" in
        L)
            ((dial -= dist))
            while ((dial < 0)); do
                ((dial += 100))
            done
            ;;
        R)
            ((dial += dist))
            while ((dial > 99)); do
                ((dial -= 100))
            done
            ;;
    esac

    if ((dial == 0)); then
        ((count++))
    fi

done < "day1.txt"

echo $count