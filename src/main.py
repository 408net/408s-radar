from playwright.sync_api import sync_playwright

from config.chaos_cards import CATEGORY_URLS
from radar.chaos_cards import get_category_products


def product_is_relevant(
    product_name: str,
    category_name: str,
) -> bool:
    """Keep only the product types your group wants."""

    name = product_name.lower()

    if category_name == "etbs":
        return (
            "elite trainer box" in name 
            and "combo" not in name
            )

    if category_name == "gift_tins":
        return True

    if category_name == "booster_bundles":
        return "booster bundle" in name

    return False


def main() -> None:
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        page = browser.new_page()

        all_products: list[dict[str, str]] = []

        for category_name, category_url in CATEGORY_URLS.items():
            print(f"\nChecking category: {category_name}")

            products = get_category_products(
                page=page,
                category_url=category_url,
                category_name=category_name,
            )

            relevant_products = [
                product
                for product in products
                if product_is_relevant(
                    product["name"],
                    category_name,
                )
            ]

            all_products.extend(relevant_products)

            print(f"Found {len(relevant_products)} relevant products.")

            for product in relevant_products:
                print(f"- {product['name']}")
                print(f"  {product['url']}")

        print(f"\nTotal relevant products found: {len(all_products)}")
        
        browser.close()


if __name__ == "__main__":
    main()