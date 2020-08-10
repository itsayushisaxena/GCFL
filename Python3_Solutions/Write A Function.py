import calendar
def is_leap(year):
  return calendar.isleap(year)
    

year = int(input())
print(is_leap(year))
