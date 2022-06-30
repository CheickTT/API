import unittest
from youtubeApi import get_channel_dic, get_info


class TestFileName(unittest.TestCase):
    def test_get_info(self):
        channel = get_channel_dic('UCtJ3xivtW_ZxG0sOBz8HtyA')
        self.assertEqual(get_info(channel)['title'], 'Iba One')
        self.assertEqual(get_info(channel)['customUrl'], 'ibaoneofficielle')
        self.assertEqual(get_info(channel)['pubDate'], '2015-01-04T22:39:25Z')


if __name__ == '__main__':
    unittest.main()
