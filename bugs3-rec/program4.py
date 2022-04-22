from tvm.relay.ty import RefType
from tvm.contrib import graph_runtime
from numpy import isclose
from tvm.relay.testing import Prelude
from tvm import relay as rly
from tvm.relay.ty import TypeVar
from tvm.relay.testing import enabled_targets
import tvm.topi.testing
from tvm.relay.build_module import bind_params_by_name
import itertools
from tvm.relay import op
import tvm.relay.testing
from tvm import autotvm
from tvm.runtime import container
import json
from tvm.relay.analysis import detect_feature
import logging
from tvm.relay import TypeMutator
from tvm.relay.data_dep_optimization import simplify_fc_transpose
from tvm.relay.ty import GlobalTypeVar
import tvm.relay.transform
from tvm.contrib.nvcc import have_fp16
from tvm.relay.backend.interpreter import RefValue
from tvm import topi
from tvm.ir import structural_equal
from tvm.relay import TypeVisitor
from tvm.relay import testing
from tvm.relay.analysis import Feature
from tvm.relay import analysis
import numpy as np
from tvm.relay import create_executor
from tvm import runtime
from tvm.relay.analysis import check_basic_block_normal_form
from tvm.relay.ty import FuncType
from tvm.relay.prelude import Prelude
from tvm.relay.testing import make_nat_expr
from tvm.relay.op.annotation import compiler_end
from tvm.relay.backend.interpreter import ConstructorValue
from tvm import relay
from tvm.relay.testing.synthetic import get_workload
from tvm import nd
from tvm.relay.op.annotation import compiler_begin
from tvm.relay.ty import TensorType
import tvm.testing
from tvm.relay import transform
from tvm.relay.ty import TypeCall
from tvm.relay import Any
from tvm.relay.testing import run_opt_pass
from tvm.relay.transform import un_cps
import tvm.relay as relay
from tvm.relay.ty import IncompleteType
from tvm.autotvm.tuner import RandomTuner
from tvm.relay.testing import create_workload
from scipy import special
import math
from tvm.relay.testing import rand
from tvm.relay.ty import TypeRelation
from tvm.relay.transform import SimplifyInference
from functools import wraps
from tvm.relay.testing import run_infer_type
from tvm.relay.transform import to_cps
from tvm.relay import TypeFunctor
from tvm.relay.testing import check_grad
import tvm.relay.transform as _transform
from tvm.relay import ExprVisitor
from tvm.relay.testing.temp_op_attr import TempOpAttr
import os
from tvm.relay import expr as _expr
from tvm.relay.ty import TupleType
import random
from tvm import te
import time
from tvm.relay.analysis import check_kind
import pytest
from typing import Union
from tvm.relay.scope_builder import ScopeBuilder
import sys
import tvm
from tvm.relay.analysis import well_formed
from tvm.relay.analysis import get_calibration_data
from tvm.relay.adt import TypeData
from tvm.relay.testing import count
from tvm.ir import IRModule
from tvm.relay.transform import FastMath
import scipy.sparse as sp
import scipy
from tvm.testing import assert_allclose

f1tqd=relay.var('''s''',shape=(0,10,16,14,),dtype='''float64''')
wMiHW=relay.const(0,dtype='''uint16''')
uHowh=relay.add(f1tqd,wMiHW)
wQvwH=relay.Function([f1tqd,],uHowh)
gAX7p=tvm.IRModule()
gAX7p['''main''']=wQvwH
gAX7p['''main''']=wQvwH
hBXVc=tvm.IRModule.from_expr(wQvwH)
X7KcI=tvm.transform.PassContext(opt_level=3,required_pass=['''FastMath''',])
with X7KcI:
	FOssk=relay.optimize(hBXVc,target='''llvm''',params=None)

CqDn1=FastMath()
snVi9=CqDn1(hBXVc)


def run_opt_pass(expr, opt_pass):
    mod = tvm.IRModule.from_expr(expr)
    mod = opt_pass(mod)
    entry = mod['main']
    return (entry if isinstance(expr, relay.Function) else entry.body)
RZuZc=relay.Var('''z''')
qB5Xt=tvm.nd.array(10)
TH408=relay.Constant(qB5Xt)
VtyVM=relay.Let(RZuZc,TH408,RZuZc)
LwqQw=transform.ToANormalForm()
ZO9bf=run_opt_pass(VtyVM,LwqQw)
check_basic_block_normal_form(ZO9bf)
NhCSP=transform.LazyGradientInit()
fQX0m=NhCSP(gAX7p)
hAuGZ=create_executor(mod=fQX0m)
gAX7p['''main''']=wQvwH
UuCFE=hAuGZ.evaluate(gAX7p['''main'''])
joMsg=rand('''uint16''',*(4,4,))
Fhplj=UuCFE(joMsg)
eabkU=Fhplj.asnumpy()
UoWjX=joMsg.asnumpy()
assert_allclose(eabkU,UoWjX)
kWGxm=relay.multiply(uHowh,wMiHW)
WkKZU=relay.TypeVar('''b''')
x7mWX=relay.TupleType([WkKZU,WkKZU,])
PMIKb=relay.Var('''f''',x7mWX)
ZfvrP=PMIKb()
QE731=relay.If(ZfvrP,kWGxm,kWGxm)
