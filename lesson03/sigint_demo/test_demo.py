from unittest import TestCase
from unittest.mock import patch
import demo

class MainTest(TestCase):
    def test_main(self):
        with self.assertRaises(KeyboardInterrupt):
            with patch("demo.print") as mocked_print:
                mocked_print.side_effect = KeyboardInterrupt()
                demo.main()