from binaryninja import BinaryView, Function
from rpyc import connect


bv: BinaryView = connect('localhost', 8888).root.bv
logger: Function = bv.get_functions_by_name('logger')[0]
print(hex(logger.start))

for caller in logger.caller_sites:
    arg2 = caller.function.get_parameter_at(caller.address, None, 2)
    name = bv.get_string_at(arg2.value).value
    caller.function.name = name


main: Function = bv.get_functions_by_name('main')[0]

for call, callee in zip(main.call_sites, main.callees):
    print(call, callee)
