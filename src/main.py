import json
from api.client import fetch_10k_filings, download_filing_html
from process.render import save_page_as_pdf
from config import CIK_LIST

def main():
    with open(CIK_LIST, "r") as f:
        ciks = f.read()

    json_data = json.loads(ciks)
    
    for cik_entry in json_data:
        cik = cik_entry["cik"]
        name = cik_entry["legal_name"]
        ticker = cik_entry.get("ticker")
        filings = fetch_10k_filings(cik, max_results=1)
        for filing in filings:
            print(f"Form: {filing.form}, Date: {filing.filing_date}, URL: {filing.filing_url}")
            html_content = download_filing_html(filing)
            output_path = f"./output/{name}_{filing.filing_date}_{filing.form}.pdf"
            save_page_as_pdf(html_content, output_path)
            print(f"Saved PDF to: {output_path}")

if __name__ == "__main__":
    main()