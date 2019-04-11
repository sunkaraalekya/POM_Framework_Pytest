import pytest
import testdata.constants as Dataval
def pytest_addoption(parser):
    parser.addoption("--browser",action="store",default='chrome')

@pytest.fixture(scope='class')
def test_setup(request):
    from selenium import webdriver
    PROXY="localhost:1234"
    chrome_options=webdriver.ChromeOptions()
    chrome_options.add_argument('--proxy-server=%s' % PROXY)


    browser=request.config.getoption("--browser")
    if browser=='chrome':
        driver=webdriver.Chrome(options=chrome_options)
    elif browser=='ff':
        driver=webdriver.Firefox()

    driver.get(Dataval.URL)
    driver.maximize_window()
    driver.implicitly_wait(30)
    request.cls.driver=driver
    yield
    driver.quit()