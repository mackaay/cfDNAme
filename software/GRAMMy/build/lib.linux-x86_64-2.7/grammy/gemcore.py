# This file was automatically generated by SWIG (http://www.swig.org).
# Version 2.0.4
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_gemcore', [dirname(__file__)])
        except ImportError:
            import _gemcore
            return _gemcore
        if fp is not None:
            try:
                _mod = imp.load_module('_gemcore', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _gemcore = swig_import_helper()
    del swig_import_helper
else:
    import _gemcore
del version_info
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

class SwigPyIterator:
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SwigPyIterator, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SwigPyIterator, name)
    def __init__(self, *args, **kwargs): raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _gemcore.delete_SwigPyIterator
    __del__ = lambda self : None;
    def value(self): return _gemcore.SwigPyIterator_value(self)
    def incr(self, n = 1): return _gemcore.SwigPyIterator_incr(self, n)
    def decr(self, n = 1): return _gemcore.SwigPyIterator_decr(self, n)
    def distance(self, *args): return _gemcore.SwigPyIterator_distance(self, *args)
    def equal(self, *args): return _gemcore.SwigPyIterator_equal(self, *args)
    def copy(self): return _gemcore.SwigPyIterator_copy(self)
    def next(self): return _gemcore.SwigPyIterator_next(self)
    def __next__(self): return _gemcore.SwigPyIterator___next__(self)
    def previous(self): return _gemcore.SwigPyIterator_previous(self)
    def advance(self, *args): return _gemcore.SwigPyIterator_advance(self, *args)
    def __eq__(self, *args): return _gemcore.SwigPyIterator___eq__(self, *args)
    def __ne__(self, *args): return _gemcore.SwigPyIterator___ne__(self, *args)
    def __iadd__(self, *args): return _gemcore.SwigPyIterator___iadd__(self, *args)
    def __isub__(self, *args): return _gemcore.SwigPyIterator___isub__(self, *args)
    def __add__(self, *args): return _gemcore.SwigPyIterator___add__(self, *args)
    def __sub__(self, *args): return _gemcore.SwigPyIterator___sub__(self, *args)
    def __iter__(self): return self
SwigPyIterator_swigregister = _gemcore.SwigPyIterator_swigregister
SwigPyIterator_swigregister(SwigPyIterator)

MM_MAX_LINE_LENGTH = _gemcore.MM_MAX_LINE_LENGTH
MatrixMarketBanner = _gemcore.MatrixMarketBanner
MM_MAX_TOKEN_LENGTH = _gemcore.MM_MAX_TOKEN_LENGTH

def mm_typecode_to_str(*args):
  return _gemcore.mm_typecode_to_str(*args)
mm_typecode_to_str = _gemcore.mm_typecode_to_str

def mm_read_banner(*args):
  return _gemcore.mm_read_banner(*args)
mm_read_banner = _gemcore.mm_read_banner

def mm_read_mtx_crd_size(*args):
  return _gemcore.mm_read_mtx_crd_size(*args)
mm_read_mtx_crd_size = _gemcore.mm_read_mtx_crd_size

def mm_read_mtx_array_size(*args):
  return _gemcore.mm_read_mtx_array_size(*args)
mm_read_mtx_array_size = _gemcore.mm_read_mtx_array_size

def mm_write_banner(*args):
  return _gemcore.mm_write_banner(*args)
mm_write_banner = _gemcore.mm_write_banner

def mm_write_mtx_crd_size(*args):
  return _gemcore.mm_write_mtx_crd_size(*args)
mm_write_mtx_crd_size = _gemcore.mm_write_mtx_crd_size

def mm_write_mtx_array_size(*args):
  return _gemcore.mm_write_mtx_array_size(*args)
mm_write_mtx_array_size = _gemcore.mm_write_mtx_array_size

def mm_is_valid(*args):
  return _gemcore.mm_is_valid(*args)
