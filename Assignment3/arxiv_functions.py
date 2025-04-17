"""CSCA08 Assignment 3: arxiv.org"""

import copy
from typing import TextIO
from constants import (ID, TITLE, CREATED, MODIFIED, AUTHORS,
                       ABSTRACT, END, SEPARATOR, NameType,
                       ArticleType, ArxivType)

EXAMPLE_ARXIV = {
    '008': {
        'identifier': '008',
        'title': 'Intro to CS is the best course ever',
        'created': '2021-09-01',
        'modified': None,
        'authors': [('Ponce', 'Marcelo'), ('Tafliovich', 'Anya Y.')],
        'abstract': '''We present clear evidence that Introduction to
Computer Science is the best course.'''},
    '031': {
        'identifier': '031',
        'title': 'Calculus is the best course ever',
        'created': None,
        'modified': '2021-09-02',
        'authors': [('Breuss', 'Nataliya')],
        'abstract': '''We discuss the reasons why Calculus I
is the best course.'''},
    '067': {'identifier': '067',
            'title': 'Discrete Mathematics is the best course ever',
            'created': '2021-09-02',
            'modified': '2021-10-01',
            'authors': [('Bretscher', 'Anna'), ('Pancer', 'Richard')],
            'abstract': ('We explain why Discrete Mathematics is the best ' +
                         'course of all times.')},
    '827': {
        'identifier': '827',
        'title': 'University of Toronto is the best university',
        'created': '2021-08-20',
        'modified': '2021-10-02',
        'authors': [('Bretscher', 'Anna'),
                    ('Ponce', 'Marcelo'),
                    ('Tafliovich', 'Anya Y.')],
        'abstract': '''We show a formal proof that the University of
Toronto is the best university.'''},
    '042': {
        'identifier': '042',
        'title': None,
        'created': '2021-05-04',
        'modified': '2021-05-05',
        'authors': [],
        'abstract': '''This is a very strange article with no title
and no authors.'''}
}

EXAMPLE_BY_AUTHOR = {
    ('Ponce', 'Marcelo'): ['008', '827'],
    ('Tafliovich', 'Anya Y.'): ['008', '827'],
    ('Bretscher', 'Anna'): ['067', '827'],
    ('Breuss', 'Nataliya'): ['031'],
    ('Pancer', 'Richard'): ['067']
}


def _parse_article_block(lines: list[str]) -> ArticleType:
    """Return an article dictionary given the list of its raw lines.

    lines: A list of strings representing one article block from the file.
    Assumes the lines follow the arXiv metadata format:
        - line 0: article ID
        - line 1: title or blank
        - line 2: created date or blank
        - line 3: modified date or blank
        - line 4 to blank line: authors (last,first)
        - after blank line: abstract (until END)

    Returns a dictionary with keys:
        ID, TITLE, CREATED, MODIFIED, AUTHORS, ABSTRACT
    """

    article_id = lines[0]
    title = lines[1] if lines[1] else None
    created = lines[2] if lines[2] else None
    modified = lines[3] if lines[3] else None

    authors = []
    i = 4
    while i < len(lines) and lines[i].strip() != '':
        last, first = lines[i].split(',', 1)
        authors.append((last.strip(), first.strip()))
        i += 1

    i += 1
    abstract = '\n'.join(lines[i:]) if i < len(lines) else None

    return {
        ID: article_id,
        TITLE: title,
        CREATED: created,
        MODIFIED: modified,
        AUTHORS: sorted(authors),
        ABSTRACT: abstract
    }


def read_arxiv_file(afile: TextIO) -> ArxivType:
    """Return a dict containing all arxiv information in afile.

    Precondition: afile is open for reading
                  afile is in the format described in the handout.
    """
    result: ArxivType = {}
    content = afile.read().strip()

    if not content:
        return result

    articles_raw = content.split(END + '\n')
    for block in articles_raw:
        lines = block.strip().split('\n')
        if lines and lines[0]:
            article = _parse_article_block(lines)
            result[article[ID]] = article

    return result


