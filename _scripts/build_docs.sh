#!/bin/bash

(
  cd docs || exit
  rm -r build/
  make html
)
