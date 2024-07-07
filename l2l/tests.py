from datetime import datetime
from django.test import TestCase
from l2l.templatetags.l2l_extras import format_datetime_to_string


# Create your tests here.
class Test(TestCase):
    def test_format_datetime_to_string_with_datetime_parameter(self):
        input_datetime = datetime(2024, 7, 4, 14, 56, 2)
        actual = format_datetime_to_string(input_datetime)
        self.assertEquals('2024-07-04 14:56:02', actual)

    def test_format_datetime_to_string_with_str_parameter(self):
        input_string = '2024-07-04T14:56:02'
        actual = format_datetime_to_string(input_string)
        self.assertEquals('2024-07-04 14:56:02', actual)
