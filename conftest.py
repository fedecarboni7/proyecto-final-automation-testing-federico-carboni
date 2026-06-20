import datetime
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from utils.logger import get_logger


@pytest.fixture(scope="function")
def driver(request):
    logger = get_logger("conftest")
    logger.info(f"Starting test: {request.node.name}")

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=1920,1080")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.maximize_window()

    yield driver

    logger.info(f"Finished test: {request.node.name}")
    driver.quit()


@pytest.fixture
def base_url():
    return "https://www.saucedemo.com"


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Hook para adjuntar screenshots al reporte HTML cuando un test falla."""
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")
        if driver:
            import os
            from datetime import datetime

            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            test_name = item.name
            screenshot_dir = "screenshots"
            os.makedirs(screenshot_dir, exist_ok=True)
            screenshot_path = os.path.join(screenshot_dir, f"{timestamp}_{test_name}.png")

            driver.save_screenshot(screenshot_path)

            abs_screenshot_path = os.path.abspath(screenshot_path)
            from pytest_html import extras
            if hasattr(report, "extras"):
                report.extras.append(extras.image(abs_screenshot_path))
            else:
                report.extras = [extras.image(abs_screenshot_path)]
