# import subprocess
# import os
# import time
# import signal


# # print(os.environ)
# # print(os.environ['TVM_HOME'])
# # os.environ['TVM_HOME'] = '/home/gakki/tvm-0.8'
# p = subprocess.run('./08env.sh', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# # p = subprocess.run('python test.py', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# print((p.stdout.decode('utf-8')))
# # print((p.stdout.decode('utf-8')))
# # os.environ['TVM_HOME'] = '/home/gakki/tvm-exp'
# # print(os.environ['TVM_HOME'])
# # p = subprocess.run('mv ~/.bashrc_cp ~/.bashrc_cp2', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# # p = subprocess.run('mv ~/.bashrc ~/.bashrc_cp', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# # p = subprocess.run('mv ~/.bashrc_cp2 ~/.bashrc', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# p = subprocess.run('./expenv.sh', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# # p = subprocess.run('source .bashrc', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# # p2 = subprocess.run('python test.py', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# print((p.stdout.decode('utf-8')))
# # def Red(string):
# #     return '\033[1;31m' + string + '\033[0m'

# # def Green(string):
# #     return '\033[1;32m' + string + '\033[0m'

# # segmFid = 0
# # _MAX_HOURS = 5
# # _CMD_RUN_TVMFUZZ = "python run.py"
# # _CMD_RUN_TVMFUZZ_TEST = "TVM_BACKTRACE=1 python byproduct/program.py"
# # _CMD_RUN_TVMFUZZ_MV = f"mv byproduct/program.py byproduct/program{segmFid}.py"

# # # p = subprocess.run('TVM_BACKTRACE=1 python ../Comgraph-generation/buggy/confirmed/bug1_builderror.py', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# # # # print(Red(p.stdout.decode('utf-8')))

# # # print(Red(p.stderr.decode('utf-8')))
# # # print(Green(f'p.returncode = {p.returncode}'))
# # # print(-int(signal.SIGFPE))

# # # visit = set()

# # inconsistency = 0

# # def keepFileTVMfuzz():
# #     p = subprocess.run(_CMD_RUN_TVMFUZZ_MV, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# #     segmFid += 1

# # f = open('result.txt', 'w')
# # # f2 = open('result_segM.txt', 'w')

# # def fun(p):
# #     str = p.stderr.decode('utf-8')
# #     # print(Red(str))
# #     strs = str.split('\n')
# #     keyline = ""
# #     for i in range(len(strs)):
# #         if strs[i].strip().startswith('0:'):
# #             # print(strs[i+1])
# #             keyline = strs[i+1]
# #     if keyline:
# #         # print(keyline)
# #         eles = keyline.strip().split(',')
# #         filename = eles[0][6:-1].strip()
# #         # print(filename)
# #         lineNum = eles[1].strip()[5:].strip()
# #         return filename, lineNum
# #     return '', ''


# # beginTime = time.time()
# # while True:
# #     endTime = time.time()
# #     if endTime - beginTime > _MAX_HOURS * 3600:
# #         break
# #     os.environ['TVM_HOME'] = '/home/gakki/tvm-exp'
# #     p = subprocess.run(_CMD_RUN_TVMFUZZ, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# #     # print(Red(p.stderr.decode('utf-8')))
# #     p = subprocess.run(_CMD_RUN_TVMFUZZ_TEST, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# #     os.environ['TVM_HOME'] = '/home/gakki/tvm-0.8'
# #     p2 = subprocess.run(_CMD_RUN_TVMFUZZ_TEST, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
# #     if p.returncode != p2.returncode:
# #         inconsistency += 1
# #     else:
# #         if p.returncode == 0:
# #             pass
# #         else:
# #             p
    
# #     if p.returncode:
# #         if 'Segmentation fault' in p.stderr.decode('utf-8'):
# #             print(Green('Segmentation fault'))
# #             subprocess.run(_CMD_RUN_TVMFUZZ_MV, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# #         else:
# #             filename, lineNum = fun(p)
# #             filename2, lineNum2 = fun(p2)
# #             print(filename, filename2)
# #             if filename != filename2:
# #                 inconsistency +=1
                
# #     f.write(str(endTime-beginTime) + " " + str(inconsistency))
# #     print(inconsistency)
# # print(inconsistency)

# # f.close()


import spacy