mm_is_valid = _gemcore.mm_is_valid
MM_COULD_NOT_READ_FILE = _gemcore.MM_COULD_NOT_READ_FILE
MM_PREMATURE_EOF = _gemcore.MM_PREMATURE_EOF
MM_NOT_MTX = _gemcore.MM_NOT_MTX
MM_NO_HEADER = _gemcore.MM_NO_HEADER
MM_UNSUPPORTED_TYPE = _gemcore.MM_UNSUPPORTED_TYPE
MM_LINE_TOO_LONG = _gemcore.MM_LINE_TOO_LONG
MM_COULD_NOT_WRITE_FILE = _gemcore.MM_COULD_NOT_WRITE_FILE
MM_MTX_STR = _gemcore.MM_MTX_STR
MM_ARRAY_STR = _gemcore.MM_ARRAY_STR
MM_DENSE_STR = _gemcore.MM_DENSE_STR
MM_COORDINATE_STR = _gemcore.MM_COORDINATE_STR
MM_SPARSE_STR = _gemcore.MM_SPARSE_STR
MM_COMPLEX_STR = _gemcore.MM_COMPLEX_STR
MM_REAL_STR = _gemcore.MM_REAL_STR
MM_INT_STR = _gemcore.MM_INT_STR
MM_GENERAL_STR = _gemcore.MM_GENERAL_STR
MM_SYMM_STR = _gemcore.MM_SYMM_STR
MM_HERM_STR = _gemcore.MM_HERM_STR
MM_SKEW_STR = _gemcore.MM_SKEW_STR
MM_PATTERN_STR = _gemcore.MM_PATTERN_STR

def mm_write_mtx_crd(*args):
  return _gemcore.mm_write_mtx_crd(*args)
mm_write_mtx_crd = _gemcore.mm_write_mtx_crd

def mm_read_mtx_crd_data(*args):
  return _gemcore.mm_read_mtx_crd_data(*args)
mm_read_mtx_crd_data = _gemcore.mm_read_mtx_crd_data

def mm_read_mtx_crd_entry(*args):
  return _gemcore.mm_read_mtx_crd_entry(*args)
mm_read_mtx_crd_entry = _gemcore.mm_read_mtx_crd_entry

def mm_read_unsymmetric_sparse(*args):
  return _gemcore.mm_read_unsymmetric_sparse(*args)
mm_read_unsymmetric_sparse = _gemcore.mm_read_unsymmetric_sparse

def vdif(*args):
  return _gemcore.vdif(*args)
vdif = _gemcore.vdif

def dmax(*args):
  return _gemcore.dmax(*args)
