import pytest
"""
pytest提供了:
    模块级（setup_module/teardown_module）开始于模块始末，全局的
    函数级（setup_function/teardown_function）只对函数用例生效（不在类中）
    类级（setup_class/teardown_class）只在类中前后运行一次(在类中)
    方法级（setup_method/teardown_method）开始于方法始末（在类中）
"""
# 多个测试用例 只执行一次 setup 和 teardown
class TestPy02:

    def setup_class(self):
        print("\n-----setup_class")

    def test_py01(self):
        print("-----test_py01")
        assert 2 > 1

    def test_py02(self):
        print("-----test_py02")
        assert 3 == 1

    def test_py03(self):
        print("-----test_py03")
        assert 0 < 1

    def teardown_class(self):
        print("\n-----teardown_class")

