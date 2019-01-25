import pytest

"""
修饰符@pytest.fixture 用于预置处理和重复操作,用于 非 setup 和 teardown
作用域scope:
    function：作用于每个测试方法，每个test运行一次
    class   : 作用于整个类，每个类所有test只运行一次
    module  : 作用于整个模块，每个模块所有test只运行一次
    session : 作用于整个会话，每个会话所有test只运行一次
参数params:
自动运行autouse：设置为True时优先级高于默认值False，一样的条件时以方法名顺序为执行顺序
引用名name：函数引用优先级高于参数引用
"""


# 返回值,引用名为函数名
@pytest.fixture()
def init_config5():
    return "\n-----init_config5"


# 设置参数params
@pytest.fixture(params=['init', 'config', 6])
def init_config6(request):
    return request.param


@pytest.fixture(name='init2')
def init_config2():
    print("\n-----init_config2")


# 在类外引用,不能引用类里面的
@pytest.mark.usefixtures('init2')
class TestPy05:

    def setup_class(self):
        print("\n-----setup_class")

    # 参数引用
    def test_py01(self, init):
        print("-----test_py01")
        assert 2 > 1

    # 函数引用
    @pytest.mark.usefixtures('init')
    def test_py02(self):
        print("-----test_py02")
        assert 3 == 1

    def test_py03(self, init_config5):
        print("-----test_py03")
        print(init_config5)
        assert 'init' in init_config5

    def test_py04(self, init_config6):
        print("-----test_py04")
        print(init_config6)
        assert isinstance(init_config6,str)

    # 设置引用名name
    @pytest.fixture(name='init')
    def init_config1(self):
        print("\n-----init_config1")

    # 设置为自动运行
    @pytest.fixture(autouse=True)
    def init_config3(self):
        print("\n-----init_config3")

    # 设置作用域scope,默认function：
    @pytest.fixture(scope='class', autouse=True)
    def init_config4(self):
        print("\n-----init_config4")

    def teardown_class(self):
        print("\n-----teardown_class")