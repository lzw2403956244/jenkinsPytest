import pytest

# @pytest.mark.skip 跳过测试方法

class TestPy06:

    def setup_class(self):
        print("\n-----setup_class")

    # 无条件跳过
    @pytest.mark.skip()
    def test_py00(self):
        print("-----test_py00")
        assert True

    # 无条件跳过
    @pytest.mark.skipif()
    def test_py01(self):
        print("-----test_py01")
        assert True

    #条件为真时跳过
    @pytest.mark.skipif(3 == 1, reason="条件为真时跳过")
    def test_py02(self):
        print("-----test_py02")
        assert 3 == 1

    # 标记为失败,run默认True执行一次,结果为断言 xpass xfail
    @pytest.mark.xfail(run=False)
    def test_py03(self):
        print("\n-----test_py03")
        assert 1 > 2

    @pytest.mark.xfail(4 > 2, reason="条件为真时标记为失败")
    def test_py04(self):
        print("\n-----test_py04")
        assert 4 > 2

    def teardown_class(self):
        print("\n-----teardown_class")

