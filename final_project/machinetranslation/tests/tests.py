'''
test translator module
'''

import unittest
import translator

class TestTranslator(unittest.TestCase):
    '''
    translator test class
    '''

    def test_FrToEn(self):
        '''
        test french to english
        '''

        self.assertEqual(translator.frenchToEnglish('Bonjour'), 'Hello')

    def test_EnToFr(self):
        '''
        test english to french
        '''

        self.assertEqual(translator.englishToFrench('Hello'), 'Bonjour')

    def test_Null_EnToFr(self):
        '''
        test for empty string in english to french
        '''

        self.assertEqual(translator.englishToFrench(""), "")

    def test_null_FrToEn(self):
        '''
        test for empty string in french to english
        '''

        self.assertEqual(translator.frenchToEnglish(""), "")

if __name__ == '__main__':
    unittest.main()
