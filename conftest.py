import pytest
import allure
from pathlib import Path
from playwright.sync_api import sync_playwright


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="browser selection: chrome, firefox or edge"
    )


@pytest.fixture(scope="session")
def playwright_instance():
    with sync_playwright() as playwright:
        yield playwright


@pytest.fixture(scope="function")
def page(playwright_instance, request):
    # Create output dirs
    videos_dir = Path("videos")
    videos_dir.mkdir(exist_ok=True)
    screenshots_dir = Path("screenshots")
    screenshots_dir.mkdir(exist_ok=True)

    # Launch browser in headed mode
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        browser = playwright_instance.chromium.launch(headless=False, slow_mo=300)
    elif browser_name == "firefox":
        browser = playwright_instance.firefox.launch(headless=False, slow_mo=300)
    elif browser_name == "edge":
        browser = playwright_instance.chromium.launch(channel="msedge", headless=False, slow_mo=300)
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")
    context = browser.new_context(record_video_dir=str(videos_dir))
    page = context.new_page()

    yield page

    # On test failure, capture screenshot and video
    test_name = request.node.name
    if request.node.rep_call.failed:
        screenshot_path = screenshots_dir / f"{test_name}.png"
        page.screenshot(path=str(screenshot_path))
        allure.attach.file(str(screenshot_path), name="Screenshot", attachment_type=allure.attachment_type.PNG)

        video_path = page.video.path()
        page.close()
        allure.attach.file(str(video_path), name="Video", attachment_type=allure.attachment_type.MP4)
    else:
        page.close()

    context.close()
    browser.close()


# Hook to check test result
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
