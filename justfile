#!/usr/bin/env just --justfile
#
name := "whome"
#
# show current available options
default:
	@just --list --unsorted --justfile {{justfile()}} | grep -v default

# Recreate build environment in docker image
builder pyversion="3.12":
	#!/usr/bin/env bash
	docker image rm -f whome-builder
	docker build \
	       --build-arg VERSION="{{pyversion}}" \
	       --build-arg NAME="{{name}}" \
	       --build-arg UID="$(id -u)" \
	       --no-cache \
	       -f Dockerfile-builder \
	       -t {{name}}-builder .

# shell into build environment
shell:
	./scripts/builder.sh /bin/bash

# clean
clean:
	#!/usr/bin/env bash
	docker image rm -f whome-builder
	git clean -fdX

# create doc
doc:
	./scripts/builder.sh /bin/bash -c "cd doc && make clean && make html"

