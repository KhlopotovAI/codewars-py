from unittest import TestCase

from .kata import format_duration


class TestFormatDuration(TestCase):
    def test_format_duration(self):
        self.assertEquals("1 second", format_duration(1))
        self.assertEquals("1 minute and 2 seconds", format_duration(62))
        self.assertEquals("2 minutes", format_duration(120))
        self.assertEquals("1 hour", format_duration(3600))
        self.assertEquals("1 hour, 1 minute and 2 seconds", format_duration(3662))
