from selenium.webdriver.common.by import By

PRODUCTS = {
    "bike_light": {
        "add": (By.ID, "add-to-cart-sauce-labs-bike-light"),
        "remove": (By.ID, "remove-sauce-labs-bike-light"),
        "display_name": "Sauce Labs Bike Light"
    },
    "backpack": {
        "add": (By.ID, "add-to-cart-sauce-labs-backpack"),
        "remove": (By.ID, "remove-sauce-labs-backpack"),
        "display_name": "Sauce Labs Backpack"
    },
    "fleece_jacket": {
        "add": (By.ID, "add-to-cart-sauce-labs-fleece-jacket"),
        "remove": (By.ID, "remove-sauce-labs-fleece-jacket"),
        "display_name": "Sauce Labs Fleece Jacket"
    },
    "onesie": {
        "add": (By.ID, "add-to-cart-sauce-labs-onesie"),
        "remove": (By.ID, "remove-sauce-labs-onesie"),
        "display_name": "Sauce Labs Onesie"
    },
    "bolt_tshirt": {
        "add": (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt"),
        "remove": (By.ID, "remove-sauce-labs-bolt-t-shirt"),
        "display_name": "Sauce Labs Bolt T-Shirt"
    },
    "red_tshirt": {
        "add": (By.ID, "add-to-cart-test.allthethings()-t-shirt-(red)"),
        "remove": (By.ID, "remove-test.allthethings()-t-shirt-(red)"),
        "display_name": "Test.allTheThings() T-Shirt (Red)"
    }
}