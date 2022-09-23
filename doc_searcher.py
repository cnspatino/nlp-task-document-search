

from itertools import chain
import re
import string

from nltk import ngrams

class DocSearcher():
	"""
		Class used to search a document for a word or multi-word phrase.
		NOTE: The search steps were optimized to use regex as minimally as possible
		since it is notoriously slow.
	"""
    
	def __init__(self):
		pass

	def _get_char_span(self, doc, search_string):
		"""
		 Returns list of tuples (character spans) for where each occurence of the 
		 search string occurs in the input document.
		"""
		# avoid false positives (e.g. nested terms) by padding search with whitespace or
		# beginning/end of string
		spans = [m.span(2) for m in re.finditer(f'(\s|^)({search_string})(\s|$)', doc)]
		return spans

	def _get_ngrams(self, text, n):
		""" 
			Get list of n-grams (string) from input text (contiguous sequence of n items)
			Ex: If n=3, 'hello there how are you' -> ['hello there how', 'there how are', 'how are you']
		"""
		#TODO: With more time, I would see if there are faster ways to generate n-grams than with nltk
		n_grams = ngrams(text.split(), n)
		final_ngrams = []
		for grams in n_grams:
			final_ngrams.append(' '.join(grams))
		return final_ngrams
    
	def _pre_process_text(self, text):
		# convert to lowercase
		text = text.lower()
		# replace any punctuation with a space
		text = text.translate(str.maketrans(dict.fromkeys(string.punctuation, ' ')))
		return text
	
	def get_char_span_multi_search(self, doc, search_list):
		"""
		PARAMS:
			doc: text document to search over (string)
			search_list: list of words/phrases to search for in the doc (list of strings)
		RETURNS:
			list of character spans represented as tuples only if all of the supplied 
			search strings occur in doc, else returns an empty list
		"""
		# STEP 1: pre-process both the document and all of the search strings
		doc = self._pre_process_text(doc)
		span_results = []
		# STEP 2: search & get char span for each search term; break if one not found
		for search_str in search_list:
			spans = self.get_char_span_single_search(doc, search_str)
			if not spans:
				# return empty result because all of the input phrases must occur in doc
				return []
			span_results.append(spans)
		# convert nested list into a single list of tuples
		all_spans = list(chain.from_iterable(span_results))
		return all_spans
	
	def get_char_span_single_search(self, doc, search_string):
		"""
		PARAMS:
				doc: text document to search over (string)
				search_string: word or multi-word phrase to search for in the doc (string)
		RETURNS:
				list of character spans represented as tuples
		"""
		spans = []
		# STEP 1: pre-process both the document and the search string
		doc = self._pre_process_text(doc)
		search_string = self._pre_process_text(search_string)
		
		# for efficiency purposes, first look to see if the string is even in the doc 
		# before continuing with more accurate search
		if search_string in doc:
			# STEP 2: convert doc to list of n-grams based on number of words in search string
			n = len(search_string.split())
			doc_n_grams = self._get_ngrams(doc, n)
			if search_string in doc_n_grams:
				# STEP 3: search the pre-processed doc for the text string and get char spans of each found match
				spans = self._get_char_span(doc, search_string)
		return spans
	

	
