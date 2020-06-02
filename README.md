# Covered California Prescription Back-End Files

These files form the work that drives the back-end of the [CoveredCA Prescription Search](http://covered-ca-prescription-search.s3-website-us-west-2.amazonaws.com/) web application.

These files scrape the prescription tables from the insurer's PDF files and write them to CSV/JSON files available for the front-end to consume.

These files have a very unstructured ad-hoc feel to them. This is because the process of extracting the prescription tables was very manual and ad-hoc. In an ideal world, this project should not exist and should be replaced by a data pipeline to the raw data provided by the collection of insurers.

## Get Started

To get started with this project,

```
git clone https://github.com/jviloria96744/covered-ca-prescription-backend.git
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

The files are independent can be run individually to test different operations with the following command, as mentioned above, this project resembles more of a workbench than a deployable set of files.

`python [filename with .py extension]`
