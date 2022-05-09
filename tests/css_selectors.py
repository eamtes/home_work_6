from selenium.webdriver.common.by import By


class Main_Page:
    IMG_MACKBOOK = (By.CSS_SELECTOR, "img[title*=MacBook]")
    IMG_IPHONE = (By.CSS_SELECTOR, "img[title*=iPhone]")
    SEARCH = (By.NAME, "search")
    CART_TOTAL = (By.ID, "cart-total")
    LINK_TEXT_OPENCART = (By.LINK_TEXT, "OpenCart")


class Catalog_Page:
    INPUT_LIMIT = (By.ID, "input-limit")
    INPUT_SORT = (By.ID, "input-sort")
    LIST_VIEV = (By.ID, "list-view")
    GRID_VIEV = (By.ID, "grid-view")
    COLUMN_LEFT = (By.ID, "column-left")


class Cart_Product_Page:
    DOT = (By.CSS_SELECTOR, "[data-original-title='Add to Wish List']")
    LINK_HP = (By.CSS_SELECTOR, "a[href$='hewlett-packard']")
    BUTTON_CART = (By.CSS_SELECTOR, "button#button-cart")
    INPUT_OPTION_255 = (By.CSS_SELECTOR, "#input-option225")
    BUTTON_ONCLICK_COMPARE = (By.CSS_SELECTOR, "button[onclick^='compare']")


class Login_Page:
    LINK_REGISTER = (By.CSS_SELECTOR, "a[href$='register'].btn")
    INPUT_LOGIN = (By.CSS_SELECTOR, "input[value='Login']")
    PLACEHOLDER_MAIL = (By.CSS_SELECTOR, "[placeholder='E-Mail Address']")
    PLACEHOLDER_PASSWORD = (By.CSS_SELECTOR, "[placeholder='Password']")
    LINK_FORGOTTEN = (By.CSS_SELECTOR, "div.form-group>a[href$='forgotten']")


class Register_Page:
    SUBSCRIBE_YES = (By.CSS_SELECTOR, "input[name='newsletter'][value='1']")
    SUBSCRIBE_NO = (By.CSS_SELECTOR, "input[name='newsletter'][value='0']")
    CHECK_BOX = (By.CSS_SELECTOR, "input[name='agree'][value='1']")
    BUTTON_CONTINUE = (By.CSS_SELECTOR, "input[value='Continue']")
    LINK_PRIVACY_POLICY = (By.CSS_SELECTOR, ".agree")
