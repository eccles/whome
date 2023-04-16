# whome

CV in reStructured text

# Initialisation

This repo requires python3 and the 'just' command.

Ensure that the local bin directory exisats and is added to the path:

```bash
ls -l ~/bin   # should not error
echo $PATH    # should contain ~/bin
```

## python3

```bash
python3 --version
```

should return the version of python3 installed.

## just

https://github.com/casey/just

which can be installed by executimng:

```bash
export BIN="~/bin"
curl --proto '=https' --tlsv1.2 -sSf https://just.systems/install.sh | bash -s -- --to ${BIN}
```

and then checking that just is available:

```bash
which just     # should return ~/bin/just
just --help    # should return the help message
just           # will return the output of the first entry in the justfile
```



