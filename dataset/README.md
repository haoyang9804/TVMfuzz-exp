# Dataset

## introduction

This dataset is the basic support for the paper: **A Comprehensive Study of Deep Learning Compiler Bugs**. 

we collected closed and merged pull requests that are responsible to fix bugs from their GitHub repositories over 15 months. In total, we collected 1,361 bug-fixing pull requests and identified 603 bugs, including 318 TVM bugs, 145 Glow bugs, and 140 nGraph bugs.

All the bugs are included in the excel table and each project was included in a single worksheet.

## repositorys

The warehouses corresponding to these three projects are as follows. Since ngraph's support for some  frameworks is in a separate warehouse, we also include this part of the data in the same time period.

TVM ：https://github.com/apache/tvm

Glow: https://github.com/pytorch/glow

nGraph:

https://github.com/NervanaSystems/ngraph、

https://github.com/NervanaSystems/ngraph-tf、(one model loader of nGraph)

https://github.com/NervanaSystems/ngraph-onnx (one model loader of nGraph)



See the paper for details.

