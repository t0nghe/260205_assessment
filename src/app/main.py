from api.client import download_filing_html
from process.render import save_page_as_pdf

def main():
    html_content = download_filing_html("https://www.sec.gov/Archives/edgar/data/320193/000032019325000079/aapl-20250927.htm")
    save_page_as_pdf(html_content, "../output/aapl-20250927.pdf")

if __name__ == "__main__":
    main()