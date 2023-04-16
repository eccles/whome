#!/usr/bin/env just --justfile
#
venvdir := "./venv"
#
# show current available options
default:
	@just --list

# create virtualenv
venv:
	#!/usr/bin/env bash
	rm -rf {{venvdir}}
	python3 -m venv {{venvdir}}
	. {{venvdir}}/bin/activate
	python3 -m pip install --force-reinstall -r requirements.txt
	deactivate

