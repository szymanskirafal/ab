import calendar
import datetime
from datetime import timedelta




def current_week_ends_in():
    days_in_week = 7
    current_date = datetime.date.today()
    current_weekday = current_date.weekday()
    days_remaining_to_full_week = days_in_week - current_weekday
    current_week_ends_in = current_date + timedelta(days = days_remaining_to_full_week)
    return current_week_ends_in


    # calculating date for different ranges of queries

   # self.next_week_starts_in = this_week_ends_in + timedelta(days = 1)
#    self.next_week_ends_in = next_week_starts_in + timedelta(days = 6)
#    self.rest_of_this_month_starts_in = next_week_ends_in + timedelta(days = 1)

 #   this_month = current_date.month
  #  this_year = current_date.year

  #  year = this_year
  #  month = this_month

   # weekday_of_first_day, number_of_days = calendar.monthrange(year, month)
    # Returns weekday of first day of the month and number of days in month, for the specified year and month.

#    def this_month_ends_in():
 #       this_month_ends_in = datetime.date(year, month, number_of_days)
  #      if month == 12:
   #         year = year + 1
#            month = 1
 #           weekday_of_first_day, number_of_days = calendar.monthrange(year, month)
  #          next_month_starts_in = datetime.date(year, month, 1)
   #         next_month_ends_in = datetime.date(year, month, number_of_days)
#        else:
 #           year = year
  #          month = month + 1
   #         weekday_of_first_day, number_of_days = calendar.monthrange(year, month)
    #        next_month_starts_in = datetime.date(year, month, 1)
     #       next_month_ends_in = datetime.date(year, month, number_of_days)