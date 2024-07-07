from datetime import datetime
from django import template

register = template.Library()


@register.filter(name='l2l_dt')
def format_datetime_to_string(input_value: datetime | str) -> str:
    if isinstance(input_value, datetime):
        input_as_datetime = input_value
    else:
        input_as_datetime = datetime.strptime(input_value, "%Y-%m-%dT%H:%M:%S")
    return input_as_datetime.strftime('%Y-%m-%d %H:%M:%S')
