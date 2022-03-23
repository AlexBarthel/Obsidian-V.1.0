import sys
from os import walk

import Modules, Parser, std, utils
modules = ["Modules", "Parser", "std", "utils"]

C = '\033[31m'
E = '\033[0m'

for module in modules:
	if module in sys.modules:
		filenames = next(walk(module), (None, None, []))[2]
		for file in filenames:
			print(f'[OBS]\tObsidian-V.1.0/{module}/{file} installed')
	else: print(f'{C}{module} failed to install{E}')