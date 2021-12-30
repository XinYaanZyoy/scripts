screen_name=XinYaanZyoy
f1=$(cat data/$screen_name/last | sed 's/data\/$screen_name//g; s/\/followers.txt//g')
f2=$(cat data/$screen_name/latest | sed 's/data\/$screen_name//g; s/\/followers.txt//g')
ls data/$screen_name | grep -E -v "last|latest|$f1|$f2" | xargs -I {} rm -rf data/$screen_name/{}

screen_name=MonadicBrahman
f1=$(cat data/$screen_name/last | sed 's/data\/$screen_name//g; s/\/followers.txt//g')
f2=$(cat data/$screen_name/latest | sed 's/data\/$screen_name//g; s/\/followers.txt//g')
ls data/$screen_name | grep -E -v "last|latest|$f1|$f2" | xargs -I {} rm -rf data/$screen_name/{}