import scipy
from tvm.contrib import graph_runtime
from tvm.autotvm.tuner import RandomTuner
from tvm.ir import structural_equal
from tvm.relay import ExprVisitor
from tvm.relay.backend.interpreter import RefValue
from tvm.relay.ty import TypeRelation
from tvm.relay import transform
from tvm.relay.analysis import well_formed
import os
import random
from tvm.relay.ty import FuncType
import tvm.testing
from scipy import special
from numpy import isclose
from tvm.relay.testing import make_nat_expr
from tvm.relay.analysis import detect_feature
from tvm.relay.ty import TensorType
from tvm.relay.ty import TupleType
from tvm.relay.backend.interpreter import ConstructorValue
from tvm.relay import testing
from typing import Union
from tvm.relay.testing.synthetic import get_workload
import logging
import tvm.relay.transform as _transform
import pytest
from tvm.relay.transform import to_cps
from tvm import runtime
from tvm.relay.testing import run_infer_type
import math
import tvm.relay as relay
import tvm
from tvm.relay.transform import un_cps
import time
from tvm.relay import Any
from tvm.relay.testing import Prelude
from tvm.relay.analysis import check_kind
from tvm.contrib.nvcc import have_fp16
from functools import wraps
from tvm.relay.ty import RefType
from tvm.relay.ty import TypeCall
from tvm import relay as rly
from tvm.relay.analysis import get_calibration_data
import tvm.topi.testing
from tvm.relay import op
from tvm.relay import create_executor
from tvm.relay.prelude import Prelude
import sys
from tvm.testing import assert_allclose
from tvm import relay
from tvm.relay.transform import SimplifyInference
import tvm.relay.transform
from tvm.relay.testing import rand
from tvm.relay.scope_builder import ScopeBuilder
from tvm.relay.ty import GlobalTypeVar
from tvm.relay.op.annotation import compiler_end
from tvm.relay.testing import create_workload
from tvm.relay import analysis
from tvm.relay.testing import run_opt_pass
import json
import scipy.sparse as sp
from tvm import autotvm
from tvm.relay import TypeVisitor
from tvm.relay.analysis import check_basic_block_normal_form
from tvm.relay import expr as _expr
from tvm.relay.op.annotation import compiler_begin
from tvm.relay.build_module import bind_params_by_name
from tvm.relay.data_dep_optimization import simplify_fc_transpose
from tvm.relay.testing import check_grad
from tvm.relay.testing import count
from tvm import nd
import tvm.relay.testing
from tvm.runtime import container
from tvm.relay.testing import enabled_targets
from tvm.relay.ty import TypeVar
from tvm.relay.analysis import Feature
import numpy as np
from tvm.relay.adt import TypeData
from tvm.relay.ty import IncompleteType
import itertools
from tvm.relay import TypeMutator
from tvm.relay.transform import FastMath
from tvm.ir import IRModule
from tvm import topi
from tvm.relay.testing.temp_op_attr import TempOpAttr
from tvm.relay import TypeFunctor
from tvm import te

qbTYN=relay.ty.TensorType((),'''int32''')
ZIYrl=relay.ty.TupleType([qbTYN,qbTYN,])
gF7Ff=relay.var('''x''',type_annotation=ZIYrl)
NqYWQ=relay.expr.TupleGetItem(gF7Ff,0)
HfXmg=relay.var('''x''',shape=(1,4,),dtype='''float16''')
Qyl9U=np.power(2,32)
LgRSE=relay.const(((62 + 64) / (Qyl9U - 1.0)),'''int64''')
xMBTv=relay.qnn.op.mul(lhs=HfXmg,rhs=HfXmg,lhs_scale=LgRSE,lhs_zero_point=LgRSE,rhs_scale=LgRSE,rhs_zero_point=LgRSE,output_scale=LgRSE,output_zero_point=LgRSE)
DoD9e=relay.Function([HfXmg,],xMBTv)
N9woM=relay.GlobalVar('''f''')
bMkSj=tvm.IRModule()
bMkSj[N9woM]=DoD9e


def check_memory_plan(func, check_fn):
    mod = tvm.IRModule().from_expr(func)
    args = []
    for param in func.params:
        param = param.type_annotation
        sh = [int(sh) for sh in param.shape]
        data = np.random.rand(*sh).astype(param.dtype)
        args.append(tvm.nd.array(data))
    ex = relay.create_executor('vm', mod)
    no_plan_result = ex.evaluate(mod['main'])(*args)
    with tvm.transform.PassContext(opt_level=1, disabled_pass=['MemoryPlan']):
        plan_result = ex.evaluate(mod['main'])(*args)
    py_res = check_fn(*[arg.asnumpy() for arg in args])
    np.testing.assert_allclose(no_plan_result.asnumpy(), plan_result.asnumpy())
    np.testing.assert_allclose(plan_result.asnumpy(), py_res)


def check_add_sub(x, y):
    z = (x + x)
    return (z - y)
check_memory_plan(DoD9e,check_add_sub)
Ys7g0=tvm.IRModule.from_expr(DoD9e)
cmebF=relay.qnn.transform.CanonicalizeOps()
IEGRS=cmebF(Ys7g0)
HArWZ=FastMath()
FJRU6=HArWZ(Ys7g0)
MU9i0=cmebF(Ys7g0)
FOp2B=relay.transform.InferType()
Fqnhq=tvm.IRModule({})
hF4ME=FOp2B(Fqnhq)
p6XJ4=tvm.cpu(0)
xHTht=relay.create_executor(mod=hF4ME,ctx=p6XJ4,target='''llvm''')
pC7EY=xHTht.evaluate(MU9i0['''main'''])
zBWPh=np.arange((-6),21,0)
Fra4O=zBWPh.reshape(0,64)
plk2q=Fra4O.astype('''uint32''')
SxTfh=zBWPh.reshape(1,64)
veWGK=SxTfh.astype('''float16''')
VeOeZ=pC7EY(plk2q,veWGK)
CYtZP=VeOeZ.asnumpy()
wB3rZ=np.concatenate((plk2q,veWGK,),axis=0)
np.testing.assert_equal(CYtZP,wB3rZ)
ljoTs=tvm.transform.PassContext(opt_level=3,required_pass=['''FastMath''',])
with ljoTs:
	FUi4d=relay.optimize(Ys7g0,target='''llvm''',params=None)

