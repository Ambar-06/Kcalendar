from datetime import datetime, timedelta
import pytz
import typing as _
import datetime as dt
import io
import base64

"""
This class is used for date time formatter
Fields:
    DATE_TIME_FORMAT_1: This field is used for date time format 1
    DATE_TIME_FORMAT_2: This field is used for date time format 2
    DATE_FORMAT_1: This field is used for date format 1
    TIME_FORMAT_1: This field is used for time format 1
    DATE_FORMAT_2: This field is used for date format 2
"""


class DateTimeFormatter:
    DATE_TIME_FORMAT_1 = "%Y-%m-%dT%H:%M:%S%z"
    DATE_TIME_FORMAT_2 = "%Y-%m-%d %H:%M:%S"
    DATE_FORMAT_1 = "%d %B, %Y"
    TIME_FORMAT_1 = "%I:%M %p"
    DATE_FORMAT_2 = "iso-8601"


class DateCompareOperations:
    GREATER_THAN = "greater_than"
    LESS_THAN = "less_than"
    EQUAL = "equal"
    GREATER_THAN_OR_EQUAL = "greater_than_or_equal"
    LESS_THAN_OR_EQUAL = "less_than_or_equal"


class DateTime:
    def __init__(self) -> None:
        pass

    def compare_date(self, date1, date2, operation):
        if operation == DateCompareOperations().LESS_THAN_OR_EQUAL:
            return date1 <= date2

    def convert_to_user_timezone(self, date_string, user_timezone):
        utc_date = datetime.fromisoformat(date_string.replace("Z", "+00:00"))

        user_tz = pytz.timezone(user_timezone)

        user_local_time = utc_date.astimezone(user_tz)

        return user_local_time

    def convert_to_humanized_format(self, date_string, user_timezone):
        user_local_time = self.convert_to_user_timezone(date_string, user_timezone)

        current_time = datetime.now(user_local_time.tzinfo)

        time_difference = current_time - user_local_time

        if time_difference.days == 0:
            if time_difference.seconds < 60:
                return "just now"
            elif time_difference.seconds < 3600:
                minutes = time_difference.seconds // 60
                return f"{minutes} minutes ago"
            else:
                hours = time_difference.seconds // 3600
                return f"{hours} hours ago"
        elif time_difference.days < 7:
            return f"{time_difference.days} days ago"
        elif time_difference.days < 30:
            weeks = time_difference.days // 7
            return f"{weeks} weeks ago"
        else:
            months = time_difference.days // 30
            return f"{months} months ago"

    def subtract_buffer_time(
        self, datetime, req_type: _.Optional[str] = "time", buffer: _.Optional[int] = 30
    ):
        ist_timezone = pytz.timezone("Asia/Kolkata")  # IST timezone
        ist_now = datetime.now(ist_timezone)
        ist_now_with_buffer = ist_now - timedelta(minutes=buffer)
        ist_time_formatted = ist_now_with_buffer.strftime("%H:%M:%S")
        if req_type == "str":
            return ist_time_formatted
        else:
            ist_time_formatted = datetime.strptime(
                ist_time_formatted, "%H:%M:%S"
            ).time()
            return ist_time_formatted

    def change_time(
        self,
        datetime_obj,
        time_zone: _.Optional[str] = "UTC",
        operation: _.Optional[str] = "+",
        delta: _.Optional[dict] = {"seconds": 0, "minutes": 0, "hours": 0, "days": 0},
    ):
        if time_zone == "UTC":
            datetime_obj = datetime_obj.replace(tzinfo=dt.timezone.utc)
        elif time_zone == "Europe":
            datetime_obj = datetime_obj.replace(tzinfo=pytz.timezone("Europe/London"))
        elif time_zone == "Asia":
            datetime_obj = datetime_obj.replace(tzinfo=pytz.timezone("Asia/Kolkata"))
        if operation == "+":
            return datetime_obj + timedelta(**delta)
        elif operation == "-":
            return datetime_obj - timedelta(**delta)

    def convert_str_date_formate(self, date):
        date_object = datetime.strptime(date, "%Y-%m-%d")
        formatted_date = date_object.strftime("%d-%m-%Y")

        return formatted_date



def convert_date_format(input_date_str):
    # Define a mapping for month names
    month_names = {
        "01": "जनवरी",
        "02": "फरवरी",
        "03": "मार्च",
        "04": "अप्रैल",
        "05": "मई",
        "06": "जून",
        "07": "जुलाई",
        "08": "अगस्त",
        "09": "सितंबर",
        "10": "अक्टूबर",
        "11": "नवंबर",
        "12": "दिसंबर",
    }

    # Parse the input date string
    input_date = datetime.strptime(str(input_date_str), "%Y-%m-%d")

    # Format the date in the desired format
    output_date = (
        f"{input_date.day} {month_names[input_date.strftime('%m')]} {input_date.year}"
    )

    return output_date


def convert_image_to_binary(image_file):
    img_buffer = io.BytesIO()
    image_file.save(img_buffer, format="PNG")
    img_binary_data = img_buffer.getvalue()

    return img_binary_data


def time_to_minutes(time_obj):
    hours = time_obj.hour
    minutes = time_obj.minute
    seconds = time_obj.second

    # Convert hours, minutes, and seconds to minutes and add them together
    total_minutes = hours * 60 + minutes + seconds // 60

    return total_minutes
