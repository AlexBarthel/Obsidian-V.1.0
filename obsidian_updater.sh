# Update Obsidian
echo -n $'[GIT]\t'
git remote update

# Git Versions
UPSTREAM=${1:-'@{u}'}
LOCAL=$(git rev-parse @)
REMOTE=$(git rev-parse "$UPSTREAM")
BASE=$(git merge-base @ "$UPSTREAM")

C='\033[0;33m'
E='\033[0m'

# Updater
if [ $LOCAL = $REMOTE ]; then
    echo $'[GIT]\tYour version of Obsidian is up-to-date'
elif [ $LOCAL = $BASE ]; then
	echo -e -n "${C}"
	read -p $'[GIT]\tA new version of Obsidian is available do you wish to update (y/n)? ' update
	echo -e -n "${E}"
	if [ $update == "y" ]; then
		echo $'[GIT]\tPulling...'
	fi
fi
