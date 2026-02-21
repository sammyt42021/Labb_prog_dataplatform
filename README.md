# Labb_prog_dataplatform

This lab implements a small ETL pipeline where product data is ingested from a CSV file, cleaned and validated, and then exported into structured output files for analysis.

## Approach

Extract product data from products.csv using Pandas.

Inspect raw data before transformation.

Clean string columns (remove whitespace, normalize casing).

Convert numeric and date columns safely using pd.to_numeric() and pd.to_datetime().

Flag potential data issues:

Missing currency

Missing price

Zero price

Negative price

Extremely high price

Define rejection rules for impossible values.

Separate valid and rejected records.

Generate required analytics summary file.

Generate bonus price analysis and rejected products files.

Export processed results to the outputs/ folder.

Extract product-level insights such as most expensive and cheapest product using sorting and aggregation.


## ETL Explanation

Extract
Read data from products.csv using pd.read_csv().

Transform
Clean and normalize data, convert data types, flag errors, and apply business rules.

Load
Save processed datasets to new CSV files:

analytics_summary.csv

price_analysis.csv (bonus)

rejected_products.csv (bonus)

Ingest → Storage → Transform → Access

Ingest – Reading CSV data into a Pandas DataFrame.

Storage – Data stored temporarily in memory (DataFrame).

Transform – Data cleaning, validation, and analysis.

Access – Exported CSV files used for reporting or further processing.

## Packages & Dependencies

pandas
Used for data ingestion, transformation, validation, analysis, and CSV export.

Python standard library
Used for script execution and file handling.

Dependencies are managed using a virtual environment (venv) and listed in requirements.txt.

Technologies Mentioned in Theory

Pandas – Data manipulation library for structured data processing.

Psycopg3 – PostgreSQL adapter for connecting Python to databases.

Pydantic (bonus concept) – Used for schema validation and enforcing data integrity.