# asdf

asdf is a tool to manage local development tools and commands.

https://asdf-vm.com/guide/introduction.html.

## Install

To install asdf execute this script:

```bash
set -euxo pipefail
cd ~/Downloads
NAME=asdf
VERSION=v0.18.0

ARCH=$(uname -m)
case "${ARCH}" in
    x86_64) ARCH="amd64";;
    arm64)  ARCH="arm64";;
    *)      echo "Unknown arch ${ARCH}"
            exit 1
            ;;
esac

OS=$(uname -s)
case "${OS}" in
    Linux)  OS="linux";;
    Darwin) OS="darwin";;
    *)      echo "Unknown OS ${OS}"
            exit 1
            ;;
esac

TARBALL=${NAME}-${VERSION}-${OS}-${ARCH}.tar.gz
URL="https://github.com/asdf-vm/asdf/releases/download"
mkdir -p ${NAME}
cd ${NAME}
curl -OL ${URL}/${VERSION}/${TARBALL}
tar xf ${TARBALL}
cp asdf ~/bin
chmod +x ~/bin/asdf
```

and add the following to the end of ~/bin/.bashrc:

```
export PATH="${ASDF_DATA_DIR:-$HOME/.asdf}/shims:$PATH"
. <($HOME/bin/asdf completion bash)
```

## Usage

### Plugins

Execute the command 'asdf plugin add <name>' to add management of a command to asdf e.g.

```bash
asdf plugin add golang
```

### Commands

To install a version of a plugin - usually 'latest' e.g.

```bash
asdf install golang latest
```

Note that for golang the following must be added to the .bashrc file:

```
. ${ASDF_DATA_DIR:-$HOME/.asdf}/plugins/golang/set-env.bash
```

### Managing installs

To manage a 'suite' of tools use a file '.tool-versions' to specify which tools and which
versions are required. For the $HOME directory:

```
bat 0.25.0
bats 1.12.0
bottom 0.10.2
dust 1.2.0
exa 0.10.1
fd 10.2.0
fzf 0.62.0
golang 1.24.4
just 1.40.0
hyperfine 1.19.0
lazygit 0.52.0
neovim 0.11.2
ripgrep 14.1.1
shellcheck 0.10.0
shfmt 3.11.0
starship 1.23.0
tokei 12.1.2 
zoxide 0.9.8
nodejs 24.2.0
```

and for a git repo that uses golang:

```
golang 1.24.4		
golangci-lint 2.1.6
just 1.40.0
```

### Upgrading a tool

Edit the appropriate .tool-versions file and execute

```bash
asdf install
```
