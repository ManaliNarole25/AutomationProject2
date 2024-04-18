import pytest

from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope='class')
def setup(request):
    browser_name = request.config.getoption("--browser_name")

    if browser_name == 'chrome':
        driver = webdriver.Chrome()
    elif browser_name == "firefox":
        driver = webdriver.Firefox
    elif browser_name == "edge":
        driver = webdriver.Edge

    else:
        print("Headless mode")
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("headless")
        driver = webdriver.Chrome(options=chrome_options)

    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()

    request.cls.driver = driver
    yield
    driver.close()

    def pytest_metadata(metadata):
        metadata["Project Name"] = "Shopping site"
        metadata["Environment"] = "QA Environment"
        metadata["Module"] = "User Profile"
        metadata["Tester"] = "Manali"
        metadata.pop("Plugins", None)
