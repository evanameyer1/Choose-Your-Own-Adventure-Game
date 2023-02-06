try:
    from pycode.gui import core
    class TestMain(object):
        @classmethod
        def setup_class(cls):
            pass

        def test_something(self):
            pass


        @classmethod
        def teardown_class(cls):
            pass

except ImportError:
    import sys
    e = sys.exc_info()[1]
    if not "tkinter" in e.message or not "ttk" in e.message:
        raise

