from cffi import FFI
ffi = FFI()
ffi.cdef("float sum(float a, float b);")
ffi_sum = ffi.dlopen("mymath.dll")

def sum(a, b):
  return ffi_sum.sum(a, b)

if __name__ == "__main__":
  print sum(2.1, 3.2)