dmax = _gemcore.dmax
class VectorFloat:
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, VectorFloat, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, VectorFloat, name)
    __repr__ = _swig_repr
    def iterator(self): return _gemcore.VectorFloat_iterator(self)
    def __iter__(self): return self.iterator()
    def __nonzero__(self): return _gemcore.VectorFloat___nonzero__(self)
    def __bool__(self): return _gemcore.VectorFloat___bool__(self)
    def __len__(self): return _gemcore.VectorFloat___len__(self)
    def pop(self): return _gemcore.VectorFloat_pop(self)
    def __getslice__(self, *args): return _gemcore.VectorFloat___getslice__(self, *args)
    def __setslice__(self, *args): return _gemcore.VectorFloat___setslice__(self, *args)
    def __delslice__(self, *args): return _gemcore.VectorFloat___delslice__(self, *args)
    def __delitem__(self, *args): return _gemcore.VectorFloat___delitem__(self, *args)
    def __getitem__(self, *args): return _gemcore.VectorFloat___getitem__(self, *args)
    def __setitem__(self, *args): return _gemcore.VectorFloat___setitem__(self, *args)
    def append(self, *args): return _gemcore.VectorFloat_append(self, *args)
    def empty(self): return _gemcore.VectorFloat_empty(self)
    def size(self): return _gemcore.VectorFloat_size(self)
    def clear(self): return _gemcore.VectorFloat_clear(self)
    def swap(self, *args): return _gemcore.VectorFloat_swap(self, *args)
    def get_allocator(self): return _gemcore.VectorFloat_get_allocator(self)
    def begin(self): return _gemcore.VectorFloat_begin(self)
    def end(self): return _gemcore.VectorFloat_end(self)
    def rbegin(self): return _gemcore.VectorFloat_rbegin(self)
    def rend(self): return _gemcore.VectorFloat_rend(self)
    def pop_back(self): return _gemcore.VectorFloat_pop_back(self)
    def erase(self, *args): return _gemcore.VectorFloat_erase(self, *args)
    def __init__(self, *args): 
        this = _gemcore.new_VectorFloat(*args)
        try: self.this.append(this)
        except: self.this = this
    def push_back(self, *args): return _gemcore.VectorFloat_push_back(self, *args)
    def front(self): return _gemcore.VectorFloat_front(self)
    def back(self): return _gemcore.VectorFloat_back(self)
    def assign(self, *args): return _gemcore.VectorFloat_assign(self, *args)
    def resize(self, *args): return _gemcore.VectorFloat_resize(self, *args)
    def insert(self, *args): return _gemcore.VectorFloat_insert(self, *args)
    def reserve(self, *args): return _gemcore.VectorFloat_reserve(self, *args)
    def capacity(self): return _gemcore.VectorFloat_capacity(self)
    __swig_destroy__ = _gemcore.delete_VectorFloat
    __del__ = lambda self : None;
VectorFloat_swigregister = _gemcore.VectorFloat_swigregister
VectorFloat_swigregister(VectorFloat)
cvar = _gemcore.cvar
dft_rt_pflt = cvar.dft_rt_pflt
dft_rt_lflt = cvar.dft_rt_lflt
dft_rt_TR1_UM_L = cvar.dft_rt_TR1_UM_L
dft_rt_TR1_UM_P = cvar.dft_rt_TR1_UM_P

class VectorInt:
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, VectorInt, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, VectorInt, name)
    __repr__ = _swig_repr
    def iterator(self): return _gemcore.VectorInt_iterator(self)
    def __iter__(self): return self.iterator()
    def __nonzero__(self): return _gemcore.VectorInt___nonzero__(self)
    def __bool__(self): return _gemcore.VectorInt___bool__(self)
    def __len__(self): return _gemcore.VectorInt___len__(self)
    def pop(self): return _gemcore.VectorInt_pop(self)
    def __getslice__(self, *args): return _gemcore.VectorInt___getslice__(self, *args)
    def __setslice__(self, *args): return _gemcore.VectorInt___setslice__(self, *args)
    def __delslice__(self, *args): return _gemcore.VectorInt___delslice__(self, *args)
    def __delitem__(self, *args): return _gemcore.VectorInt___delitem__(self, *args)
    def __getitem__(self, *args): return _gemcore.VectorInt___getitem__(self, *args)
    def __setitem__(self, *args): return _gemcore.VectorInt___setitem__(self, *args)
    def append(self, *args): return _gemcore.VectorInt_append(self, *args)
    def empty(self): return _gemcore.VectorInt_empty(self)
    def size(self): return _gemcore.VectorInt_size(self)
    def clear(self): return _gemcore.VectorInt_clear(self)
    def swap(self, *args): return _gemcore.VectorInt_swap(self, *args)
    def get_allocator(self): return _gemcore.VectorInt_get_allocator(self)
    def begin(self): return _gemcore.VectorInt_begin(self)
    def end(self): return _gemcore.VectorInt_end(self)
    def rbegin(self): return _gemcore.VectorInt_rbegin(self)
    def rend(self): return _gemcore.VectorInt_rend(self)
    def pop_back(self): return _gemcore.VectorInt_pop_back(self)
    def erase(self, *args): return _gemcore.VectorInt_erase(self, *args)
    def __init__(self, *args): 
        this = _gemcore.new_VectorInt(*args)
        try: self.this.append(this)
        except: self.this = this
    def push_back(self, *args): return _gemcore.VectorInt_push_back(self, *args)
    def front(self): return _gemcore.VectorInt_front(self)
    def back(self): return _gemcore.VectorInt_back(self)
    def assign(self, *args): return _gemcore.VectorInt_assign(self, *args)
    def resize(self, *args): return _gemcore.VectorInt_resize(self, *args)
    def insert(self, *args): return _gemcore.VectorInt_insert(self, *args)
    def reserve(self, *args): return _gemcore.VectorInt_reserve(self, *args)
    def capacity(self): return _gemcore.VectorInt_capacity(self)
    __swig_destroy__ = _gemcore.delete_VectorInt
    __del__ = lambda self : None;
