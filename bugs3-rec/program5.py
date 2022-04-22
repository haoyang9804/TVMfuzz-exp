import tvm.topi.testing
import scipy.sparse as sp
import tvm.relay as relay
from scipy import special
from tvm.testing import assert_allclose
from tvm.relay.ty import IncompleteType
import scipy
from tvm.relay import expr as _expr
from tvm.relay.testing import create_workload
import logging
from tvm.relay import TypeMutator
from tvm.relay.transform import FastMath
from tvm.relay.testing import check_grad
import tvm.relay.testing
from tvm.relay.testing.synthetic import get_workload
from tvm.autotvm.tuner import RandomTuner
from tvm import te
from tvm.relay.transform import un_cps
from tvm.relay.scope_builder import ScopeBuilder
from tvm.relay.prelude import Prelude
from tvm.contrib import graph_runtime
import sys
from tvm import autotvm
from tvm.relay.testing import rand
from tvm.relay.op.annotation import compiler_end
import time
from tvm.relay.testing.temp_op_attr import TempOpAttr
import tvm.relay.transform as _transform
from tvm.relay import create_executor
import numpy as np
import tvm
from tvm.relay.ty import RefType
import itertools
from tvm.relay.ty import TypeVar
from tvm.relay.testing import run_opt_pass
from tvm.relay.ty import FuncType
from tvm.relay.op.annotation import compiler_begin
import pytest
import math
from numpy import isclose
from tvm.ir import structural_equal
from tvm.relay import Any
from tvm.relay.ty import TypeCall
from tvm.relay.transform import to_cps
from tvm.relay.ty import TypeRelation
from tvm.relay.analysis import check_kind
from tvm import relay
from tvm.relay.ty import TupleType
from tvm.relay import TypeVisitor
from tvm.relay.analysis import check_basic_block_normal_form
import json
from tvm.relay.analysis import get_calibration_data
from tvm.relay.ty import TensorType
from tvm.contrib.nvcc import have_fp16
from functools import wraps
from tvm.relay.ty import GlobalTypeVar
from tvm.relay.testing import count
from tvm.relay import analysis
from tvm import relay as rly
from typing import Union
from tvm.relay.testing import make_nat_expr
from tvm.relay.adt import TypeData
from tvm.relay.backend.interpreter import ConstructorValue
from tvm.relay.data_dep_optimization import simplify_fc_transpose
from tvm.relay import TypeFunctor
from tvm.relay.testing import enabled_targets
from tvm.relay.analysis import well_formed
import tvm.relay.transform
import random
from tvm.runtime import container
from tvm.relay import op
from tvm.ir import IRModule
from tvm.relay import testing
from tvm import topi
from tvm.relay.testing import Prelude
from tvm.relay.analysis import Feature
from tvm.relay.transform import SimplifyInference
from tvm.relay.build_module import bind_params_by_name
from tvm.relay import transform
from tvm.relay.testing import run_infer_type
import os
from tvm.relay.backend.interpreter import RefValue
from tvm.relay.analysis import detect_feature
import tvm.testing
from tvm.relay import ExprVisitor
from tvm import nd
from tvm import runtime

E6kRS=np.array([(-63.5),(-45),(-23.0),(-62),(-61.5),30,8,8.1,23.53,4,])
VwLe4=E6kRS.astype('''float32''')


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
Yo6H6=E6kRS.astype('''int32''')
ltJrj=E6kRS.astype('''uint8''')
RfuwU=ltJrj.reshape((2,5,))
YDncN=np.transpose(RfuwU)
quantize_test_driver(in_dtype='''float32''',quant_args={'''out_zero_point''':Yo6H6,'''out_scale''':VwLe4},axis=0,out_dtype='''uint8''',in_data=YDncN,verify_output_data=YDncN)
