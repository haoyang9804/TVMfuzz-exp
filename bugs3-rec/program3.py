from tvm.relay.transform import SimplifyInference
from tvm.relay.testing import run_opt_pass
import scipy.sparse as sp
from tvm.relay.analysis import get_calibration_data
import tvm.relay as relay
import pytest
from tvm.ir import IRModule
from tvm.relay.analysis import check_basic_block_normal_form
from tvm.relay.analysis import Feature
from tvm.relay.analysis import well_formed
from tvm.relay.testing import count
from tvm.relay.ty import TupleType
from tvm.relay.ty import RefType
from tvm import autotvm
from tvm.relay.data_dep_optimization import simplify_fc_transpose
from tvm.relay.ty import TypeRelation
from numpy import isclose
from tvm.autotvm.tuner import RandomTuner
import tvm.topi.testing
from tvm.relay import ExprVisitor
from tvm.relay import op
from tvm import topi
from tvm.relay.scope_builder import ScopeBuilder
from tvm.relay.ty import TypeVar
import tvm.testing
import tvm
from tvm.testing import assert_allclose
from tvm.contrib.nvcc import have_fp16
from tvm.relay.testing import create_workload
from tvm.relay import expr as _expr
import json
from tvm.relay import analysis
from tvm.relay.transform import to_cps
import numpy as np
from tvm.relay.backend.interpreter import RefValue
from tvm.ir import structural_equal
from tvm.relay.ty import GlobalTypeVar
from tvm.relay.prelude import Prelude
from typing import Union
from tvm.relay.op.annotation import compiler_end
import logging
from tvm.relay.ty import FuncType
from tvm.relay import transform
from tvm.relay.transform import FastMath
import scipy
from tvm.relay.testing.temp_op_attr import TempOpAttr
import os
from tvm.relay.testing import enabled_targets
import math
from tvm.relay.testing import rand
import random
from tvm import relay
from tvm.relay.testing import make_nat_expr
from tvm.relay import testing
from functools import wraps
from tvm.relay.testing import Prelude
from tvm import runtime
from tvm.runtime import container
from scipy import special
from tvm.relay.testing.synthetic import get_workload
import tvm.relay.testing
from tvm.relay.testing import run_infer_type
from tvm.relay import create_executor
import time
import sys
from tvm.relay.ty import TensorType
from tvm.relay.transform import un_cps
import itertools
from tvm.relay import TypeVisitor
from tvm.relay.op.annotation import compiler_begin
from tvm import te
from tvm.relay import TypeFunctor
from tvm import relay as rly
from tvm.relay.analysis import detect_feature
import tvm.relay.transform as _transform
from tvm.relay.backend.interpreter import ConstructorValue
from tvm.relay.analysis import check_kind
import tvm.relay.transform
from tvm.contrib import graph_runtime
from tvm.relay.build_module import bind_params_by_name
from tvm.relay.ty import IncompleteType
from tvm.relay.adt import TypeData
from tvm.relay import TypeMutator
from tvm.relay import Any
from tvm.relay.testing import check_grad
from tvm import nd
from tvm.relay.ty import TypeCall

KOWOw=tvm.transform.PassContext(opt_level=0,required_pass=['''FastMath''',])
EfbkN=relay.Var('''uv''')
YYv4D=relay.scalar_type('''float16''')
eLuxz=relay.FuncType([],YYv4D,[],[])
xIMIl=relay.Var('''alignment''',eLuxz)
Ykrai=relay.const(0)
irLBS=relay.RefCreate(Ykrai)
WAmqU=relay.add(EfbkN,EfbkN)
NxyWR=relay.Let(xIMIl,irLBS,WAmqU)
GuIqU=relay.Function([EfbkN,],NxyWR)
qJCZD=relay.GlobalVar('''three_with_ref''')
HFGGf=tvm.IRModule()
HFGGf['''main''']=GuIqU
HFGGf['''main''']=GuIqU
zrika=relay.GlobalTypeVar('''gtv2''')
FznvQ=relay.Constructor('''Nil''',[],zrika)
gwOIx=relay.TypeData(zrika,[],[FznvQ,])
HFGGf[zrika]=gwOIx
HFGGf['''main''']=GuIqU
HFGGf[qJCZD]=GuIqU
HFGGf['''main''']=GuIqU
OjcjB=tvm.IRModule.from_expr(GuIqU)
with KOWOw:
	OPuqp=relay.optimize(OjcjB,target='''llvm''',params=None)

