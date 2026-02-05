# Test (Feb 5)

## Goal

The goal of this project is to fetch 10-K reports filed with the SEC by Apple, Meta, Alphabet, Amazon, Netflix, Goldman Sachs.

The immediate goal of this task is to fetch the reports from these companies and convert them to PDFs. 

## Consideration

10-K reports are submitted annually. There is no need to provide the data with WebSocket. 

## Structure

- *api*: Fetch the data from SEC.
- *convert*: Convert fetched data to PDFs.
- *storage*: Save the PDF files to the disk.
- *data*: parse data maybe
- *tests*: Unit tests.



