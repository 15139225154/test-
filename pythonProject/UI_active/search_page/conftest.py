import pytest

#引用login函数
@pytest.fixture()
def login():
    print('123456')

