import sys

SHARED_CAFFE_RESOLVER = None

class CaffeResolver(object):
    def __init__(self):
        self.import_caffe()

    def import_caffe(self):
        self.caffe = None
        # Fall back to the protobuf implementation
        from . import caffepb
        self.caffepb = caffepb
        show_fallback_warning()
        self.NetParameter = self.caffepb.NetParameter

    def has_pycaffe(self):
        return self.caffe is not None

def get_caffe_resolver():
    global SHARED_CAFFE_RESOLVER
    if SHARED_CAFFE_RESOLVER is None:
        SHARED_CAFFE_RESOLVER = CaffeResolver()
    return SHARED_CAFFE_RESOLVER

def has_pycaffe():
    return get_caffe_resolver().has_pycaffe()

def show_fallback_warning():
    msg = '''
------------------------------------------------------------
    WARNING: PyCaffe not found!
    Falling back to a pure protocol buffer implementation.
    * Conversions will be drastically slower.
    * This backend is UNTESTED!
------------------------------------------------------------

'''
    sys.stderr.write(msg)
