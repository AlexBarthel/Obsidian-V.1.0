clear -x
python3 obsidian_installer.py
# clear -x
bash obsidian_updater.sh
clear -x

today=$(TZ=":US/Eastern" date)
repo=$(basename -s .git `git config --get remote.origin.url`)
branch=$(git rev-parse --abbrev-ref HEAD)
echo "$repo ($branch, $today)"

python3 obsidian.py
