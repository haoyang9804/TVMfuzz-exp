from tvm.relay.testing import create_workload
import tvm.relay.transform as _transform
from tvm import autotvm
from tvm.relay.analysis import Feature
import json
from tvm.contrib.nvcc import have_fp16
from tvm.relay import TypeFunctor
from tvm.relay.transform import un_cps
from tvm.relay import TypeMutator
from tvm.relay.data_dep_optimization import simplify_fc_transpose
from tvm.contrib import graph_runtime
from tvm.relay import transform
import os
from tvm.relay import TypeVisitor
from tvm.relay.analysis import well_formed
from tvm.relay.testing import run_infer_type
from tvm import runtime
from tvm.relay import ExprVisitor
from tvm.relay.transform import SimplifyInference
from tvm.relay.testing import count
import tvm.relay.testing
import tvm.relay as relay
from tvm.runtime import container
from numpy import isclose
from tvm.relay import analysis
from tvm.relay.ty import TypeVar
from tvm.ir import structural_equal
import tvm.testing
from tvm.relay.transform import to_cps
from scipy import special
import scipy.sparse as sp
from tvm.relay.scope_builder import ScopeBuilder
import tvm.topi.testing
from tvm.relay.ty import FuncType
from tvm import relay
from tvm.relay.testing import Prelude
from tvm.relay.ty import TypeCall
import tvm
from tvm.relay.adt import TypeData
from tvm import nd
import time
from tvm.testing import assert_allclose
from tvm.relay.analysis import check_basic_block_normal_form
from tvm.relay.prelude import Prelude
from tvm.relay.ty import TypeRelation
from tvm.relay import op
from tvm.relay.backend.interpreter import ConstructorValue
from tvm import te
import sys
from tvm.relay.analysis import get_calibration_data
import math
from tvm.relay.testing import rand
from tvm.relay.testing.synthetic import get_workload
from tvm.relay import Any
from tvm.relay.ty import TupleType
from tvm.relay.testing import enabled_targets
import pytest
from tvm.relay import expr as _expr
from tvm import relay as rly
from tvm.relay.testing import check_grad
from tvm.relay.ty import RefType
import tvm.relay.transform
from tvm.relay.transform import FastMath
from tvm.relay.testing import make_nat_expr
from tvm.relay.build_module import bind_params_by_name
from tvm.ir import IRModule
import itertools
from functools import wraps
import numpy as np
from tvm.relay import testing
from tvm.relay.op.annotation import compiler_end
from tvm.relay.backend.interpreter import RefValue
from tvm.relay import create_executor
import random
from tvm.relay.analysis import check_kind
from tvm import topi
import scipy
from tvm.relay.testing.temp_op_attr import TempOpAttr
import logging
from tvm.autotvm.tuner import RandomTuner
from tvm.relay.testing import run_opt_pass
from tvm.relay.analysis import detect_feature
from tvm.relay.ty import TensorType
from typing import Union
from tvm.relay.ty import GlobalTypeVar
from tvm.relay.op.annotation import compiler_begin
from tvm.relay.ty import IncompleteType

j9wsC=np.array([(-23.4),(-35),(-52.4),(-62),(-18.4),30,31,31.5,26.58,32,])
yCeRG=j9wsC.astype('''float64''')


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
Nc4J7=j9wsC.astype('''float64''')
h8cws=j9wsC.astype('''uint8''')
RgJwu=h8cws.reshape((2,5,))
xH2Ow=np.transpose(RgJwu)
quantize_test_driver(in_dtype='''float32''',quant_args={'''out_zero_point''':yCeRG,'''out_scale''':Nc4J7},axis=1,out_dtype='''uint8''',in_data=xH2Ow,verify_output_data=xH2Ow)
jOPAv=j9wsC.astype('''uint32''')
TjFTk=jOPAv.reshape((2,5,))
FQa0X=np.transpose(RgJwu)
