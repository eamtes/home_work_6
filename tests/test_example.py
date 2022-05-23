from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from css_selectors import Register_Page, Main_Page, Catalog_Page, Cart_Product_Page, Login_Page


def test_main_page(drivers):
    drivers.get("http://192.168.1.74:8081/")
    assert WebDriverWait(drivers, 0.5).until(EC.visibility_of_element_located(Main_Page.IMG_MACKBOOK))
    assert WebDriverWait(drivers, 0.5).until(EC.visibility_of_element_located(Main_Page.IMG_IPHONE))
    assert WebDriverWait(drivers, 0.5).until(EC.visibility_of_element_located(Main_Page.SEARCH))
    assert WebDriverWait(drivers, 0.5).until(EC.visibility_of_element_located(Main_Page.CART_TOTAL))
    assert WebDriverWait(drivers, 0.5).until(EC.visibility_of_element_located(Main_Page.LINK_TEXT_OPENCART))


def test_catalog_page(drivers):
    drivers.get("http://192.168.1.74:8081/desktops")
    assert WebDriverWait(drivers, 0.5).until(EC.visibility_of_element_located(Catalog_Page.INPUT_LIMIT))
    assert WebDriverWait(drivers, 0.5).until(EC.visibility_of_element_located(Catalog_Page.INPUT_SORT))
    assert WebDriverWait(drivers, 0.5).until(EC.visibility_of_element_located(Catalog_Page.LIST_VIEV))
    assert WebDriverWait(drivers, 0.5).until(EC.visibility_of_element_located(Catalog_Page.GRID_VIEV))
    assert WebDriverWait(drivers, 0.5).until(EC.visibility_of_element_located(Catalog_Page.COLUMN_LEFT))


def test_cart_product_page(drivers):
    drivers.get("http://192.168.1.74:8081/desktops/hp-lp3065")
    assert WebDriverWait(drivers, 0.5).until(EC.visibility_of_element_located(Cart_Product_Page.DOT))
    assert WebDriverWait(drivers, 0.5).until(EC.visibility_of_element_located(Cart_Product_Page.LINK_HP))
    assert WebDriverWait(drivers, 0.5).until(EC.visibility_of_element_located(Cart_Product_Page.BUTTON_CART))
    assert WebDriverWait(drivers, 0.5).until(EC.visibility_of_element_located(Cart_Product_Page.INPUT_OPTION_255))
    assert WebDriverWait(drivers, 0.5).until(EC.visibility_of_element_located(Cart_Product_Page.BUTTON_ONCLICK_COMPARE))


def test_login_page(drivers):
    drivers.get("http://192.168.1.74:8081/index.php?route=account/login")
    assert WebDriverWait(drivers, 0.5).until(EC.visibility_of_element_located(Login_Page.LINK_REGISTER))
    assert WebDriverWait(drivers, 0.5).until(EC.visibility_of_element_located(Login_Page.INPUT_LOGIN))
    assert WebDriverWait(drivers, 0.5).until(EC.visibility_of_element_located(Login_Page.PLACEHOLDER_MAIL))
    assert WebDriverWait(drivers, 0.5).until(EC.visibility_of_element_located(Login_Page.PLACEHOLDER_PASSWORD))
    assert WebDriverWait(drivers, 0.5).until(EC.visibility_of_element_located(Login_Page.LINK_FORGOTTEN))


def test_register_page(drivers):
    drivers.get("http://192.168.1.74:8081/index.php?route=account/register")
    assert WebDriverWait(drivers, 0.5).until(EC.visibility_of_element_located(Register_Page.SUBSCRIBE_YES))
    assert WebDriverWait(drivers, 0.5).until(EC.visibility_of_element_located(Register_Page.SUBSCRIBE_NO))
    assert WebDriverWait(drivers, 0.5).until(EC.visibility_of_element_located(Register_Page.CHECK_BOX))
    assert WebDriverWait(drivers, 0.5).until(EC.visibility_of_element_located(Register_Page.BUTTON_CONTINUE))
    assert WebDriverWait(drivers, 0.5).until(EC.visibility_of_element_located(Register_Page.LINK_PRIVACY_POLICY))
