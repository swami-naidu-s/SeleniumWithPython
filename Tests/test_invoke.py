def test_case1(pages):
    print(pages.driver.title)
    pages.driver.switch_to.alert.accept()