from unittest import TestCase

from .kata import generate_hashtag


class TestGenerateHashtag(TestCase):
    def test_generate_hashtag(self):
        self.assertFalse(generate_hashtag(''), 'Expected an empty string to return False')
        self.assertEqual('#', generate_hashtag('Do We have A Hashtag')[0], 'Expeted a Hashtag (#) at the beginning.')
        self.assertEqual('#Codewars', generate_hashtag('Codewars'), 'Should handle a single word.')
        self.assertEqual('#Codewars', generate_hashtag('Codewars      '), 'Should handle trailing whitespace.')
        self.assertEqual('#CodewarsIsNice', generate_hashtag('Codewars Is Nice'), 'Should remove spaces.')
        self.assertEqual('#CodewarsIsNice', generate_hashtag('codewars is nice'),
                         'Should capitalize first letters of words.')
        self.assertEqual('#CodewarsIsNice', generate_hashtag('CodeWars is nice'),
                         'Should capitalize all letters of words - all lower case but the first.')
        self.assertEqual('#CIN', generate_hashtag('c i n'),
                         'Should capitalize first letters of words even when single letters.')
        self.assertEqual('#CodewarsIsNice', generate_hashtag('codewars  is  nice'),
                         'Should deal with unnecessary middle spaces.')
        self.assertFalse(generate_hashtag(
            'Loooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo'
            'ooooooooooooooooooooooooooooooooooooooooooooooooooooooong Cat'
        ), 'Should return False if the final word is longer than 140 chars.')
