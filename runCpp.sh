#!/bin/bash

cd $1/cpp

mkdir -p bin

part=${2^^}

make ans$part
