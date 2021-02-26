# Dataset

## Introduction

This dataset is the basic support for the paper: **A Comprehensive Study of Deep Learning Compiler Bugs**. 

We collected the closed and tje merged pull requests that are responsible for fixing bugs from their GitHub repositories over 15 months. In total, we collected 1,361 bug-fixing pull requests and identified 603 bugs, including 318 TVM bugs, 145 Glow bugs, and 140 nGraph bugs.

All the bugs are recorded in the excel table and the bugs of each compiler are displayed in a single worksheet.

## Repositorys

The repositories corresponding to these three compilers are as follows. Since nGraph's support for some frameworks is in a separate repository, we also include this part of the data in the same time period.

TVM ：https://github.com/apache/tvm

Glow: https://github.com/pytorch/glow

nGraph:

https://github.com/NervanaSystems/ngraph、

https://github.com/NervanaSystems/ngraph-tf、(one model loader of nGraph)

https://github.com/NervanaSystems/ngraph-onnx (one model loader of nGraph)

## Information

For each worksheet, the following related information are shown:

+ the name of the compiler
+ pr_id: short for pull request id
+ the title of the pull request(pr)
+ the url directed to this pr
+ the concrete date when this pr was published
+ the number of comments involved
+ the number of files involved and their seperate names
