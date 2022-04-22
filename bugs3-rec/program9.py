from tvm import relay as rly
from tvm.relay.testing.synthetic import get_workload
from tvm.relay import transform
from tvm.relay.scope_builder import ScopeBuilder
from tvm.contrib.nvcc import have_fp16
from tvm.relay.transform import un_cps
from tvm import autotvm
from tvm.relay import TypeMutator
from tvm.relay.op.annotation import compiler_end
from tvm.relay.testing.temp_op_attr import TempOpAttr
import tvm.relay.transform as _transform
from tvm.relay import analysis
from tvm.contrib import graph_runtime
from tvm.autotvm.tuner import RandomTuner
from tvm.relay.ty import TypeCall
import scipy.sparse as sp
from tvm import runtime
from tvm.relay import TypeVisitor
import numpy as np
import json
import itertools
from tvm.relay import ExprVisitor
from tvm.runtime import container
from tvm.relay import TypeFunctor
from tvm.testing import assert_allclose
from tvm.relay.testing import run_infer_type
from tvm.relay import op
from tvm.relay.ty import TypeRelation
from tvm.relay.data_dep_optimization import simplify_fc_transpose
from tvm.relay.ty import FuncType
import tvm.testing
from tvm.ir import IRModule
import scipy
from tvm.relay import expr as _expr
from tvm.relay.testing import create_workload
from tvm.relay.analysis import check_basic_block_normal_form
from tvm.relay.prelude import Prelude
from tvm import topi
from tvm.relay.ty import GlobalTypeVar
from tvm.relay.ty import TensorType
from numpy import isclose
import time
from tvm.relay.analysis import detect_feature
from tvm.relay.testing import run_opt_pass
from tvm.relay.build_module import bind_params_by_name
from tvm.relay import create_executor
from tvm.relay import testing
from tvm.relay.transform import FastMath
from functools import wraps
from tvm.relay.testing import check_grad
from tvm import nd
import logging
import tvm.relay as relay
from tvm.relay.ty import IncompleteType
from typing import Union
import random
from scipy import special
from tvm import te
from tvm.relay.testing import enabled_targets
from tvm.relay.backend.interpreter import RefValue
from tvm.relay.analysis import check_kind
from tvm.relay.analysis import Feature
from tvm.relay import Any
from tvm.relay.ty import TypeVar
from tvm.relay.transform import SimplifyInference
from tvm.relay.testing import make_nat_expr
import math
import tvm.topi.testing
import pytest
from tvm.relay.testing import rand
from tvm import relay
from tvm.relay.testing import count
import os
from tvm.relay.analysis import get_calibration_data
from tvm.relay.op.annotation import compiler_begin
from tvm.relay.testing import Prelude
import sys
import tvm.relay.transform
from tvm.ir import structural_equal
from tvm.relay.analysis import well_formed
from tvm.relay.backend.interpreter import ConstructorValue
from tvm.relay.ty import RefType
from tvm.relay.ty import TupleType
from tvm.relay.adt import TypeData
from tvm.relay.transform import to_cps
import tvm.relay.testing
import tvm

KrZe3=relay.vm.VMCompiler()
t4N3X=tvm.IRModule()
IdfL8=relay.GlobalTypeVar('''gtv''')
OCNEu=relay.TypeVar('''tv''')
CMwMH=relay.Constructor('''Right''',[OCNEu,],IdfL8)
TQTax=relay.TypeData(IdfL8,[OCNEu,OCNEu,],[CMwMH,CMwMH,])
t4N3X[IdfL8]=TQTax
t4N3X[IdfL8]=TQTax
t4N3X[IdfL8]=TQTax
nQ7o5=relay.TypeData(IdfL8,[OCNEu,OCNEu,],[CMwMH,CMwMH,])
t4N3X[IdfL8]=nQ7o5
AyVnf=KrZe3.optimize(t4N3X,target='''llvm''')
