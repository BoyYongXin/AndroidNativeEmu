import sys
import logging
import posixpath
from unicorn import UcError, UC_HOOK_MEM_UNMAPPED, UC_HOOK_CODE, UC_HOOK_MEM_READ, UC_HOOK_MEM_WRITE
from unicorn.arm_const import *
from androidemu.emulator import Emulator  # 仿真器
from androidemu.java.java_class_def import JavaClassDef
from androidemu.java.java_method_def import java_method_def

from samples import debug_utils


# Create java class.
class AcosUtil(metaclass=JavaClassDef, jvm_name='com/acos/utils/AcosUtil'):

    def __init__(self):
        pass

    @java_method_def(name='getAcosEnc', signature='(Ljava/lang/String;)[B', native=True)
    def get_acos_enc(self, mu):
        pass

    @java_method_def(name='getAcosDec', signature='([B)Ljava/lang/String;', native=True)
    def get_acos_dec(self, mu):
        pass

    @java_method_def(name='convertCStringToJniSafeString', signature='([B)Ljava/lang/String;', native=False,
                     args_list=['jbyteArrayLocal'])
    
    def convert_cstring_to_jni_safe_string(self, arr):
        return arr.value.decode()

    def test(self):
        pass


# Configure logging
logging.basicConfig(
    stream=sys.stdout,
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)7s %(name)34s | %(message)s"
)

logger = logging.getLogger(__name__)

# Initialize emulator
emulator = Emulator(
    vfp_inst_set=True,
    vfs_root=posixpath.join(posixpath.dirname(__file__), "vfs")
)

# Register Java class.
emulator.java_classloader.add_class(AcosUtil)

## Load all libraries.
emulator.load_library("../samples/example_binaries/libdl.so")
emulator.load_library("../samples/example_binaries/libc.so")
emulator.load_library("../samples/example_binaries/libstdc++.so")
emulator.load_library("../samples/example_binaries/libm.so")
emulator.load_library("../samples/example_binaries/libz.so")
lib_module = emulator.load_library("../samples/example_binaries/libacos_util.so")


# Show loaded modules.
logger.info("Loaded modules:")

for module in emulator.modules:
    logger.info("=> 0x%08x - %s" % (module.base, module.filename))

# Debug
# emulator.mu.hook_add(UC_HOOK_CODE, debug_utils.hook_code)
# emulator.mu.hook_add(UC_HOOK_MEM_UNMAPPED, debug_utils.hook_unmapped)
# emulator.mu.hook_add(UC_HOOK_MEM_WRITE, debug_utils.hook_mem_write)
# emulator.mu.hook_add(UC_HOOK_MEM_READ, debug_utils.hook_mem_read)

try:
    # Run JNI_OnLoad.
    #   JNI_OnLoad will call 'RegisterNatives'.
    emulator.call_symbol(lib_module, 'JNI_OnLoad', emulator.java_vm.address_ptr, 0x00)

    # Do native stuff.
    acos_util = AcosUtil()
    result = acos_util.get_acos_enc(emulator, 'fuckkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk')
    print(result)
    result_hex = ''.join(['%02x' % b for b in result])
    print(result_hex)
    result = acos_util.get_acos_dec(emulator, bytearray(bytes.fromhex(result_hex)))
    print(result)

    # Dump natives found.
    logger.info("Exited EMU.")
    logger.info("Native methods registered to MainActivity:")

    for method in AcosUtil.jvm_methods.values():
        if method.native:
            logger.info("- [0x%08x] %s - %s" % (method.native_addr, method.name, method.signature))
except UcError as e:
    print("Exit at %x" % emulator.mu.reg_read(UC_ARM_REG_PC))
    raise


def get_acos_dec(enc):
    emulator.call_symbol(lib_module, 'JNI_OnLoad', emulator.java_vm.address_ptr, 0x00)

    # Do native stuff.
    acos_util = AcosUtil()
    enc =eval(enc)
    # enc = bytearray(enc)
    # print(enc)
    # result = acos_util.get_acos_enc(emulator, 'fuckkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk')
    enc_hex = ''.join(['%02x' % b for b in enc])
    # print(enc_hex)
    result = acos_util.get_acos_dec(emulator, bytearray(bytes.fromhex(enc_hex)))
    return result

def get_acos_enc(enc_string):
    # Run JNI_OnLoad.
    #   JNI_OnLoad will call 'RegisterNatives'.
    emulator.call_symbol(lib_module, 'JNI_OnLoad', emulator.java_vm.address_ptr, 0x00)
    # Do native stuff.
    acos_util = AcosUtil()
    result = acos_util.get_acos_enc(emulator, enc_string)
    return result