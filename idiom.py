from binaryninja import BinaryView, Function
from rpyc import connect


bv: BinaryView = connect('localhost', 8888).root.bv
logger: Function = bv.get_functions_by_name('logger')[0]

for caller in logger.caller_sites:
    arg2 = caller.function.get_parameter_at(caller.address, None, 2)
    name = bv.get_string_at(arg2.value).value
    caller.function.name = name


main: Function = bv.get_functions_by_name('main')[0]

for call in main.call_sites:
    arg0 = main.get_parameter_at(call.address, None, 0)
