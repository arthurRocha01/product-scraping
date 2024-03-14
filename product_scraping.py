import pyscraper
import sys

def main():
    if len(sys.argv) != 3 and len(sys.argv) != 4:
        print('Usage: python product_scraping.py <quantidade de produtos> <tempo de espera> <número de raspagem>')
        sys.exit(1)

    quantity_products = int(sys.argv[1])
    wait_time = float(sys.argv[2])
    
    scraper = pyscraper.Scraper(quantity_products, wait_time)
    scraper.run()

if __name__ == '__main__':
    main()
