#!/bin/bash
while IFS="" read -r line || [[ -n "$line" ]]; do
echo "*${line}#" > /dev/pts/3
echo "Frame sent: *${line}#"
done <"$1"


