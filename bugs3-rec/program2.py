from tvm.relay.analysis import check_kind
from tvm.ir import structural_equal
from tvm.relay.op.annotation import compiler_begin
from tvm.relay.testing import run_infer_type
import tvm.relay.testing
import itertools
import time
from tvm import runtime
from tvm.relay.testing import rand
import scipy.sparse as sp
from tvm.testing import assert_allclose
from tvm import te
import sys
from tvm.relay.ty import TypeCall
from tvm.relay.ty import IncompleteType
from tvm.relay import testing
from tvm.relay.testing import enabled_targets
from tvm.relay.testing.synthetic import get_workload
from tvm.relay.testing.temp_op_attr import TempOpAttr
from tvm.relay.analysis import check_basic_block_normal_form
from tvm.relay.scope_builder import ScopeBuilder
from tvm.relay.ty import FuncType
import tvm.testing
import scipy
from tvm.relay import ExprVisitor
import numpy as np
from tvm import relay
from tvm.relay.analysis import detect_feature
from tvm import relay as rly
from tvm.relay.testing import create_workload
from tvm.relay import expr as _expr
from tvm.relay import TypeMutator
from tvm.contrib.nvcc import have_fp16
from typing import Union
from tvm.relay.testing import check_grad
from tvm.relay.backend.interpreter import RefValue
from tvm.relay.testing import count
from tvm.relay.testing import make_nat_expr
from tvm.relay.ty import TypeVar
from tvm.relay import TypeFunctor
from tvm.relay import Any
from tvm.relay.backend.interpreter import ConstructorValue
import tvm.relay.transform
from tvm.relay import op
from tvm.relay.adt import TypeData
import os
from tvm.contrib import graph_runtime
from tvm.relay.transform import FastMath
from tvm.relay.data_dep_optimization import simplify_fc_transpose
from tvm.relay.transform import un_cps
from tvm.ir import IRModule
from functools import wraps
from tvm import autotvm
import random
from tvm.relay.transform import SimplifyInference
from tvm.relay import create_executor
from tvm.relay.ty import TensorType
import math
import tvm.relay as relay
from tvm.relay.analysis import Feature
from tvm.relay.op.annotation import compiler_end
import tvm.relay.transform as _transform
import pytest
from tvm.relay.prelude import Prelude
from tvm.relay.ty import GlobalTypeVar
from tvm.relay import analysis
import tvm.topi.testing
from tvm.relay.ty import TypeRelation
import tvm
from tvm.relay.analysis import well_formed
from tvm import topi
from tvm import nd
import logging
import json
from tvm.relay.testing import run_opt_pass
from tvm.runtime import container
from tvm.relay import TypeVisitor
from tvm.relay.ty import RefType
from tvm.relay import transform
from tvm.relay.transform import to_cps
from tvm.relay.testing import Prelude
from numpy import isclose
from tvm.autotvm.tuner import RandomTuner
from tvm.relay.ty import TupleType
from scipy import special
from tvm.relay.build_module import bind_params_by_name
from tvm.relay.analysis import get_calibration_data

LnPCZ=np.array([(-63.5),(-20),(-62.5),(-62),(-41.4),30,30,23.4,31.40,15,])
WRSvd=LnPCZ.astype('''uint64''')
CGBXS=WRSvd.reshape((2,5,))


def quantize_test_driver(in_dtype, quant_args, axis, out_dtype, in_data, verify_output_data):
    shape = in_data.shape
    input_data = relay.var('input_data', shape=shape, dtype=in_dtype)
    output_zero_point = relay.const(quant_args['out_zero_point'])
    output_scale = relay.const(quant_args['out_scale'])
    quantized_output = relay.qnn.op.quantize(input_data, output_scale=output_scale, output_zero_point=output_zero_point, axis=axis, out_dtype=out_dtype)
    mod = relay.Function(relay.analysis.free_vars(quantized_output), quantized_output)
    mod = tvm.IRModule.from_expr(mod)
    with tvm.transform.PassContext(opt_level=3):
        (graph, lib, params) = relay.build(mod, 'llvm', params=None)
        rt_mod = graph_runtime.create(graph, lib, ctx=tvm.cpu(0))
        rt_mod.set_input(input_data=in_data)
        rt_mod.set_input(**params)
        rt_mod.run()
        res = rt_mod.get_output(0).asnumpy()
        np.testing.assert_equal(res, verify_output_data)
        assert (res.dtype == out_dtype)
kEngM=LnPCZ.astype('''float16''')
cKefs=LnPCZ.astype('''float64''')
at4ii=LnPCZ.astype('''uint8''')
sZ2up=at4ii.reshape((2,5,))
quantize_test_driver(in_dtype='''int16''',quant_args={'''out_zero_point''':kEngM,'''out_scale''':cKefs},axis=0,out_dtype='''uint8''',in_data=CGBXS,verify_output_data=sZ2up)
