IN=$0
STR1=$1
STR2=$2
OUT=$3
sed ':a;N;$!ba;s/.,.,.\n/0,0,0\n/g' $IN > $OUT 