VectorInt_swigregister = _gemcore.VectorInt_swigregister
VectorInt_swigregister(VectorInt)

class VectorDouble:
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, VectorDouble, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, VectorDouble, name)
    __repr__ = _swig_repr
    def iterator(self): return _gemcore.VectorDouble_iterator(self)
    def __iter__(self): return self.iterator()
    def __nonzero__(self): return _gemcore.VectorDouble___nonzero__(self)
    def __bool__(self): return _gemcore.VectorDouble___bool__(self)
    def __len__(self): return _gemcore.VectorDouble___len__(self)
    def pop(self): return _gemcore.VectorDouble_pop(self)
    def __getslice__(self, *args): return _gemcore.VectorDouble___getslice__(self, *args)
    def __setslice__(self, *args): return _gemcore.VectorDouble___setslice__(self, *args)
    def __delslice__(self, *args): return _gemcore.VectorDouble___delslice__(self, *args)
    def __delitem__(self, *args): return _gemcore.VectorDouble___delitem__(self, *args)
    def __getitem__(self, *args): return _gemcore.VectorDouble___getitem__(self, *args)
    def __setitem__(self, *args): return _gemcore.VectorDouble___setitem__(self, *args)
    def append(self, *args): return _gemcore.VectorDouble_append(self, *args)
    def empty(self): return _gemcore.VectorDouble_empty(self)
    def size(self): return _gemcore.VectorDouble_size(self)
    def clear(self): return _gemcore.VectorDouble_clear(self)
    def swap(self, *args): return _gemcore.VectorDouble_swap(self, *args)
    def get_allocator(self): return _gemcore.VectorDouble_get_allocator(self)
    def begin(self): return _gemcore.VectorDouble_begin(self)
    def end(self): return _gemcore.VectorDouble_end(self)
    def rbegin(self): return _gemcore.VectorDouble_rbegin(self)
    def rend(self): return _gemcore.VectorDouble_rend(self)
    def pop_back(self): return _gemcore.VectorDouble_pop_back(self)
    def erase(self, *args): return _gemcore.VectorDouble_erase(self, *args)
    def __init__(self, *args): 
        this = _gemcore.new_VectorDouble(*args)
        try: self.this.append(this)
        except: self.this = this
    def push_back(self, *args): return _gemcore.VectorDouble_push_back(self, *args)
    def front(self): return _gemcore.VectorDouble_front(self)
    def back(self): return _gemcore.VectorDouble_back(self)
    def assign(self, *args): return _gemcore.VectorDouble_assign(self, *args)
    def resize(self, *args): return _gemcore.VectorDouble_resize(self, *args)
    def insert(self, *args): return _gemcore.VectorDouble_insert(self, *args)
    def reserve(self, *args): return _gemcore.VectorDouble_reserve(self, *args)
    def capacity(self): return _gemcore.VectorDouble_capacity(self)
    __swig_destroy__ = _gemcore.delete_VectorDouble
    __del__ = lambda self : None;
VectorDouble_swigregister = _gemcore.VectorDouble_swigregister
VectorDouble_swigregister(VectorDouble)

