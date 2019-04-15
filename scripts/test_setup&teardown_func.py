import pytest


# 以下为函数级别的setup、teardown方法的使用，每一次函数的调用都会先调用他们
def test_login():
    print('正在登陆')


def test_click():
    print('点击成功')


def test_move():
    print('移动成功')


def test_qwe():
    print('是否会执行')


# 这个方法在执行每个方法之前，都会先执行一遍
def setup():
    print('前置方法')


def teardown():
    print('后置方法')


# if __name__ == '__main__':
#     pytest.main(["-s", "test_setup&teardown_func.py"])
