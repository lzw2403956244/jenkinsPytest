import pytest

# 插件 pytest-rerunfailures 失败重试 可以指定次数
# 命令行：--reruns n # n:重试次数 n+1
# 会重复运行 setup_class teardown_class
# 延迟命令追加：--reruns-delay 2
# 显示摘要命令：-r aR

class TestPy04:

    def setup_class(self):
        print("\n-----setup_class")

    # 失败时，自动重复运行3次
    @pytest.mark.flaky(reruns=3)
    def test_py01(self):
        print("-----test_py01")
        assert 3 == 1

    def test_py02(self):
        print("-----test_py02")
        assert 2 > 1

    # 失败时，自动重复运行2次，每次延迟3秒
    @pytest.mark.flaky(reruns=2, reruns_delay=3)
    def test_py03(self):
        print("-----test_py03")
        assert 0 < 0

    def teardown_class(self):
        print("\n-----teardown_class")

