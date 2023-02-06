class Decorator:
    def __new__(self,*args,**kwargs):
        self.decoree = None
        self.newargs = args
        self.newkwargs = kwargs
        self.decorators = {}
        if "decorators" in self.newkwargs:
            self.decorators = self.newargs["decorators"]
        if args:
            if isinstance(args[0],type):
                self.decoree = args[0]
            if callable(args[0]):
                if len(args) == 1 and len(kwargs) == 0:
                    return args[0]
            else:
                pass
        return self

    def __init__(self,*args,**kwargs):
        self.decoree = None
        self.initargs = args
        self.initkwargs = kwargs
        if args and callable(args[0]):
            self.decoree = args[0]

    def __call__(self, *args, **kwargs):
        if args and callable(args[0]):
            self.decoree = args[0]
            if isinstance(self.decoree,type):
                return self.create_wrapping_class(self.decoree, self.decorators)
            return self.decoree
        elif self.decoree:
            if isinstance(self.decoree,type):
                return self.create_wrapping_class(args[0],self.decorators)(*args,**kwargs)
            return self.decoree(*args,**kwargs)

    @staticmethod
    def create_wrapping_class(cls,decorators):
        from future.utils import with_metaclass
        class MetaNewClass(type):
            def __repr__(self):
                return repr(cls)

        class NewClass(with_metaclass(MetaNewClass,cls)):
            def __init__(self,*args,**kwargs):
                self.__instance = cls(*args,**kwargs)
            "This is the overwritten class"
            def __getattribute__(self, attr_name):
                if attr_name == "__class__":
                    return cls
                obj = super(NewClass, self).__getattribute__(attr_name)
                if hasattr(obj, '__call__'):
                    if attr_name in decorators:
                        for decorator in decorators:
                            obj = decorator(obj)
                    elif "*" in decorators:
                        for decorator in decorators:
                            obj = decorator(obj)
                    return obj
                return obj
            def __repr__(self):
                return repr(self.__instance)
        return NewClass

def lcs(a, b):
    lengths = [[0 for j in range(len(b)+1)] for i in range(len(a)+1)]
    # row 0 and column 0 are initialized to 0 already
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            if x == y:
                lengths[i+1][j+1] = lengths[i][j] + 1
            else:
                lengths[i+1][j+1] = max(lengths[i+1][j], lengths[i][j+1])
    # read the substring out from the matrix
    result = ""
    x, y = len(a), len(b)
    while x != 0 and y != 0:
        if lengths[x][y] == lengths[x-1][y]:
            x -= 1
        elif lengths[x][y] == lengths[x][y-1]:
            y -= 1
        else:
            assert a[x-1] == b[y-1]
            result = a[x-1] + result
            x -= 1
            y -= 1
    return result