def make_author_to_articles(
        id_to_article: ArxivType) -> dict[NameType, list[str]]:
    """Return a dict that maps each author name to a list (sorted in
    lexicographic order) of IDs of articles written by that author,
    based on the information in arxiv data id_to_article.

    >>> make_author_to_articles(EXAMPLE_ARXIV) == EXAMPLE_BY_AUTHOR
    True
    """
    author_to_articles = {}
    for article_id, article_info in id_to_article.items():
        for author in article_info.get(AUTHORS, []):
            author_to_articles.setdefault(author, []).append(article_id)
    for article_list in author_to_articles.values():
        article_list.sort()
    return author_to_articles


def get_coauthors(
       id_to_article: ArxivType, author_name: NameType) -> list[NameType]:
    """Return a list of coauthors of the author specified by author_name in
    arxiv data id_to_article.

    >>> get_coauthors(EXAMPLE_ARXIV, ('Tafliovich', 'Anya Y.'))
    [('Bretscher', 'Anna'), ('Ponce', 'Marcelo')]
    """
    coauthors = set()
    for article in id_to_article.values():
        if author_name in article[AUTHORS]:
            coauthors.update(a for a in article[AUTHORS] if a != author_name)
    return sorted(coauthors)


def get_most_published_authors(id_to_article: ArxivType) -> list[NameType]:
    """Return a sorted list of authors who published the most articles
    in arxiv data id_to_article.

    >>> get_most_published_authors(EXAMPLE_ARXIV)
    [('Bretscher', 'Anna'), ('Ponce', 'Marcelo'), ('Tafliovich', 'Anya Y.')]
    """
    author_to_articles = make_author_to_articles(id_to_article)
    if not author_to_articles:
        return []
    max_count = max(len(articles) for articles in author_to_articles.values())
    return sorted([a for a, arts in author_to_articles.items() if
                   len(arts) == max_count])


def suggest_collaborators(
           id_to_article: ArxivType, author_name: NameType) -> list[NameType]:
    """Returns a list of authors with whom the author specificed, author_name,
    is encouraged to collaborate in arxiv data id_to_article.

    >>> suggest_collaborators(EXAMPLE_ARXIV, ('Pancer', 'Richard'))
    [('Ponce', 'Marcelo'), ('Tafliovich', 'Anya Y.')]
    """
    coauthors = set(get_coauthors(id_to_article, author_name))
    suggestions = set()
    for coauthor in coauthors:
        for candidate in get_coauthors(id_to_article, coauthor):
            if candidate != author_name and candidate not in coauthors:
                suggestions.add(candidate)
    return sorted(suggestions)


def has_prolific_authors(
        author_articles: dict[NameType, list[str]], information: ArticleType,
        min_publications: int) -> bool:
    """Return True iff the article has at least one prolific author.

    Parameters:
    - author_articles: dict mapping author names to their article ID list.
    - information: the article metadata to examine.
    - min_publications: the minimum number of publications to
    qualify as prolific.
    >>> has_prolific_authors(EXAMPLE_BY_AUTHOR, EXAMPLE_ARXIV['008'], 2)
    True
    >>> has_prolific_authors(EXAMPLE_BY_AUTHOR, EXAMPLE_ARXIV['031'], 2)
    False
    >>> has_prolific_authors(EXAMPLE_BY_AUTHOR, EXAMPLE_ARXIV['031'], 5)
    False
    """
    return any(len(author_articles[author]) >= min_publications
               for author in information[AUTHORS])


def keep_prolific_authors(
        id_to_article: ArxivType, min_publications: int) -> None:
    """Update the articles data id_to_article so that it contains only
    articles published by authors with min_publications or more
    articles published.

    >>> arxiv_copy = copy.deepcopy(EXAMPLE_ARXIV)
    >>> keep_prolific_authors(arxiv_copy, 2)
    >>> len(arxiv_copy)
    3
    >>> '008' in arxiv_copy and '067' in arxiv_copy and '827' in arxiv_copy
    True
    """
    author_to_articles = make_author_to_articles(id_to_article)
    to_keep = [aid for aid, art in id_to_article.items()
               if has_prolific_authors(author_to_articles,
                                       art, min_publications)]
    updated = {aid: id_to_article[aid] for aid in to_keep}
    id_to_article.clear()
    id_to_article.update(updated)
