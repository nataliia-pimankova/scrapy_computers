test scrapy project for educational purposes

goes by a list of items, gets every product and collect info to ComputerItem

with pagination by arrow right next page link

Output: items.csv

Problems:

- Not all info exists on a list page - Resolved
- some fields are not presented in a resulting table (some graphics card in a link tag) - Resolved
- price in a no number format - Resolved
- pagination does not work properly (only 4 pages)
- [scrapy.spidermiddlewares.httperror] INFO: Ignoring response <428 https://www.komputronik.pl/product/742511/komputronik-infinity-x510-m2-.html>: HTTP status code is not handled or not allowed