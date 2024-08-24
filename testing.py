import pytest 

def test_1():
    assert 1+1==2

# pip install pytest-json-report
# pytest -s -v --json-report --json-report-file=<.json> <.py>
#-v:exec status
# -s: print val

# pip install allure-pytest
# view for layman
# exec test: pytest <.py> --alluredir <tmp dir> 
# gen table: allure generate <tmp dir> -o <exp dir> --clean



# cannot check other errors in a with once an error detected,
# need to write outta with.

@pytest.mark.skip(reason="Test case to be skipped")
def raise_error():
    raise IndexError("ERROR on Index")
def test_error():
    with pytest.raises(IndexError):
        raise_error()
    assert 1+1==3


# TDD 3A principle: Arrange, Act, Assert
# Arrange: write test func (explanans) first, not func to be tested (explanandum 
# exec explanans
# Act: write explanandum
# Assert
# optimise explanandum

def mulNum(_1: int, _2: int) -> int:
    return _1 / _2

def test_mulNum():
    # arrange:
    _1=12
    _2=40
    expect=480
    
    # act
    res = mulNum(_1,_2)

    # assert
    assert res == expect

# Selenium
# pip install selenium, webdriver_manager

import time
from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

def create_webdriver() -> Chrome:
    opt = Options()
    opt.add_argument("--headless")
    opt.add_argument("--start-maximized")

    driver = Chrome(ChromeDriverManager().install(), options=opt)
    return driver


url = "https://reddit.com"
driv = create_webdriver()
driv.get(url=url)
time.sleep(10)
driv.quit()

# find HTML elements
def find_elem():
    driv = create_webdriver()
    driv.get(url=url)

    #single 
    data= WebDriverWait(driv, 10).until( ec.presence_of_element_located
    ((By.CSS_SELECTOR, "div.b-ent")))
    print(data.text)

    #multi
    datas= WebDriverWait(driv, 10).until( ec.presence_of_all_elements_located
    ((By.CSS_SELECTOR, "div.b-ent")))
    [print(tmp.text) for tmp in datas]

@pytest.fixture(name="driver")
def driver_fixture() -> Chrome:
    opt = Options()
    opt.add_argument("--headless")
    opt.add_argument("--start-maximized")
    opt.add_argument(f"user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                     f"AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36")

    driver = Chrome(ChromeDriverManager().install(), options=opt)
    yield driver
    driver.quit()

def test_url(driver: Chrome):
    driver.get(url=url)
    expect_url = "https://reddit.com"
    assert driver.current_url == expect_url
    expect_title = "REDDIT"
    assert driver.title_startswith(expect_title)
    question_h2_element = driver.find_element(By.CSS_SELECTOR, "h2.tab-title")
    expect_text = "r/classics"
    assert question_h2_element.text == expect_text
    