nlp = spacy.load('en_core_web_sm')
txt1 = '''
  34: TVMFuncCall
  33: _ZNSt17_Function_handlerIFvN3tvm
  32: tvm::relay::backend::RelayBuildModule::GetFunction(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, tvm::runtime::ObjectPtr<tvm::runtime::Object> const&)::{lambda(tvm::runtime::TVMArgs, tvm::runtime::TVMRetValue*)#3}::operator()(tvm::runtime::TVMArgs, tvm::runtime::TVMRetValue*) const
  31: tvm::relay::backend::RelayBuildModule::BuildRelay(tvm::IRModule, std::unordered_map<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, tvm::runtime::NDArray, std::hash<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, std::equal_to<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, std::allocator<std::pair<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const, tvm::runtime::NDArray> > > const&, tvm::runtime::String)
  30: std::_Function_handler<void (tvm::runtime::TVMArgs, tvm::runtime::TVMRetValue*), tvm::relay::backend::GraphExecutorCodegenModule::GetFunction(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, tvm::runtime::ObjectPtr<tvm::runtime::Object> const&)::{lambda(tvm::runtime::TVMArgs, tvm::runtime::TVMRetValue*)#2}>::_M_invoke(std::_Any_data const&, tvm::runtime::TVMArgs&&, tvm::runtime::TVMRetValue*&&)
  29: tvm::relay::backend::GraphExecutorCodegen::Codegen(tvm::relay::Function, tvm::runtime::String)
  28: tvm::transform::Pass::operator()(tvm::IRModule) const
  27: tvm::transform::Pass::operator()(tvm::IRModule, tvm::transform::PassContext const&) const
  26: tvm::transform::SequentialNode::operator()(tvm::IRModule, tvm::transform::PassContext const&) const
  25: tvm::transform::Pass::operator()(tvm::IRModule, tvm::transform::PassContext const&) const
  24: tvm::transform::ModulePassNode::operator()(tvm::IRModule, tvm::transform::PassContext const&) const
  23: std::_Function_handler<void (tvm::runtime::TVMArgs, tvm::runtime::TVMRetValue*), tvm::runtime::TypedPackedFunc<tvm::IRModule (tvm::IRModule, tvm::transform::PassContext)>::AssignTypedLambda<tvm::relay::tec::LowerTEPass(std::unordered_map<DLDeviceType, tvm::Target, tvm::relay::backend::EnumClassHash, std::equal_to<DLDeviceType>, std::allocator<std::pair<DLDeviceType const, tvm::Target> > >, tvm::runtime::String const&, std::function<void (tvm::relay::Function)>)::{lambda(tvm::IRModule, tvm::transform::PassContext)#1}>(tvm::relay::tec::LowerTEPass(std::unordered_map<DLDeviceType, tvm::Target, tvm::relay::backend::EnumClassHash, std::equal_to<DLDeviceType>, std::allocator<std::pair<DLDeviceType const, tvm::Target> > >, tvm::runtime::String const&, std::function<void (tvm::relay::Function)>)::{lambda(tvm::IRModule, tvm::transform::PassContext)#1})::{lambda(tvm::runtime::TVMArgs const&, tvm::runtime::TVMRetValue*)#1}>::_M_invoke(std::_Any_data const&, tvm::runtime::TVMArgs&&, tvm::runtime::TVMRetValue*&&)
  22: tvm::relay::tec::LowerTE(tvm::IRModule const&, std::unordered_map<DLDeviceType, tvm::Target, tvm::relay::backend::EnumClassHash, std::equal_to<DLDeviceType>, std::allocator<std::pair<DLDeviceType const, tvm::Target> > >, tvm::runtime::String const&, std::function<void (tvm::relay::Function)>)
  21: tvm::transform::Pass::operator()(tvm::IRModule) const
  20: tvm::transform::Pass::operator()(tvm::IRModule, tvm::transform::PassContext const&) const
  19: tvm::relay::transform::FunctionPassNode::operator()(tvm::IRModule, tvm::transform::PassContext const&) const
  18: tvm::runtime::TypedPackedFunc<tvm::relay::Function (tvm::relay::Function, tvm::IRModule, tvm::transform::PassContext)>::AssignTypedLambda<tvm::relay::tec::LowerTensorExpr(std::unordered_map<DLDeviceType, tvm::Target, tvm::relay::backend::EnumClassHash, std::equal_to<DLDeviceType>, std::allocator<std::pair<DLDeviceType const, tvm::Target> > >, tvm::runtime::String const&, tvm::relay::tec::TECompiler, std::function<void (tvm::relay::Function)>)::{lambda(tvm::relay::Function, tvm::IRModule, tvm::transform::PassContext)#1}>(tvm::relay::tec::LowerTensorExpr(std::unordered_map<DLDeviceType, tvm::Target, tvm::relay::backend::EnumClassHash, std::equal_to<DLDeviceType>, std::allocator<std::pair<DLDeviceType const, tvm::Target> > >, tvm::runtime::String const&, tvm::relay::tec::TECompiler, std::function<void (tvm::relay::Function)>)::{lambda(tvm::relay::Function, tvm::IRModule, tvm::transform::PassContext)#1})::{lambda(tvm::runtime::TVMArgs const&, tvm::runtime::TVMRetValue*)#1}::operator()(tvm::runtime::TVMArgs const, tvm::runtime::TVMRetValue) const
  17: tvm::relay::ExprMutator::VisitExpr(tvm::RelayExpr const&)
  16: _ZZN3tvm5relay11ExprFunctorIFNS_9RelayExprERKS2_EE10InitVTableEvENUlRKNS_7r
  15: tvm::relay::transform::DeviceAwareExprMutator::VisitExpr_(tvm::relay::FunctionNode const*)
  14: tvm::relay::tec::LowerTensorExprMutator::DeviceAwareVisitExpr_(tvm::relay::FunctionNode const*)
  13: _ZN3tvm5relay9transform22DeviceAwareExprMutator21DeviceAwareVisit
  12: tvm::relay::ExprMutator::VisitExpr_(tvm::relay::FunctionNode const*)
  11: tvm::relay::ExprMutator::VisitExpr(tvm::RelayExpr const&)
  10: _ZZN3tvm5relay11ExprFunctorIFNS_9RelayExprERKS2_EE10InitVTableEvENUlRKNS_7r
  9: tvm::relay::ExprMutator::VisitExpr_(tvm::relay::TupleNode const*)
  8: tvm::relay::ExprMutator::VisitExpr(tvm::RelayExpr const&)
  7: _ZZN3tvm5relay11ExprFunctorIFNS_9RelayExprERKS2_EE10InitVTableEvENUlRKNS_7r
  6: tvm::relay::ExprMutator::VisitExpr_(tvm::relay::TupleGetItemNode const*)
  5: tvm::relay::ExprMutator::VisitExpr(tvm::RelayExpr const&)
  4: _ZZN3tvm5relay11ExprFunctorIFNS_9RelayExprERKS2_EE10InitVTableEvENUlRKNS_7r
  3: tvm::relay::transform::DeviceAwareExprMutator::VisitExpr_(tvm::relay::CallNode const*)
  2: tvm::relay::tec::LowerTensorExprMutator::DeviceAwareVisitExpr_(tvm::relay::CallNode const*)
  1: tvm::relay::tec::LowerTensorExprMutator::ResolveToPrimitive(tvm::RelayExpr)
  0: tvm::IRModuleNode::Lookup(tvm::GlobalVar const&) const
           '''

