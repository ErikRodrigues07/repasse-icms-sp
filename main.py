from Database.connection import get_connection
from Repository.repasse_repository import RepasseRepository
from Service.repasse_service import RepasseService
from Scraper.repasse_scraper import RepasseScraper

def main():
    conn = get_connection()

    repository = RepasseRepository(conn)
    service = RepasseService(repository)
    scraper = RepasseScraper(service)

    scraper.executar()

    conn.close()

if __name__ == "__main__":
    main()