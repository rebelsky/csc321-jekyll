default: _prelim/*.md */*.md
	_tools/deploy-local.sh

_prelim/prelim%.md: _eboards/eboard%.md
	prelim2 $*
