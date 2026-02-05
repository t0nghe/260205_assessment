from __future__ import annotations

from pathlib import Path

from playwright.sync_api import sync_playwright


def save_page_as_pdf(
	url: str,
	output_path: str | Path,
	*,
	wait_until: str = "networkidle",
	timeout: int = 30000,
) -> Path:
	"""Save a webpage as PDF using Playwright Chromium.
	
	Args:
		url: The URL to render and save.
		output_path: Where to save the PDF file.
		wait_until: Event to wait for ("load", "domcontentloaded", or "networkidle").
		timeout: Timeout in milliseconds.
	
	Returns:
		Path to the saved PDF file.
	"""
	output_path = Path(output_path)
	output_path.parent.mkdir(parents=True, exist_ok=True)
	print(output_path)
	
	with sync_playwright() as p:
		browser = p.chromium.launch()
		page = browser.new_page()
		page.goto(url, wait_until=wait_until, timeout=timeout)
		page.pdf(path=str(output_path))
		browser.close()
	
	return output_path
