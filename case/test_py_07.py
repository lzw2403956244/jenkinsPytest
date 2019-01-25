import pytest

# @pytest.mark.parametrize 参数化
class TestPy07:

    @pytest.mark.parametrize("data", [1,2,3])
    def test_py01(self, data):
        print("-----test_py01")
        print(data)
        assert data != 3

    @pytest.mark.parametrize("data,list",[('a',['a','b','c']),("b",['d','e','f'])])
    def test_py02(self,data,list):
        print("-----test_py02")
        print(data)
        print(list)
        assert data in list

    def test_py03(self):
        print("-----test_py03")
        assert 0 < 1
