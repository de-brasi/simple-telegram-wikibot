import wikipediaapi
import langid


def get_info_from_wiki(query: str, language: str) -> str:
    wiki_wiki = wikipediaapi.Wikipedia(language)
    page = wiki_wiki.page(query)
    if page.exists():
        if 'may refer to' in page.summary:
            return page.text
        else:
            return page.summary
    else:
        return "This page was not found"


def get_lang(text: str) -> str:
    return langid.classify(text)[0]     # 0 index is lang type