txt2 = '''
  43: TVMFuncCall
  42: _ZNSt17_Function_handlerIFvN3tvm
  41: tvm::relay::backend::RelayBuildModule::GetFunction(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, tvm::runtime::ObjectPtr<tvm::runtime::Object> const&)::{lambda(tvm::runtime::TVMArgs, tvm::runtime::TVMRetValue*)#3}::operator()(tvm::runtime::TVMArgs, tvm::runtime::TVMRetValue*) const
  40: tvm::relay::backend::RelayBuildModule::BuildRelay(tvm::IRModule, std::unordered_map<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, tvm::runtime::NDArray, std::hash<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, std::equal_to<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, std::allocator<std::pair<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const, tvm::runtime::NDArray> > > const&, tvm::runtime::String)
  39: std::_Function_handler<void (tvm::runtime::TVMArgs, tvm::runtime::TVMRetValue*), tvm::relay::backend::GraphExecutorCodegenModule::GetFunction(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, tvm::runtime::ObjectPtr<tvm::runtime::Object> const&)::{lambda(tvm::runtime::TVMArgs, tvm::runtime::TVMRetValue*)#2}>::_M_invoke(std::_Any_data const&, tvm::runtime::TVMArgs&&, tvm::runtime::TVMRetValue*&&)
  38: tvm::relay::backend::GraphExecutorCodegen::Codegen(tvm::relay::Function, tvm::runtime::String)
  37: tvm::transform::Pass::operator()(tvm::IRModule) const
  36: tvm::transform::Pass::operator()(tvm::IRModule, tvm::transform::PassContext const&) const
  35: tvm::transform::SequentialNode::operator()(tvm::IRModule, tvm::transform::PassContext const&) const
  34: tvm::transform::Pass::operator()(tvm::IRModule, tvm::transform::PassContext const&) const
  33: tvm::transform::ModulePassNode::operator()(tvm::IRModule, tvm::transform::PassContext const&) const
  32: std::_Function_handler<void (tvm::runtime::TVMArgs, tvm::runtime::TVMRetValue*), tvm::runtime::TypedPackedFunc<tvm::IRModule (tvm::IRModule, tvm::transform::PassContext)>::AssignTypedLambda<tvm::relay::tec::LowerTEPass(std::unordered_map<DLDeviceType, tvm::Target, tvm::relay::backend::EnumClassHash, std::equal_to<DLDeviceType>, std::allocator<std::pair<DLDeviceType const, tvm::Target> > >, tvm::runtime::String const&, std::function<void (tvm::relay::Function)>)::{lambda(tvm::IRModule, tvm::transform::PassContext)#1}>(tvm::relay::tec::LowerTEPass(std::unordered_map<DLDeviceType, tvm::Target, tvm::relay::backend::EnumClassHash, std::equal_to<DLDeviceType>, std::allocator<std::pair<DLDeviceType const, tvm::Target> > >, tvm::runtime::String const&, std::function<void (tvm::relay::Function)>)::{lambda(tvm::IRModule, tvm::transform::PassContext)#1})::{lambda(tvm::runtime::TVMArgs const&, tvm::runtime::TVMRetValue*)#1}>::_M_invoke(std::_Any_data const&, tvm::runtime::TVMArgs&&, tvm::runtime::TVMRetValue*&&)
  31: tvm::relay::tec::LowerTE(tvm::IRModule const&, std::unordered_map<DLDeviceType, tvm::Target, tvm::relay::backend::EnumClassHash, std::equal_to<DLDeviceType>, std::allocator<std::pair<DLDeviceType const, tvm::Target> > >, tvm::runtime::String const&, std::function<void (tvm::relay::Function)>)
  30: tvm::transform::Pass::operator()(tvm::IRModule) const
  29: tvm::transform::Pass::operator()(tvm::IRModule, tvm::transform::PassContext const&) const
  28: tvm::relay::transform::FunctionPassNode::operator()(tvm::IRModule, tvm::transform::PassContext const&) const
  27: tvm::runtime::TypedPackedFunc<tvm::relay::Function (tvm::relay::Function, tvm::IRModule, tvm::transform::PassContext)>::AssignTypedLambda<tvm::relay::tec::LowerTensorExpr(std::unordered_map<DLDeviceType, tvm::Target, tvm::relay::backend::EnumClassHash, std::equal_to<DLDeviceType>, std::allocator<std::pair<DLDeviceType const, tvm::Target> > >, tvm::runtime::String const&, tvm::relay::tec::TECompiler, std::function<void (tvm::relay::Function)>)::{lambda(tvm::relay::Function, tvm::IRModule, tvm::transform::PassContext)#1}>(tvm::relay::tec::LowerTensorExpr(std::unordered_map<DLDeviceType, tvm::Target, tvm::relay::backend::EnumClassHash, std::equal_to<DLDeviceType>, std::allocator<std::pair<DLDeviceType const, tvm::Target> > >, tvm::runtime::String const&, tvm::relay::tec::TECompiler, std::function<void (tvm::relay::Function)>)::{lambda(tvm::relay::Function, tvm::IRModule, tvm::transform::PassContext)#1})::{lambda(tvm::runtime::TVMArgs const&, tvm::runtime::TVMRetValue*)#1}::operator()(tvm::runtime::TVMArgs const, tvm::runtime::TVMRetValue) const
  26: tvm::relay::ExprMutator::VisitExpr(tvm::RelayExpr const&)
  25: _ZZN3tvm5relay11ExprFunctorIFNS_9RelayExprERKS2_EE10InitVTableEvENUlRKNS_7r
  24: tvm::relay::transform::DeviceAwareExprMutator::VisitExpr_(tvm::relay::FunctionNode const*)
  23: tvm::relay::tec::LowerTensorExprMutator::DeviceAwareVisitExpr_(tvm::relay::FunctionNode const*)
  22: _ZN3tvm5relay9transform22DeviceAwareExprMutator21DeviceAwareVisit
  21: tvm::relay::ExprMutator::VisitExpr_(tvm::relay::FunctionNode const*)
  20: tvm::relay::ExprMutator::VisitExpr(tvm::RelayExpr const&)
  19: _ZZN3tvm5relay11ExprFunctorIFNS_9RelayExprERKS2_EE10InitVTableEvENUlRKNS_7r
  18: tvm::relay::ExprMutator::VisitExpr_(tvm::relay::TupleNode const*)
  17: tvm::relay::ExprMutator::VisitExpr(tvm::RelayExpr const&)
  16: _ZZN3tvm5relay11ExprFunctorIFNS_9RelayExprERKS2_EE10InitVTableEvENUlRKNS_7r
  15: tvm::relay::transform::DeviceAwareExprMutator::VisitExpr_(tvm::relay::CallNode const*)
  14: tvm::relay::tec::LowerTensorExprMutator::DeviceAwareVisitExpr_(tvm::relay::CallNode const*)
  13: tvm::relay::ExprMutator::VisitExpr(tvm::RelayExpr const&)
  12: _ZZN3tvm5relay11ExprFunctorIFNS_9RelayExprERKS2_EE10InitVTableEvENUlRKNS_7r
  11: tvm::relay::transform::DeviceAwareExprMutator::VisitExpr_(tvm::relay::CallNode const*)
  10: tvm::relay::tec::LowerTensorExprMutator::DeviceAwareVisitExpr_(tvm::relay::CallNode const*)
  9: tvm::relay::ExprMutator::VisitExpr(tvm::RelayExpr const&)
  8: _ZZN3tvm5relay11ExprFunctorIFNS_9RelayExprERKS2_EE10InitVTableEvENUlRKNS_7r
  7: tvm::relay::transform::DeviceAwareExprMutator::VisitExpr_(tvm::relay::CallNode const*)
  6: tvm::relay::tec::LowerTensorExprMutator::DeviceAwareVisitExpr_(tvm::relay::CallNode const*)
  5: tvm::relay::ExprMutator::VisitExpr(tvm::RelayExpr const&)
  4: _ZZN3tvm5relay11ExprFunctorIFNS_9RelayExprERKS2_EE10InitVTableEvENUlRKNS_7r
  3: tvm::relay::transform::DeviceAwareExprMutator::VisitExpr_(tvm::relay::CallNode const*)
  2: tvm::relay::tec::LowerTensorExprMutator::DeviceAwareVisitExpr_(tvm::relay::CallNode const*)
  1: tvm::relay::tec::LowerTensorExprMutator::ResolveToPrimitive(tvm::RelayExpr)
  0: tvm::IRModuleNode::Lookup(tvm::GlobalVar const&) const
           '''
