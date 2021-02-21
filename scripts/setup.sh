#!/bin/bash

BLUE='\033[0;34m'
NC='\033[0m'
GREEN='\033[0;32m'

echo -e "
${BLUE}Setting the script directory in system path${NC} ..."

echo $PATH > prev_SysPATH.txt


prsnt=`pwd`

echo $prsnt

sudo echo "export PATH="$PATH:$prsnt"" >> ~/.bashrc

chmod 744 insecure_shell.py ssh_brute-*
