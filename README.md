# nlp-task-document-search

### File Descriptions:
`doc_searcher.py`: This script contains a DocSearcher class that does the following:

1. **Single search**: Takes as input a word or phrase as well as a text document and searches that document for any case variant of that word/phrase. 
Returns character spans for where each occurrence is in the input document.
2. **Multi search**: Takes a input a list of words/phrases as well as a text document, and, if *all* of the supplied words/phrases occur, 
it returns the character spans for where each of the supplied terms occur; else, it returns an empty list.

`test_doc_searcher.py`: Contains the unit tests for both the single search function and multi search function of the DocSearcher class.
Run the tests by running the following command in the terminal:
```
python test_doc_searcher.py
```
