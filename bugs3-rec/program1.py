from tvm.relay import ExprVisitor
from numpy import isclose
import os
from tvm.relay.transform import un_cps
from tvm.ir import structural_equal
from tvm.relay.analysis import detect_feature
from tvm.relay import op
from tvm.relay.testing import run_infer_type
from typing import Union
from tvm.relay.analysis import get_calibration_data
from tvm.runtime import container
from tvm.relay.backend.interpreter import RefValue
from tvm.relay.ty import TupleType
from tvm import relay
from tvm import relay as rly
from tvm.contrib import graph_runtime
from tvm.relay.ty import RefType
import tvm
from tvm import topi
from tvm.relay.analysis import well_formed
from tvm.relay.analysis import check_basic_block_normal_form
import math
from tvm.relay.adt import TypeData
from tvm.relay.analysis import Feature
from tvm.relay import expr as _expr
from tvm.testing import assert_allclose
from tvm.relay import transform
from tvm.relay.ty import TensorType
from tvm.relay.testing import make_nat_expr
from tvm.relay import analysis
from tvm.relay.ty import GlobalTypeVar
from tvm.relay.testing import rand
from tvm.relay.testing import create_workload
from tvm.relay.testing import Prelude
from tvm.ir import IRModule
from tvm.relay.op.annotation import compiler_begin
import itertools
import pytest
from tvm.relay.backend.interpreter import ConstructorValue
import scipy
from tvm.relay.testing import enabled_targets
from tvm import nd
from tvm.relay.transform import to_cps
import random
from tvm.relay.op.annotation import compiler_end
from tvm.relay.transform import FastMath
from tvm.relay.build_module import bind_params_by_name
from tvm import te
from tvm import autotvm
from tvm.relay import TypeFunctor
import time
from tvm.relay.testing.synthetic import get_workload
from tvm.relay import create_executor
from tvm.relay.transform import SimplifyInference
import logging
from tvm.relay.testing import count
from scipy import special
from tvm.relay.ty import TypeRelation
import tvm.topi.testing
from tvm import runtime
import tvm.relay.testing
from tvm.relay.ty import IncompleteType
from tvm.relay.analysis import check_kind
import tvm.testing
from tvm.relay.testing.temp_op_attr import TempOpAttr
from tvm.relay.scope_builder import ScopeBuilder
import tvm.relay.transform as _transform
import tvm.relay.transform
from tvm.relay.testing import check_grad
import tvm.relay as relay
from functools import wraps
from tvm.relay.data_dep_optimization import simplify_fc_transpose
from tvm.relay import TypeVisitor
import numpy as np
from tvm.relay import TypeMutator
from tvm.relay.ty import TypeVar
import sys
from tvm.relay import Any
import scipy.sparse as sp
from tvm.contrib.nvcc import have_fp16
from tvm.relay.ty import FuncType
from tvm.relay.prelude import Prelude
from tvm.relay.ty import TypeCall
from tvm.autotvm.tuner import RandomTuner
import json
from tvm.relay import testing
from tvm.relay.testing import run_opt_pass

BIpaH=relay.scalar_type('''int64''')
M4Vnw=relay.Var('''x''',BIpaH)
v0Lif=tvm.gpu()
NQxA2=relay.op.memory.alloc_storage(M4Vnw,M4Vnw,v0Lif)
nAvj8=relay.var('''y''',shape=(2,10,))
V1wYy=nAvj8(nAvj8)
Fn9YX=relay.TypeVar('''b''')
vsXRL=relay.Function([nAvj8,nAvj8,],V1wYy,Fn9YX,[Fn9YX,])


def run_infer_type(expr, mod=None):
    if (not mod):
        mod = tvm.IRModule.from_expr(expr)
        mod = transform.InferType()(mod)
        entry = mod['main']
        return (entry if isinstance(expr, relay.Function) else entry.body)
    else:
        if isinstance(expr, relay.GlobalVar):
            gv = expr.name_hint
        else:
            func = expr
            if (not isinstance(expr, relay.Function)):
                func = relay.Function(analysis.free_vars(expr), expr)
            mod['main'] = func
            gv = 'main'
        mod = transform.InferType()(mod)
        if isinstance(expr, (relay.GlobalVar, relay.Function)):
            return mod[gv]
        return mod[gv].body
EK9ON=relay.Function([nAvj8,nAvj8,],(nAvj8 + nAvj8))
uZt2I=tvm.IRModule()
PHgDu=relay.GlobalTypeVar('''Ayy''')
ntFSO=relay.TypeData(PHgDu,[],[])
uZt2I[PHgDu]=ntFSO
uZt2I['''main''']=EK9ON
uZt2I['''main''']=EK9ON
uZt2I['''main''']=EK9ON
Sh3M2=run_infer_type(EK9ON)
