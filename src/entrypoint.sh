#!/bin/bash


set -e

mkdir -p /root/.local/share/nucypher
mkdir -p /root/.ethereum/keystore

python ./init.py

exec nucypher ursula run
