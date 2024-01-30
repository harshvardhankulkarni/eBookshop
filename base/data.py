import requests
from bs4 import BeautifulSoup


def scrape_genra():
    response = requests.get('https://selfpublishing.com/list-of-book-genres/')

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        genra = []
        for country in soup.select(selector=f'.et_pb_post_content_0_tb_body h{3}'):
            genra.append(country.text.split('.')[1].strip())
        for country in soup.select(selector=f'.et_pb_post_content_0_tb_body h{4}'):
            genra.append(country.text.split('.')[1].strip())
        return list(set(genra))

    else:
        print(f"Error: Unable to retrieve the webpage. Status code: {response.status_code}")
        return None


def scrape_languages():
    response = requests.get('https://guidely.in/blog/languages-of-india')

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        languages = []
        for country in soup.select(selector=f'.maincontent ol span'):
            if len(languages) != 22:
                languages.append(country.text)
        languages.append('English')
        return languages

    else:
        print(f"Error: Unable to retrieve the webpage. Status code: {response.status_code}")
        return None


# from base.data import scrape_genra, scrape_languages
# from base.models import Genra, Language

# for genra in scrape_genra():
#     Genra.objects.create(genra=genra)

# for language in scrape_languages():
#     Language.objects.create(language=language)
