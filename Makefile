# We don't need a default
default:

# Create a branch for the generic courses repository (somewhat upstream)
.PHONY: generic
generic:
	@if [ ! `git remote | grep '^generic$$'` ]; then \
	  git remote add generic https://github.com/rebelsky/generic-course/jekyll; \
	fi

# Pull from the generic course
pull-generic: generic
	git pull generic master

