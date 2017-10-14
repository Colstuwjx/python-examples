# coding=utf-8

import sys
import mymodule


# patched method `Hello`
def Hello():
    print "Hello, Monkey!"


# monkey patch
class monkeypatch(object):
    def __init__(self):
        mymod = self._get_global_module("mymodule")

        # Methods to replace
        self.methods = ('Hello', )
        # Store the original methods
        self.orig_methods = dict(
            (m, mymod.__dict__[m]) for m in self.methods)
        # Monkey patch
        g = globals()
        for m in self.methods:
            # mymod's method has been replaced!
            mymod.__dict__[m] = g[m]

    def _get_global_module(self, mod):
        return sys.modules[mod]

    def __enter__(self):
        return self

    def __exit__(self, *args):
        mymod = self._get_global_module("mymodule")
        # restore the method
        for m in self.methods:
            mymod.__dict__[m] = self.orig_methods[m]


if __name__ == '__main__':
    monkeypatch()

    # under this hood, mymodule's Hello has been monkeypatched.
    mymodule.Hello()
