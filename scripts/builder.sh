#!/bin/bash
#
# Executes a command inside the builder container
#
# Usage Examples
#
#     ./scripts/builder.sh /bin/bash   # for shell
#     ./scripts/builder.sh             # enters python REPL

if [ "$USER" = "builder" -o "$USER" = "vscode" ]
then
    "$@"
    exit 0
fi

if [ -t 1 ]
then
    USE_TTY="-it"
fi
NAME=${NAME:-whome}
docker run \
    --rm ${USE_TTY} \
    -v $(pwd):/home/builder/${NAME} \
    -u $(id -u):$(id -g) \
    -e GITHUB_REF \
    ${NAME}-builder \
    "$@"
