from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable

import requests

from config import USER_AGENT, SEC_SUBMISSIONS_BASE_URL, SEC_ARCHIVES_BASE_URL


@dataclass(frozen=True)
class Filing:
	cik: str
	accession_number: str
	form: str
	filing_date: str
	report_date: str | None
	primary_document: str
	filing_url: str


def _normalize_cik(cik: str | int) -> str:
	cik_str = str(cik).strip()
	if not cik_str.isdigit():
		raise ValueError("CIK must be numeric")
	if len(cik_str) > 10:
		raise ValueError("CIK must be 10 digits or fewer")
	return cik_str.zfill(10)


def _build_filings_from_recent(
	cik: str,
	recent: dict,
	forms: Iterable[str],
) -> list[Filing]:
	form_set = set(forms)
	accession_numbers = recent.get("accessionNumber", [])
	form_types = recent.get("form", [])
	filing_dates = recent.get("filingDate", [])
	report_dates = recent.get("reportDate", [])
	primary_documents = recent.get("primaryDocument", [])

	filings: list[Filing] = []
	cik_for_path = str(int(cik))
	for index, form in enumerate(form_types):
		if form not in form_set:
			continue
		accession_number = accession_numbers[index]
		accession_no_dashes = accession_number.replace("-", "")
		primary_document = primary_documents[index]
		report_date = report_dates[index] or None
		filing_url = (
			f"{SEC_ARCHIVES_BASE_URL}/{cik_for_path}/"
			f"{accession_no_dashes}/{primary_document}"
		)
		filings.append(
			Filing(
				cik=cik,
				accession_number=accession_number,
				form=form,
				filing_date=filing_dates[index],
				report_date=report_date,
				primary_document=primary_document,
				filing_url=filing_url,
			)
		)

	return filings


def fetch_10k_filings(
	cik: str | int,
	*,
	include_amended: bool = True,
	max_results: int | None = None,
	timeout: float = 30.0,
	session: requests.Session | None = None,
) -> list[Filing]:
	"""Fetch recent 10-K filings for a given CIK using the SEC submissions API."""
	normalized_cik = _normalize_cik(cik)
	forms = ["10-K"]
	if include_amended:
		forms.append("10-K/A")

	url = f"{SEC_SUBMISSIONS_BASE_URL}/CIK{normalized_cik}.json"
	headers = {
		"User-Agent": USER_AGENT,
		"Accept-Encoding": "gzip, deflate",
	}

	client = session or requests.Session()
	response = client.get(url, headers=headers, timeout=timeout)
	response.raise_for_status()
	payload = response.json()
	recent = payload.get("filings", {}).get("recent", {})

	filings = _build_filings_from_recent(normalized_cik, recent, forms)
	if max_results is not None:
		return filings[:max_results]
	return filings