average = 0
txt1 = txt1.strip()
txt2 = txt2.strip()
txts1 = txt1.split('\n')
txts2 = txt2.split('\n')
print('>>>', len(txts1), len(txts2))
for i in range(len(txts1)):
    t1 = txts1[i]
    t2 = txts2[i]
    print(t1.strip() + '\n' + t2.strip())
    doc1 = nlp(t1.strip())
    doc2 = nlp(t2.strip())
    average += doc1.similarity(doc2)
    print('++', average)

print(average/len(txts1))

# for token in doc2:
#     print(token.text, token.pos_, token.dep_)
doc1 = nlp(txt1)
doc2 = nlp(txt2)
print(doc1.similarity(doc2))



# import subprocess
# import os
# import time
# import signal


# # print(os.environ)
# # print(os.environ['TVM_HOME'])
# # os.environ['TVM_HOME'] = '/home/gakki/tvm-0.8'
# p = subprocess.run('./08env.sh', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# # p = subprocess.run('python test.py', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# print((p.stdout.decode('utf-8')))
# # print((p.stdout.decode('utf-8')))
# # os.environ['TVM_HOME'] = '/home/gakki/tvm-exp'
# # print(os.environ['TVM_HOME'])
# # p = subprocess.run('mv ~/.bashrc_cp ~/.bashrc_cp2', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# # p = subprocess.run('mv ~/.bashrc ~/.bashrc_cp', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# # p = subprocess.run('mv ~/.bashrc_cp2 ~/.bashrc', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# p = subprocess.run('./expenv.sh', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# # p = subprocess.run('source .bashrc', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# # p2 = subprocess.run('python test.py', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# print((p.stdout.decode('utf-8')))
# # def Red(string):
# #     return '\033[1;31m' + string + '\033[0m'

