<div align="center">
<a href="#">
    <img src="assets/images/logo.jpg" alt="Logo" width="80" height="80" />
</a>

<h3 align="center">Gigs By Bob</h3>
<p align="center">
    Bob will send you alerts on discord so that you can place bids on projects faster than other users on freelancer platform.
</p>
</div>

<br />

## Features

- Fetch the products URLs of every medicine.
- Fetch the product URLs by category names.
- Store detailed information of a product with values:
    - Name
    - URL
    - Is Prescription Required
    - Salt Composition
    - Manufacturer Name
    - Discount Price
    - MRP Price
    - Recent Purchase
    - Variants
    - Is Sold Out
    - Is Discontinued
    - Is Banned For Sale
    - Is Not For Sale
    - Is Scraped

<br />

## Built With

[![Python][Python]][Python-url]&nbsp; &nbsp;[![Selenium][Selenium]][Selenium-url]&nbsp; &nbsp;[![Pandas][Pandas]][Pandas-url]


<br />

## Getting Started

Follow the below steps in order to step this project on your local machine.

### Prerequisites

- Make sure you have python version **3.9.5** running on your local machine.

- In case you don't have python installed, go to the official website ([Python.org](https://python.org)) and install it.

### Installation

- Clone repository
```
git clone https://github.com/Guri-X/Proto-1mg-Scraper
```

- Create a virtual environment
```
cd Proto-1mg-Scraper/
python -m venv env
```

- Activate virtual environment
```
source env/bin/activate
```

- Install requirements from **requirements.txt** file
```
pip install -r requirements.txt
```

### Execution

- To fetch the product URLs of a medicines, run the `scrape_urls.py` script:
```
python scrape_urls.py
```

- To scrape the product URLs of a particular category, run the `scrape_category_urls.py` script:
```
python scrape_category_urls.py <category_name> <category_url> <pages_count>
```

- To fetch the details of each product, run the `scrape_data_page.py` script:
```
python scrape_data_page.py
```

<br />

## Contributing

If you would like to improve this project by adding more features, feel free to create a pull request.

## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

## Contact

:star2: Gurvinder Singh - [@Guri_XD](https://twitter.com/Guri_XD)

:email: Email - guri.developer97@gmail.com

:rocket: Project Repo - [https://github.com/Guri-X/Proto-1mg-Scraper](https://github.com/Guri-X/Proto-1mg-Scraper)

<br />

# References

- https://developers.freelancer.com/docs
- https://discordpy.readthedocs.io/en/stable/discord.html