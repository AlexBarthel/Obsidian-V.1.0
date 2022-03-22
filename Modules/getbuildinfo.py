print(f'{str(__file__).replace("/", ".")[1:]} imported')
GITVERSION = 0.1;
GITTAG     = 'default';
buildinfo = {
	'build-month': 'Nov',
	'build-day': 12,
	'build-year': 2021,
};


def Obs_GetBuildInfo():
    gitid = _Obs_gitidentifier();
    revision = _Obs_gitversion();
    print(
        f'Obsidian+ {revision} ({gitid} {buildinfo["build-month"]} {buildinfo["build-day"]} {buildinfo["build-year"]})'
    )


def _Obs_gitversion():
	return GITVERSION;


def _Obs_gitidentifier():
	gitid = 'default';
	if (GITTAG != 'default'):
		gitid = GITTAG;
	return gitid;