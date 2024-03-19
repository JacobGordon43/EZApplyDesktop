import actions as AC
import insert

def test_browser_error():
    result = AC.handle_browser("Not a browser option", "path")
    if result == 15:
        return True
    else:
        return False

if test_browser_error:
    print("Browser Error functionality: Successful")

def test_browser_opens():
    link = "https://www.youtube.com/"
    driver = AC.handle_browser("Chrome", "path")
    driver.get(link)
    return driver.current_url == link

if test_browser_opens:
    print("Browser opening functionality: Successful")