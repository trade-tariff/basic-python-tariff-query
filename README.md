# Basic Python project to access the Online Trade Tariff API

## Implementation steps

- Create and activate a virtual environment, e.g.

  `python3 -m venv venv/`

  `source venv/bin/activate`

## Environment variable settings:

- Make a copy of .env.sample, named .env

- Use the following entries:
  - ```api_url_pattern_basic="https://www.trade-tariff.service.gov.uk/api/v2/commodities/{commodity}"```
  - ```api_url_pattern_filtered="https://www.trade-tariff.service.gov.uk/api/v2/commodities/{commodity}?filter[geographical_area_id]={geographical_area_id}"```

Respectively, these URLs are for:

- a commodity API URL with no country filter
- a commodity API URL with a specified country filter


## Installation

- Install necessary Python modules via `pip3 install -r requirements.txt`
- Install dev Python modules via `pip3 install -r requirements_dev.txt`

## Usage

To process a commodity code API with no country restriction:

`python3 process_commodity.py 8716109800`

To process a commodity code API with a country restriction:

`python3 process_commodity.py 8716109800 FR`

