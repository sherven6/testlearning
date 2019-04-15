import pytest
import allure

# 使用类级别的setup、teardown方法

class TestPy:
    def setup_class(self):
        print('类级别的前置方法')

    def teardown_class(self):
        print('类级别的后置方法')

    @pytest.mark.skip(True,reason='done')
    def test_login(self):
        print('正在登陆')
        assert 0

    @allure.step('点击')
    def test_click(self):
        print('点击成功')
        assert 1


    def test_move(self):
        print('移动成功')
        assert 1


    def test_qwe(self):
        print('是否会执行')


# if __name__ == "__main__":
#     pytest.main(["-s", r"--html=./report1.html", "test_setup&teardown_clas.py"])
