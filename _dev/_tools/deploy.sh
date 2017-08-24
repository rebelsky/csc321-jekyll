#!/bin/bash

TARGET=/home/rebelsky/Web/Courses/CSC151/2017S
jekyll build
ssh church.cs.grinnell.edu "mkdir -p $TARGET"
rsync -rtz -e "ssh -p22" _site/ church.cs.grinnell.edu:$TARGET
