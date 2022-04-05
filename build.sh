#!/bin/bash

./scripts/sass.py
hugo
find public -name "*.scss" | xargs rm
