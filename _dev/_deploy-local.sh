#!/bin/bash

TARGET=..
jekyll build
time rsync -rtz _site/ $TARGET
