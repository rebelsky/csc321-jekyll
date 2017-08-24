#!/bin/bash

TARGET=..
time jekyll build
mkdir -p $TARGET
echo "-------------------------------------------------"
echo "Synching with target directory."
time rsync -rtz _site/ $TARGET