# # def Green(string):
# #     return '\033[1;32m' + string + '\033[0m'

# # segmFid = 0
# # _MAX_HOURS = 5
# # _CMD_RUN_TVMFUZZ = "python run.py"
# # _CMD_RUN_TVMFUZZ_TEST = "TVM_BACKTRACE=1 python byproduct/program.py"
# # _CMD_RUN_TVMFUZZ_MV = f"mv byproduct/program.py byproduct/program{segmFid}.py"

# # # p = subprocess.run('TVM_BACKTRACE=1 python ../Comgraph-generation/buggy/confirmed/bug1_builderror.py', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# # # # print(Red(p.stdout.decode('utf-8')))

# # # print(Red(p.stderr.decode('utf-8')))
# # # print(Green(f'p.returncode = {p.returncode}'))
# # # print(-int(signal.SIGFPE))

# # # visit = set()

# # inconsistency = 0

# # def keepFileTVMfuzz():
# #     p = subprocess.run(_CMD_RUN_TVMFUZZ_MV, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# #     segmFid += 1

# # f = open('result.txt', 'w')
# # # f2 = open('result_segM.txt', 'w')

# # def fun(p):
# #     str = p.stderr.decode('utf-8')
# #     # print(Red(str))
# #     strs = str.split('\n')
# #     keyline = ""
# #     for i in range(len(strs)):
# #         if strs[i].strip().startswith('0:'):
# #             # print(strs[i+1])
# #             keyline = strs[i+1]
# #     if keyline:
# #         # print(keyline)
# #         eles = keyline.strip().split(',')
# #         filename = eles[0][6:-1].strip()
# #         # print(filename)
# #         lineNum = eles[1].strip()[5:].strip()
# #         return filename, lineNum
# #     return '', ''


