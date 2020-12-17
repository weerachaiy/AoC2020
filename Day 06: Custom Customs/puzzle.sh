#
#cat $1 | tr '\n' '=' | sed 's/==/\n/g' | tr -d '=' | \
#awk '{print "echo "$1" | grep -o . | sort |tr -d \"\\n\"| tr -s \"a-z\" | wc -c"}' | \
#bash | paste -s -d+ - | bc

#
cat $1 | tr '\n' '=' | sed 's/==/\n/g' | tr -d '=' | \
awk '{print "echo "$1" | grep -o . | sort |tr -d \"\\n\"| tr -s \"a-z\""}' | \
bash | wc -c

#
#cat $1 | tr '\n' ',' |sed 's/,,/\n/g'> $1.out
#python puzzle.py $1.out
