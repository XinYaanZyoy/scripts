f1=$(cat data/last | sed 's/data\///g; s/\/followers.txt//g')
f2=$(cat data/latest | sed 's/data\///g; s/\/followers.txt//g')
ls data | grep -E -v "last|latest|$f1|$f2" | xargs -I {} rm -rf data/{}