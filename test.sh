#!/bin/bash
rm test1
find -name "*.sh" -exec cat {} \; >> test1

