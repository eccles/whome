#!/bin/bash
#
# Install docker
#
set -euxo pipefail
cd ~/Downloads
mkdir -p docker
cd docker
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh ./get-docker.sh
rm -f ./get-docker.sh
