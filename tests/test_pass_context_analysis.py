import numpy as np
import pytest

import tvm
from tvm import relay
from tvm.relay import expr as _expr


def test_device_copy():
    if not tvm.testing.device_enabled("cuda") or not tvm.gpu(0).exist:
        return

    mod = tvm.IRModule()
    x = relay.var("x", shape=(2, 3))
    copy = relay.op.device_copy(x, tvm.cpu(), tvm.gpu())
    out = copy + relay.const(np.random.rand(2, 3))
    glb_var = relay.GlobalVar("main")
    mod[glb_var] = relay.Function([x], out)


def test_shape_func():
    if not tvm.testing.device_enabled("cuda") or not tvm.gpu(0).exist:
        return

    mod = tvm.IRModule()
    data_shape = (relay.Any(),)
    x = relay.var("x", shape=data_shape)
    y = relay.op.vm.shape_of(x)
    z = relay.nn.relu(y)
    p0 = relay.var("p0", shape=data_shape)
    fn = relay.Function([p0], z)
    out = relay.var("out", shape=(1,), dtype="int64")
    ins = relay.Tuple([y])
    outs = relay.Tuple([out])
    is_inputs = [False]
    shape_func = relay.op.vm.shape_func(fn, ins, outs, is_inputs)
    mod["main"] = relay.Function([x, out], shape_func)


def test_vm_shape_of():
    if not tvm.testing.device_enabled("cuda") or not tvm.gpu(0).exist:
        return

    mod = tvm.IRModule()
    data_shape = (relay.Any(),)
    x = relay.var("x", shape=data_shape)
    y = relay.op.vm.shape_of(x)
    mod["main"] = relay.Function([x], y)


def test_alloc_storage():
    if not tvm.testing.device_enabled("cuda") or not tvm.gpu(0).exist:
        return

    mod = tvm.IRModule()
    mod.import_from_std("core.rly")
    size = relay.Var("size", relay.scalar_type("int64"))
    alignment = relay.Var("alignment", relay.scalar_type("int64"))
    # allocate a chunk on of memory on gpu.
    sto = relay.op.memory.alloc_storage(size, alignment, tvm.gpu())
    mod["main"] = relay.Function([size, alignment], sto)
    main = mod["main"]
    body = main.body

    cpu_dev = tvm.cpu().device_type
    gpu_dev = tvm.gpu().device_type


def test_alloc_tensor():
    if not tvm.testing.device_enabled("cuda") or not tvm.gpu(0).exist:
        return

    mod = tvm.IRModule()
    mod.import_from_std("core.rly")
    sto_type = relay.TypeCall(mod.get_global_type_var("Storage"), [])
    sto = relay.Var("x", sto_type)
    sh = relay.const(np.array([3, 2]), dtype="int64")
    at = relay.op.memory.alloc_tensor(sto, relay.const(0, dtype="int64"), sh)
    mod["main"] = relay.Function([sto], at)
    main = mod["main"]
    body = main.body

    cpu_dev = tvm.cpu().device_type
    gpu_dev = tvm.gpu().device_type


def test_vm_reshape_tensor():
    if not tvm.testing.device_enabled("cuda") or not tvm.gpu(0).exist:
        return

    x = relay.var("x", shape=(2, 8), dtype="float32")
    shape = relay.const([-1, 4, 2], dtype="int64")
    y = relay.op.vm.reshape_tensor(x, shape, [2, 4, 2])
    mod = tvm.IRModule()
    mod["main"] = relay.Function([x], y)
    main = mod["main"]
    body = main.body



def test_dynamic_input():
    if not tvm.testing.device_enabled("cuda") or not tvm.gpu(0).exist:
        return

    mod = tvm.IRModule()
    data_shape = (relay.Any(), relay.Any())
    x0 = relay.var("x0", shape=data_shape)
    x1 = relay.var("x1", shape=data_shape)
    mod["main"] = relay.Function([x0, x1], x0 + x1)

    compiler = relay.vm.VMCompiler()
    mod, _ = compiler.optimize(mod, target="cuda")
    main = mod["main"]

    gpu_dev = tvm.gpu().device_type