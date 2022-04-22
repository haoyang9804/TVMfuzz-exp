

from webbrowser import get


txt = '''
6: TVMFuncCall
  5: _ZNSt17_Function_handlerIFvN3tvm7runtime7
  4: tvm::runtime::{lambda(tvm::runtime::TVMArgs, tvm::runtime::TVMRetValue*)#1}::operator()(tvm::runtime::TVMArgs, tvm::runtime::TVMRetValue*) const [clone .isra.808]
  3: tvm::runtime::GraphExecutorCreate(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, tvm::runtime::Module const&, std::vector<DLDevice, std::allocator<DLDevice> > const&, tvm::runtime::PackedFunc)
  2: tvm::runtime::GraphExecutor::Init(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, tvm::runtime::Module, std::vector<DLDevice, std::allocator<DLDevice> > const&, tvm::runtime::PackedFunc)
  1: tvm::runtime::GraphExecutor::SetupOpExecs()
  0: tvm::runtime::GraphExecutor::CreateTVMOp(tvm::runtime::TVMOpParam const&, std::vector<DLTensor, std::allocator<DLTensor> > const&)
  File "../src/runtime/graph_executor/graph_executor.cc", line 503
'''

def startswithNum(line):
    line = line.strip()
    if line.startswith('0') or \
        line.startswith('1') or \
            line.startswith('2') or \
                line.startswith('3') or \
                    line.startswith('4') or \
                        line.startswith('5') or \
                            line.startswith('6') or \
                                line.startswith('7') or \
                                    line.startswith('8') or \
                                        line.startswith('9'):
                                            return True
    return False
                            
def getPureReport():
    pureTxt = ''
    lines = txt.split('\n')
    for line in lines:
        if startswithNum(line):
            pureTxt += line 
    # return pureTxt
    print(pureTxt)
    
getPureReport()