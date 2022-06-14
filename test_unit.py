import random
import unittest

import base62

import dao
import logic


class MyTestCase(unittest.TestCase):
    def _test_add_url(self):
        for i in range(100000):
            full_url = 'https://www.google' + str(random.random()) + '.com'
            seq = dao.get_or_gen_short_id(full_url)
            if seq < 0:
                print('duplicate url')
            else:
                short_url = base62.encode(seq)
                dao.insert_url_map(short_url, full_url)
        self.assertGreaterEqual(1, 1)

    def test_add_url_with_name(self):
        full_url = 'https://www.google' + str(random.random()) + '.com'
        name = 'UU'
        short = logic.add_full_url_with_name(full_url, name)
        full = logic.get_full_url(short)
        self.assertGreaterEqual(full, full_url)


if __name__ == '__main__':
    unittest.main()
