from bs4 import BeautifulSoup
import requests


def get_soup() -> BeautifulSoup:
    headers: dict = {
        'User-Agent': 'my user agent'}
    request = requests.get('https://www.bbc.com/news', headers=headers)
    html: bytes = request.content

    # Create Soup
    soup = BeautifulSoup(html, 'html.parser')
    return soup


def get_headlines(soup: BeautifulSoup) -> list[str]:
    headlines: set = set()

    for h in soup.findAll('h3', class_='gs-c-promo-heading__title'):
        headline: str = h.contents[0].lower()
        headlines.add(headline)

    return sorted(headlines)


def check_headlines(headlines: list[str], term: str):
    term_list: list[str] = []
    terms_found: int = 0

    for i, headline in enumerate(headlines, start=1):
        if term.lower() in headline.split(' ') or term.lower()+'?' in headline.split(' '):
            terms_found += 1
            term_list.append(headline)
            print(f'{i}: {headline.capitalize()} <-------------------------- "{term}"')
        else:
            print(f'{i}: {headline.capitalize()}')

    print('-'*15) # Divider
    if terms_found:
        print(f'{term} was mentioned {terms_found} times.')
        print('-'*15)

        for i, headline in enumerate(term_list, start=1):
            print(f'{i}: {headline.capitalize()} <-------------------------- "{term}"')
    else:
        print(f'No matches found for: {term}')
        print('-' * 15)
def main():
    soup: BeautifulSoup = get_soup()
    headlines: list[str] = get_headlines(soup=soup)
    user_input:str = input('Search term: ')
    check_headlines(headlines,user_input)

if __name__ == '__main__':
    main()