class MatrixFloat:
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, MatrixFloat, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, MatrixFloat, name)
    __repr__ = _swig_repr
    def iterator(self): return _gemcore.MatrixFloat_iterator(self)
    def __iter__(self): return self.iterator()
    def __nonzero__(self): return _gemcore.MatrixFloat___nonzero__(self)
    def __bool__(self): return _gemcore.MatrixFloat___bool__(self)
    def __len__(self): return _gemcore.MatrixFloat___len__(self)
    def pop(self): return _gemcore.MatrixFloat_pop(self)
    def __getslice__(self, *args): return _gemcore.MatrixFloat___getslice__(self, *args)
    def __setslice__(self, *args): return _gemcore.MatrixFloat___setslice__(self, *args)
    def __delslice__(self, *args): return _gemcore.MatrixFloat___delslice__(self, *args)
    def __delitem__(self, *args): return _gemcore.MatrixFloat___delitem__(self, *args)
    def __getitem__(self, *args): return _gemcore.MatrixFloat___getitem__(self, *args)
    def __setitem__(self, *args): return _gemcore.MatrixFloat___setitem__(self, *args)
    def append(self, *args): return _gemcore.MatrixFloat_append(self, *args)
    def empty(self): return _gemcore.MatrixFloat_empty(self)
    def size(self): return _gemcore.MatrixFloat_size(self)
    def clear(self): return _gemcore.MatrixFloat_clear(self)
    def swap(self, *args): return _gemcore.MatrixFloat_swap(self, *args)
    def get_allocator(self): return _gemcore.MatrixFloat_get_allocator(self)
    def begin(self): return _gemcore.MatrixFloat_begin(self)
    def end(self): return _gemcore.MatrixFloat_end(self)
    def rbegin(self): return _gemcore.MatrixFloat_rbegin(self)
    def rend(self): return _gemcore.MatrixFloat_rend(self)
    def pop_back(self): return _gemcore.MatrixFloat_pop_back(self)
    def erase(self, *args): return _gemcore.MatrixFloat_erase(self, *args)
    def __init__(self, *args): 
        this = _gemcore.new_MatrixFloat(*args)
        try: self.this.append(this)
        except: self.this = this
    def push_back(self, *args): return _gemcore.MatrixFloat_push_back(self, *args)
    def front(self): return _gemcore.MatrixFloat_front(self)
    def back(self): return _gemcore.MatrixFloat_back(self)
    def assign(self, *args): return _gemcore.MatrixFloat_assign(self, *args)
    def resize(self, *args): return _gemcore.MatrixFloat_resize(self, *args)
    def insert(self, *args): return _gemcore.MatrixFloat_insert(self, *args)
    def reserve(self, *args): return _gemcore.MatrixFloat_reserve(self, *args)
    def capacity(self): return _gemcore.MatrixFloat_capacity(self)
    __swig_destroy__ = _gemcore.delete_MatrixFloat
    __del__ = lambda self : None;
MatrixFloat_swigregister = _gemcore.MatrixFloat_swigregister
MatrixFloat_swigregister(MatrixFloat)

