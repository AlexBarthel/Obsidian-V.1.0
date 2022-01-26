clear -x

today=$(TZ=":US/Eastern" date)
repo=$(basename -s .git `git config --get remote.origin.url`)
branch=$(git rev-parse --abbrev-ref HEAD)
echo "$repo ($branch, $today)"

python3 main.py
