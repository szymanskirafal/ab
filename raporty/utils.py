import calendar
import datetime
from datetime import timedelta


class DateRanges(object):


    current_date = datetime.date.today()

    def current_week_ends_in():
        days_in_week = 7
        current_weekday = DateRanges.current_date.weekday()
        days_remaining_to_full_week = days_in_week - current_weekday
        current_week_ends_in = DateRanges.current_date + timedelta(days = days_remaining_to_full_week)
        return current_week_ends_in

    def next_week_ends_in():
        current_week_ends_in = DateRanges.current_week_ends_in()
        next_week_ends_in = current_week_ends_in + timedelta(days = 7)
        return next_week_ends_in

    def current_month_ends_in():
        current_day = DateRanges.current_date
        month = current_day.month
        year = current_day.year

        weekday_of_first_day, number_of_days = calendar.monthrange(year, month)
        # Returns weekday of first day of the month and number of days in month, for the specified year and month.

        current_month_ends_in = datetime.date(year, month, number_of_days)
        return current_month_ends_in


#        if month == 12:
#            year = year + 1
#            month = 1
#            weekday_of_first_day, number_of_days = calendar.monthrange(year, month)
#            next_month_starts_in = datetime.date(year, month, 1)
#            next_month_ends_in = datetime.date(year, month, number_of_days)
#        else:
#            year = year
#            month = month + 1
#            weekday_of_first_day, number_of_days = calendar.monthrange(year, month)
#            next_month_starts_in = datetime.date(year, month, 1)
#           next_month_ends_in = datetime.date(year, month, number_of_days)

