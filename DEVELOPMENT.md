# whome

Miscellaneous notes

# Initialisation

This repo requires docker, python3 and the 'just' command as dependencies.
Additionally all changes are generated in a docker image which has to be built.

Ensure that the local bin directory exists and is added to the path:

```bash
ls -l ~/bin   # should not error
echo $PATH    # should contain ~/bin
```

## python3

```bash
python3 --version
```

should return the version of python3 installed.

## docker

Install docker locally by following one of these links:

```bash
./scripts/install-docker.sh
```

## just

If using asdf just type 

```bash
asdf install
```

Otherwise refer to

https://github.com/casey/just

which can be installed by executing:

```bash
export BIN="~/bin"
curl --proto '=https' --tlsv1.2 -sSf https://just.systems/install.sh | bash -s -- --to ${BIN}
```

and then checking that 'just' is available:

```bash
which just     # should return a patyh to tyhe just executable.
just --help    # should return the help message
just           # will return the output of the first entry in the justfile
```

## create the builder image

Create the docker image and test that one can shell into the build environment:

```bash
just builder
just shell
```

# Development

After creating the build environment one can edit the files.

To generate the html output:


```bash
just doc
```

