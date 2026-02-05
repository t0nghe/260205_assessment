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


## Notes

- 0000320193   APPLE INC.   
- Legal name of Meta is: Meta Platforms, Inc. 0001326801
- Alphabet Inc. 0001652044
- Amazon.com, Inc. 0001018724
- Netflix, Inc. 0001065280
- There are many registered entities affiliated with Goldman Sachs. Two of them bear the name "Goldman Sachs Group, Inc.". The one at 200 West St has more filings.
    - Goldman Sachs Group, Inc.  (200 West St, NY, NY) 0000886982      
    - Goldman Sachs Group, Inc.  (85 BROAD ST, NEW YORK) 0000904571
