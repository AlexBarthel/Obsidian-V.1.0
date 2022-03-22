clear -x

today=$(TZ=":US/Eastern" date)
repo=$(basename -s .git `git config --get remote.origin.url`)
branch=$(git rev-parse --abbrev-ref HEAD)
echo "$repo ($branch, $today)"

# When official program is released it will look something like
# python3 obs_updater.py
# python3 obs_installer.py
# python3 obsidian.py
python3 main.py
