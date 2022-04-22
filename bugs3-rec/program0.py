from tvm import autotvm
from tvm.relay.testing import create_workload
from tvm.relay.analysis import check_kind
from tvm.relay.analysis import Feature
from tvm.relay import expr as _expr
from tvm.relay.op.annotation import compiler_begin
from tvm.relay.scope_builder import ScopeBuilder
from tvm.relay.testing import count
from tvm.relay.backend.interpreter import ConstructorValue
from tvm.contrib.nvcc import have_fp16
from tvm.relay import create_executor
import scipy.sparse as sp
from tvm.relay.analysis import get_calibration_data
from tvm.relay.data_dep_optimization import simplify_fc_transpose
from typing import Union
from tvm.relay import ExprVisitor
import tvm.topi.testing
from tvm.relay import TypeMutator
from tvm.relay.ty import TypeVar
import tvm.relay.transform as _transform
from tvm.relay.ty import TensorType
from tvm.ir import IRModule
from scipy import special
from tvm.relay.analysis import detect_feature
import numpy as np
import logging
from tvm import te
from tvm.relay.op.annotation import compiler_end
from tvm.relay.analysis import check_basic_block_normal_form
import time
from tvm import relay as rly
from tvm.relay import Any
from tvm.relay.prelude import Prelude
from tvm.relay.transform import FastMath
from tvm import nd
from tvm.relay.ty import TupleType
from tvm import relay
from tvm import runtime
from tvm.relay.ty import IncompleteType
from tvm.relay.ty import GlobalTypeVar
from tvm.relay.testing import run_opt_pass
import math
from tvm.ir import structural_equal
from functools import wraps
from tvm.relay import op
import itertools
import random
from tvm.relay.ty import FuncType
from tvm.relay.transform import to_cps
import scipy
from tvm.relay.ty import TypeRelation
import tvm
from tvm import topi
import pytest
from tvm.relay.testing import make_nat_expr
from tvm.testing import assert_allclose
import sys
import tvm.relay.transform
from tvm.relay.testing import Prelude
from numpy import isclose
from tvm.relay.build_module import bind_params_by_name
import tvm.testing
from tvm.relay import TypeVisitor
from tvm.runtime import container
from tvm.relay.backend.interpreter import RefValue
from tvm.relay.analysis import well_formed
from tvm.relay.testing.synthetic import get_workload
import tvm.relay as relay
from tvm.relay.ty import RefType
from tvm.relay.testing import run_infer_type
import json
from tvm.relay.ty import TypeCall
from tvm.relay import TypeFunctor
from tvm.relay.transform import un_cps
from tvm.autotvm.tuner import RandomTuner
import tvm.relay.testing
from tvm.contrib import graph_runtime
from tvm.relay.testing.temp_op_attr import TempOpAttr
from tvm.relay import analysis
from tvm.relay.adt import TypeData
from tvm.relay.testing import rand
import os
from tvm.relay.testing import check_grad
from tvm.relay.testing import enabled_targets
from tvm.relay.transform import SimplifyInference
from tvm.relay import transform
from tvm.relay import testing

m5465=rand('''float16''',*(10,7,))
FfIgy=m5465.asnumpy()


def has_func_type(t):

    class FuncTypeVisitor(TypeVisitor):

        def __init__(self):
            super().__init__()
            self.has_func = False

        def visit_func_type(self, ftt):
            self.has_func = True
    ftvisitor = FuncTypeVisitor()
    ftvisitor.visit(t)
    return ftvisitor.has_func


def assert_no_higher_order_functions(expr, mod):

    class CheckFirstOrderVisitor(ExprVisitor):

        def __init__(self, mod):
            super().__init__()
            self.mod = mod
            self.hof = []
            self.visited_gv = set()

        def visit_call(self, call):
            is_higher_order = False
            if has_func_type(call.checked_type):
                is_higher_order = True
            for a in call.args:
                if has_func_type(a.checked_type):
                    is_higher_order = True
            if is_higher_order:
                self.hof.append(call)
            super().visit_call(call)

        def visit_global_var(self, gv):
            if (gv not in self.visited_gv):
                self.visited_gv.add(gv)
                self.visit(self.mod[gv])
    mod = transform.InferType()(mod)
    check_fo_visitor = CheckFirstOrderVisitor(mod)
    check_fo_visitor.visit(expr)
    nl = '\n--------\n'
    errmsg = f'''found {len(check_fo_visitor.hof)} higher order functions:
  {nl.join((expr.astext() for expr in check_fo_visitor.hof))}'''
    assert (len(check_fo_visitor.hof) == 0), errmsg


def defunctionalized(mod):
    mod = transform.InferType()(mod)
    mod['main'] = transform.Defunctionalization(mod['main'], mod)
    mod = transform.InferType()(mod)
    assert_no_higher_order_functions(mod['main'], mod)
    return mod
m1KrO=tvm.parser.fromtext('''
#[version = "0.0.5"]
def @id[A](%x: A) -> A {
  %x
}
def @main(%f: float32) -> float32 {
  @id(%f)
}
''')
jL1dK=defunctionalized(m1KrO)
FUUbA=relay.create_executor('''debug''',mod=jL1dK)
q6O0b=FUUbA.evaluate(m1KrO['''main'''])
ZAp8z=q6O0b(m5465)
BWjOZ=ZAp8z.asnumpy()
assert_allclose(BWjOZ,(FfIgy + FfIgy))
