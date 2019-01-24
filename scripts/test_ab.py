import allure
def test_a():
    print('aaa')
    assert 1

@allure.step(title='测试登录的流程')
def test_b():
    allure.attach('登录','输入用户名')
    print('bbb')
    allure.attach('登录','输入密码')
    print('ccc')
    allure.attach('登录','点击登录')
    assert 1








