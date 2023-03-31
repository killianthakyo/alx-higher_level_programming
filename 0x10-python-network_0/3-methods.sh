#!/bin/bash
#Script to display allowed methods
curl -sI "$1" | grep -i "Allow" | cut -c8-
