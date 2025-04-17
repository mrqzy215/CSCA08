# Working with Metadata
In the starter code file arxiv_functions.py, complete the following function definitions. In addition, you must add some helper functions to aid with the implementation of these required functions.

Functions to implement in arxiv_functions.py
Function name:
(Parameter types) -> Return type	Full Description (paraphrase to get a proper docstring description)
make_author_to_articles:
(ArxivType) -> dict[NameType, list[str]]	
The parameter represents arxiv metadata. This function should return a dictionary that maps each author name to a list of identifiers of articles written by that author. The list should be sorted in lexicographic order.

Hint: You can simply use the built-in method sort or function sorted to do the sorting. It is a good idea to build the dictionary first, and then sort the article lists (the values in the dictionary).

For example, if the input is a dictionary that represents the information from our example metadata file, then make_author_to_articles should return the dictionary

{
    ('Ponce', 'Marcelo'): ['008', '827'],
    ('Tafliovich', 'Anya Y.'): ['008', '827'],
    ('Bretscher', 'Anna'): ['067', '827'],
    ('Breuss', 'Nataliya'): ['031'],
    ('Pancer', 'Richard'): ['067']
}
      
get_coauthors:
(ArxivType, NameType) -> list[NameType]	
The first parameter represents arxiv metadata and the second parameter represents an author's name. This function should return a list of coauthors of the author specified by the second argument. (Two people are coauthors if they are authors of the same article.) The list should be sorted in lexicographic order.

Hints: You can simply use the built-in method sort or function sorted to do the sorting. Make sure you don't claim that a person is her own coauthor and don't include any names more than once in the return list. Make sure your code does not crash if the author does not appear in the input dictionary at all! Consider using function(s) you already defined to simplify your solution.

For example, if the first argument is a dictionary that represents the information from our example metadata file and the second argument is ('Tafliovich', 'Anya Y.'), then this function should return the list

[('Bretscher', 'Anna'), ('Ponce', 'Marcelo')]
      
Note that ('Ponce', 'Marcelo') appears only once in the list, even though he authored two articles with ('Tafliovich', 'Anya Y.'), namely articles '008' and '827'.

get_most_published_authors:
(ArxivType) -> list[NameType]	
The parameter represents arxiv metadata. This function should return a list of authors who published the most articles. Note that this list has more than one author only in case of a tie! The list should be sorted in lexicographic order.

Hints: You can simply use the built-in method sort or function sorted to do the sorting. Consider using function(s) you already defined to simplify your solution. Specifically, it is a good idea to implement the function make_author_to_articles before this one.

For example, if input is a dictionary that represents the information from our example metadata file, then this function should return the list

[('Bretscher', 'Anna'), ('Ponce', 'Marcelo'), ('Tafliovich', 'Anya Y.')]
      
suggest_collaborators:
(ArxivType, NameType) -> list[NameType]	
The first parameter represents arxiv metadata and the second parameter represents the author's name. This function should return a list of authors with whom the author specified by the second argument is encouraged to collaborate. The list should be sorted in lexicographic order.

The list of suggested collaborators should include all authors who are coauthors of this author's coauthors. In other words, if author A wrote an article with author B and author B wrote an article with author C, then we will include C as suggested collaborator for A.

Hints: You can simply use the built-in method sort or function sorted to do the sorting. Consider using function(s) you already defined to simplify your solution. Make sure you do not include people who are already coauthors of the given author in the return list (they already know each other!). Make sure you don't include the author herself as a suggested collaborator. Finally, make sure the resulting list does not contain any names more than once.

For example, if the first argument is a dictionary that represents the information from our example metadata file and the second argument is ('Pancer', 'Richard'), then this function should return the list

[('Ponce', 'Marcelo'), ('Tafliovich', 'Anya Y.')]
      
and if the second argument is ('Tafliovich', 'Anya Y.'), then this function should return the list

[('Pancer', 'Richard')]
      
has_prolific_authors:
(dict[NameType, list[str]], ArticleType, int) -> bool	
The first parameter is a dictionary that maps author name to a list of IDs of articles published by that author, the second parameter represents the information on a single article, and the third argument represents the minimum number of publications required for an author to be considered prolific. The function should return True if and only if the article (second argument) has at least one author who is considered prolific.

For example, if the first argument is the dictionary

{
    ('Ponce', 'Marcelo'): ['008', '827'],
    ('Tafliovich', 'Anya Y.'): ['008', '827'],
    ('Bretscher', 'Anna'): ['067', '827'],
    ('Breuss', 'Nataliya'): ['031'],
    ('Pancer', 'Richard'): ['067']
}
      
the second argument is the article with ID '008' from our example, and the third argument is 2, then the function should return True, because at least one of the authors of the article with ID '008' is "prolific", i.e., has published at least 2 papers. (In fact, both Marcelo Ponce and Anya Tafliovich are "prolific" in the example.) If the second argument is the article with ID '031' (and the other arguments are the same), then the function should return False, since none of the authors of this article have published at least two papers.

You can assume that every author of the input article also appears as a key in the dict which is the first argument.

keep_prolific_authors:
(ArxivType, int) -> None	
The first parameter represents arxiv metadata and the second parameter represents the minimum number of publications required for an author to be considered prolific. The function should modify its first argument so that it contains only articles published by prolific authors, i.e., articles that have at least one author who has published at least the minimum required number of articles.

For example, if the first argument is a dictionary that represents the information from our example metadata file and the second argument is 2, then the function should modify its first argument by removing the articles with IDs '031' and '042', and keeping the articles with IDs '008', '067', and '827'.

In this example, we have three authors who have published at least two articles: ('Ponce', 'Marcelo'), ('Tafliovich', 'Anya Y.'), and ('Bretscher', 'Anna'), i.e. three "prolific" authors. Therefore, the function should keep only those articles who have (at least) one of these three people as authors: articles with IDs '008', '067', and '827'.

Hint: Notice that this function returns None and modifies its argument. Recall that in Python you never want to remove items from a dictionary while iterating over that same dictionary. One way to avoid this issue in your solution is to first decide on which articles should be removed from the dictionary, and then remove them in a separate loop.

More hints: Consider using the functions make_author_to_articles and has_prolific_authors as helpers to simplify your solution. When writing tests for this function, remember that the function modifies its input. To make sure that the tests do not interfere with each other, we often create copies of sample input and pass these copies to the function we are testing. Take a careful look at the docstring for this function which we provided in the starter code and pay attention to the use of copy.deepcopy in the example calls.

read_arxiv_file:
(TextIO) -> ArxivType	
The parameter represents an arxiv metadata file that is already open for reading. This function should read the file and return the data in the ArxivType dictionary format. Take a careful look at the starter file example_data.txt (same as the example above) and the corresponding dictionary EXAMPLE_ARXIV defined in the file arxiv_functions.py for an example.

Note: in the docstring, do not provide example calls for functions that read files.
