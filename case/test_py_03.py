import pytest

# 插件 pytest-ordering 可以按照您指定的任何顺序运行测试
# 0 的优先级最高
# 正数 和 负数： 值越小优先级越高
# 正数优先于负数
# 不能用于非test开头的方法

class TestPy03:

    def setup_class(self):
        print("\n-----setup_class")

    @pytest.mark.run(order=-1)
    def test_py01(self):
        print("-----test_py01")
        assert 2 > 1

    @pytest.mark.run(order=3)
    def test_py02(self):
        print("-----test_py02")
        assert 3 == 1

    @pytest.mark.run(order=2)
    def test_py03(self):
        print("-----test_py03")
        assert 0 < 1

    @pytest.mark.run(order=1)
    def test_py04(self):
        print("-----test_py04")
        assert 0 == 0

    def teardown_class(self):
        print("\n-----teardown_class")