# # beginTime = time.time()
# # while True:
# #     endTime = time.time()
# #     if endTime - beginTime > _MAX_HOURS * 3600:
# #         break
# #     os.environ['TVM_HOME'] = '/home/gakki/tvm-exp'
# #     p = subprocess.run(_CMD_RUN_TVMFUZZ, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# #     # print(Red(p.stderr.decode('utf-8')))
# #     p = subprocess.run(_CMD_RUN_TVMFUZZ_TEST, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# #     os.environ['TVM_HOME'] = '/home/gakki/tvm-0.8'
# #     p2 = subprocess.run(_CMD_RUN_TVMFUZZ_TEST, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
# #     if p.returncode != p2.returncode:
# #         inconsistency += 1
# #     else:
# #         if p.returncode == 0:
# #             pass
# #         else:
# #             p
    
# #     if p.returncode:
# #         if 'Segmentation fault' in p.stderr.decode('utf-8'):
# #             print(Green('Segmentation fault'))
# #             subprocess.run(_CMD_RUN_TVMFUZZ_MV, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# #         else:
# #             filename, lineNum = fun(p)
# #             filename2, lineNum2 = fun(p2)
# #             print(filename, filename2)
# #             if filename != filename2:
# #                 inconsistency +=1
                
# #     f.write(str(endTime-beginTime) + " " + str(inconsistency))
# #     print(inconsistency)
# # print(inconsistency)

# # f.close()


# # import spacy

# # nlp = spacy.load('en_core_web_sm')
# # doc1 = nlp('''
           
# #   Check failed: (pf != nullptr) is false: no such function in module: func_50
# #            ''')
# # print(doc1.text)
# # doc2 = nlp('''
           
# # DiagnosticError: one or more error diagnostics were emitted, please check diagnostic render for output.
# #            ''')
# # print(doc2.text)
# # for token in doc2:
# #     print(token.text, token.pos_, token.dep_)
# # print(doc1.similarity(doc2))