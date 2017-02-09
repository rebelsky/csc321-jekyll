#!/bin/bash

TARGET=..
jekyll build
echo "*** Copying to release directory ***\n";
time rsync -rtz _site/ $TARGET
