# TVMfuzz

## introduction

TVMfuzz is a demo project for fuzzing TVM, a widely-used Deep Learning Compiler, based on the findings in **A Comprehensive Study of Deep Learning Compiler Bugs**. TVMfuzz is capable of analyzing the interrelationship among statements and building test programs given the existing test files in TVM.

This project involves only 3 folders and 1 script.

+ buggyFile: includes 8 bug-triggered programs found by TVMfuzz
+ tests: includes 53 effective test files in TVM for analysis
+ TVMfuzz: includes all the implementation of major features and functions of TVMfuzz
+ run.py: the script for building test programs

After running *run.py*, a new folder named *byproduct* will be created and it contains 3 extra files:

+ asTree.txt: illustrates the AST of test files with the help of Python package *ast*
+ log.txt: records the interrelationship among all involved statements of interest
+ program.py: the generated test program

## dependency and version

TVMfuzz requires Python package ast, astunparse and numpy, also need to install tvm according the instruction [here](https://tvm.apache.org/docs/install/from_source.html) before executing.

By the way, Python version 3.9.1 is required for successful execution.