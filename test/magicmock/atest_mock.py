# coding=utf-8

import amodule

if __name__ == '__main__':
    from mock import MagicMock
    thing = amodule.AClass()

    # method方法替换成MagicMock实例
    # 这里传入参数指定了return_value，因此调用MagicMock伪造的method方法，将会返回3！
    thing.method = MagicMock(return_value=3)
    print thing.method('an_arg')

    # assert_called_with 即验证，我们最近一次调用method方法，是通过下面的参数来调用的
    # 显然不是:( 因此这行会报错
    print thing.method.assert_called_with('others')
