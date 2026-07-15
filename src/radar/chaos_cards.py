from urllib.parse import urljoin

from playwright.sync_api import Page


BASE_URL = "https://www.chaoscards.co.uk"


def extract_product_name(card_text: str) -> str | None:
    """Extract the product name from a Chaos Cards product card."""

    lines = [
        line.strip()
        for line in card_text.splitlines()
        if line.strip()
    ]

    for line in lines:
        if line.lower().startswith("pokemon"):
            return line

    return None


def get_category_products(
    page: Page,
    category_url: str,
    category_name: str,
) -> list[dict[str, str]]:
    """Collect unique product names and URLs from a category page."""

    page.goto(category_url, wait_until="domcontentloaded")

    product_links = page.locator('a[href^="/prod/"]')

    products_by_url: dict[str, dict[str, str]] = {}

    for index in range(product_links.count()):
        link = product_links.nth(index)

        href = link.get_attribute("href")
        card_text = link.inner_text().strip()

        if not href or not card_text:
            continue

        product_name = extract_product_name(card_text)

        if not product_name:
            continue

        product_url = urljoin(BASE_URL, href)

        products_by_url[product_url] = {
            "name": product_name,
            "url": product_url,
            "category": category_name,
        }

    return list(products_by_url.values())


def get_product_name(page: Page) -> str:
    """Return the product name from a product page."""

    return page.locator("h1#prod_title").inner_text().strip()


def get_product_status(page: Page) -> tuple[bool, str]:
    """Return whether the product is a preorder and its stock status."""

    stock_sections = page.locator(".product-section--stock")

    all_stock_text = " ".join(
        stock_sections.all_inner_texts()
    ).lower()

    is_preorder = "pre-order" in all_stock_text

    stock_elements = page.locator(
        ".product-section--stock .product-detail__content"
    )

    stock_status = "Unknown"

    for index in range(stock_elements.count()):
        text = stock_elements.nth(index).inner_text().strip()
        normalised = text.lower().rstrip(".")

        if normalised == "in stock":
            stock_status = "In stock"

        elif normalised == "out of stock":
            stock_status = "Out of stock"

    return is_preorder, stock_status