class cMEM:
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, cMEM, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, cMEM, name)
    __repr__ = _swig_repr
    __swig_setmethods__["N"] = _gemcore.cMEM_N_set
    __swig_getmethods__["N"] = _gemcore.cMEM_N_get
    __swig_setmethods__["M"] = _gemcore.cMEM_M_set
    __swig_getmethods__["M"] = _gemcore.cMEM_M_get
    __swig_setmethods__["R"] = _gemcore.cMEM_R_set
    __swig_getmethods__["R"] = _gemcore.cMEM_R_get
    __swig_setmethods__["logL"] = _gemcore.cMEM_logL_set
    __swig_getmethods__["logL"] = _gemcore.cMEM_logL_get
    __swig_setmethods__["plogL"] = _gemcore.cMEM_plogL_set
    __swig_getmethods__["plogL"] = _gemcore.cMEM_plogL_get
    __swig_setmethods__["V"] = _gemcore.cMEM_V_set
    __swig_getmethods__["V"] = _gemcore.cMEM_V_get
    __swig_setmethods__["pV"] = _gemcore.cMEM_pV_set
    __swig_getmethods__["pV"] = _gemcore.cMEM_pV_get
    __swig_setmethods__["Sample"] = _gemcore.cMEM_Sample_set
    __swig_getmethods__["Sample"] = _gemcore.cMEM_Sample_get
    __swig_setmethods__["P"] = _gemcore.cMEM_P_set
    __swig_getmethods__["P"] = _gemcore.cMEM_P_get
    def __init__(self, *args): 
        this = _gemcore.new_cMEM(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _gemcore.delete_cMEM
    __del__ = lambda self : None;
    def clr_P(self): return _gemcore.cMEM_clr_P(self)
    def get_P(self, *args): return _gemcore.cMEM_get_P(self, *args)
    def mstep(self): return _gemcore.cMEM_mstep(self)
    def estep(self): return _gemcore.cMEM_estep(self)
    def init_V(self, *args): return _gemcore.cMEM_init_V(self, *args)
    def loglikelihood(self): return _gemcore.cMEM_loglikelihood(self)
    def set_R(self, *args): return _gemcore.cMEM_set_R(self, *args)
    def solve(self, *args): return _gemcore.cMEM_solve(self, *args)
    def bootstrap(self, *args): return _gemcore.cMEM_bootstrap(self, *args)
    def bootstrap_sample(self): return _gemcore.cMEM_bootstrap_sample(self)
    def original_sample(self): return _gemcore.cMEM_original_sample(self)
cMEM_swigregister = _gemcore.cMEM_swigregister
cMEM_swigregister(cMEM)

class cMONO(cMEM):
    __swig_setmethods__ = {}
    for _s in [cMEM]: __swig_setmethods__.update(getattr(_s,'__swig_setmethods__',{}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, cMONO, name, value)
    __swig_getmethods__ = {}
    for _s in [cMEM]: __swig_getmethods__.update(getattr(_s,'__swig_getmethods__',{}))
    __getattr__ = lambda self, name: _swig_getattr(self, cMONO, name)
    __repr__ = _swig_repr
    __swig_setmethods__["EN"] = _gemcore.cMONO_EN_set
    __swig_getmethods__["EN"] = _gemcore.cMONO_EN_get
    __swig_setmethods__["AN"] = _gemcore.cMONO_AN_set
    __swig_getmethods__["AN"] = _gemcore.cMONO_AN_get
    __swig_setmethods__["MN"] = _gemcore.cMONO_MN_set
    __swig_getmethods__["MN"] = _gemcore.cMONO_MN_get
    __swig_setmethods__["Prg"] = _gemcore.cMONO_Prg_set
    __swig_getmethods__["Prg"] = _gemcore.cMONO_Prg_get
    def __init__(self, *args): 
        this = _gemcore.new_cMONO(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _gemcore.delete_cMONO
    __del__ = lambda self : None;
    def clr_Prg(self): return _gemcore.cMONO_clr_Prg(self)
    def get_Prg(self, *args): return _gemcore.cMONO_get_Prg(self, *args)
    def loglikelihood(self): return _gemcore.cMONO_loglikelihood(self)
    def init_Prg(self, *args): return _gemcore.cMONO_init_Prg(self, *args)
    def init_ENANMN(self): return _gemcore.cMONO_init_ENANMN(self)
    def rand_V(self): return _gemcore.cMONO_rand_V(self)
    def moment_V(self): return _gemcore.cMONO_moment_V(self)
    def init_V(self, *args): return _gemcore.cMONO_init_V(self, *args)
    def estep(self): return _gemcore.cMONO_estep(self)
    def mstep(self): return _gemcore.cMONO_mstep(self)
cMONO_swigregister = _gemcore.cMONO_swigregister
cMONO_swigregister(cMONO)


def showuum(*args):
  return _gemcore.showuum(*args)
showuum = _gemcore.showuum
# This file is compatible with both classic and new-style classes.

