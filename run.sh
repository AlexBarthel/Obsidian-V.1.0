clear -x
var=`date`
branch=$(git symbolic-ref HEAD | sed -e 's,.*/\(.*\),\1,')
echo "$branch ($var)\n"

python3 main.py