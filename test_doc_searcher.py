import unittest

from doc_searcher import DocSearcher

class TestDocSearcher(unittest.TestCase):
  """
  Test the DocSearcher class
  """
  print('Running test for DocSearcher...')
  def setUp(self):
    # Initialize the docSearcher object
    self.DS = DocSearcher()

  def test_single_search(self):
    doc = 'I have a cat. My cat loves to nap. She is not good at catching mice. What a CAT'
    search_term = 'cat'
    expected = [(9, 12), (17, 20), (76, 79)]
    result = self.DS.get_char_span_single_search(doc, search_term)
    self.assertEqual(expected, result)
  
  def test_multi_search_all_occur(self):
    doc = 'I have a cat. My cat loves to nap. She is not good at catching mice. What a CAT'
    search_list = ['cat', 'catching mice']
    expected = [(9, 12), (17, 20), (76, 79), (54, 67)]
    result = self.DS.get_char_span_multi_search(doc, search_list)
    self.assertEqual(expected, result)
  
  def test_multi_search_not_all_occur(self):
    doc = 'I have a cat. My cat loves to nap. She is not good at catching mice. What a CAT'
    search_list = ['cat', 'dog']
    result = self.DS.get_char_span_multi_search(doc, search_list)
    self.assertEqual([], result)


if __name__ == '__main__':
  unittest.main()
