from playwright.sync_api import Page, expect
import re


def test_google_search(page: Page):
    """Open Google and search for 'Sudhir Bagi S'."""
    # Navigate to Google (English) to reduce localized consent dialogs
    page.goto("https://www.google.com/?hl=en")

    # Try to accept a consent dialog if it appears (common in EU flows)
    try:
        consent_button = page.get_by_role("button", name=re.compile(r"agree|accept", re.I))
        if consent_button.is_visible():
            consent_button.click()
    except Exception:
        # If the consent button isn't present or interaction fails, continue anyway
        pass

    # Locate the search box, type the query, and submit
    search_input = page.locator("input[name='q']")
    search_input.fill("Sudhir Bagi S")
    search_input.press("Enter")

    # Wait for results: verify the page title contains the search query
    expect(page).to_have_title(re.compile(r"Sudhir Bagi S", re.I))
