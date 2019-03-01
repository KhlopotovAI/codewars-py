from unittest import TestCase

from .kata import song_decoder


class TestSongDecoder(TestCase):
    def test_song_decoder(self):
        self.assertEqual("A B C", song_decoder("AWUBBWUBC"), "WUB should be replaced by 1 space")
        self.assertEqual("A B C", song_decoder("AWUBWUBWUBBWUBWUBWUBC"),
                         "multiples WUB should be replaced by only 1 space")
        self.assertEqual("A B C", song_decoder("WUBAWUBBWUBCWUB"), "heading or trailing spaces should be removed")
