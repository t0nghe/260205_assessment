# Assessment (5 Feb 2026)

## Goal

The goal of this project is to fetch 10-K reports filed with the SEC by Apple, Meta, Alphabet, Amazon, Netflix, Goldman Sachs and then convert them to PDF files.

## Usage

1. At the project root, run the following command:

(Optional) Start a new virtual environment so the dependencies do not conflict with your global setup:

```bash
pipenv shell
```

Then install dependencies from `requirements.txt` and run the entrypoint of the program `src/main.py`. 

```bash
pip install -r requirements.txt
python src/main.py
```

2. Alternatively, if you prefer `poetry`, you can run the following commands from the project root:

```bash
poetry install
poetry run python src/main.py
```

## Structure

- *api*: Fetch the data from SEC and download HTML content from the filing.
- *process*: Render the HTML in Chromium using Playwright and export the rendered page to PDF.
- *config.py*: Basic configuration for SEC APIs.
- *main.py*: Main entrypoint of the program.

## How it works

We have a manually defined list of CIK codes for the listed companies. When the program starts, `main.py` iterates over the list of CIK codes. 

For each entry, we then make a query using `fetch_10k_filings` function to fetch a list of available filings. There can be multiple filings for each company. By default we are only fetching the first. This can be changed using the `max_result` argument.

Each filing entry looks something like this:

```python
[Filing(cik='0000886982', accession_number='0000886982-25-000005', form='10-K', filing_date='2025-02-27', report_date='2024-12-31', primary_document='gs-20241231.htm', filing_url='https://www.sec.gov/Archives/edgar/data/886982/000088698225000005/gs-20241231.htm')]
```

With this entry, we then fetch the HTML content by following the `filing_url`. To show courtesy, we follow the instruction of SEC by providing a user agent signature declaring we are an individual investor, with an email address provided.

Next, in `render.py`, we use `save_page_as_pdf` function to render the HTML content headlessly using Playwright and its Chromium extension. We subsequently save the rendered page as a PDF file in the output directory. 

Theoretically we can instruct Playwright to navigate to the `file_url` shown above. In reality, such requests would be blocked for using an “undeclared automated tool”.

Directly rendering the HTML markup works, but not without downsides. Notably, embedded media, including company logos and charts are missing. An alternative could be parsing the HTML using BeautifulSoup and requesting media files separately.

## Possible extensions

There are many ways to extend this program.

One useful feature to add is running NER on the content to read numerical data from the file. This will be helpful for downstream analytical, reporting or trading tasks.

It will be helpful if this script is deployed as a cron job to fetch latest filings periodically. Companies submit their 10-K filings by the end of their fiscal year, which can be any month in the calendar year.

Adding support for RESTful API for internal use will also be helpful.



