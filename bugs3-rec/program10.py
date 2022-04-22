from tvm.relay.ty import FuncType
from tvm.relay.testing import create_workload
from tvm.relay import ExprVisitor
from tvm.contrib import graph_runtime
from tvm.relay import transform
import logging
import sys
from tvm import relay
import os
from tvm.relay.ty import TypeRelation
import numpy as np
from tvm.relay.ty import IncompleteType
import tvm.topi.testing
from tvm.relay import TypeMutator
from tvm.relay.data_dep_optimization import simplify_fc_transpose
from tvm.relay.backend.interpreter import ConstructorValue
from tvm.relay.ty import RefType
from tvm.relay import create_executor
from tvm.relay.testing import check_grad
from tvm.relay.analysis import get_calibration_data
from tvm import nd
from tvm.relay import Any
from tvm.relay.testing import run_opt_pass
from tvm.relay.adt import TypeData
from numpy import isclose
from tvm.ir import IRModule
from tvm.relay.testing import enabled_targets
from tvm.relay.ty import TupleType
from tvm import autotvm
from tvm.ir import structural_equal
from tvm.relay.prelude import Prelude
from tvm.relay.ty import TensorType
import tvm
from tvm.relay import TypeFunctor
from tvm.relay import op
from tvm.relay.analysis import check_basic_block_normal_form
from typing import Union
from tvm.relay.scope_builder import ScopeBuilder
from tvm.relay.ty import GlobalTypeVar
import scipy.sparse as sp
from tvm.relay.testing import run_infer_type
import tvm.relay as relay
import time
from tvm.relay.ty import TypeVar
from tvm.relay.testing import make_nat_expr
import tvm.testing
from tvm.runtime import container
import random
from tvm.testing import assert_allclose
from tvm.relay.transform import un_cps
from tvm.contrib.nvcc import have_fp16
import tvm.relay.transform
from tvm.relay.testing.temp_op_attr import TempOpAttr
from tvm.relay.testing import count
from tvm.relay import analysis
import itertools
from tvm.autotvm.tuner import RandomTuner
from tvm.relay import testing
from tvm.relay.build_module import bind_params_by_name
import pytest
from tvm.relay.testing.synthetic import get_workload
import tvm.relay.testing
from tvm.relay.testing import Prelude
from tvm import te
from tvm.relay.backend.interpreter import RefValue
from tvm.relay import TypeVisitor
from tvm import runtime
from tvm import topi
from tvm.relay import expr as _expr
import tvm.relay.transform as _transform
from scipy import special
from tvm.relay.analysis import Feature
from tvm.relay.ty import TypeCall
from tvm import relay as rly
import scipy
from tvm.relay.op.annotation import compiler_end
from tvm.relay.analysis import well_formed
from tvm.relay.transform import to_cps
from tvm.relay.op.annotation import compiler_begin
from tvm.relay.testing import rand
import math
from tvm.relay.transform import FastMath
from functools import wraps
from tvm.relay.analysis import detect_feature
import json
from tvm.relay.analysis import check_kind
from tvm.relay.transform import SimplifyInference

RnT85=create_executor('''debug''')
lCWQO=relay.var('''data1''',shape=(2,3,))
B4olY=relay.Function([lCWQO,],lCWQO)
ve4nt=tvm.IRModule()
umll8=relay.GlobalVar('''f''')
ve4nt[umll8]=B4olY
ve4nt['''main''']=B4olY
OK3Zv=RnT85.evaluate(ve4nt['''main'''])
hIfua=rand('''float32''',*(15,11,))
gERor=OK3Zv(hIfua)
gqQek=gERor.asnumpy()
zyHby=hIfua.asnumpy()
assert_allclose(gqQek,(zyHby * zyHby))
