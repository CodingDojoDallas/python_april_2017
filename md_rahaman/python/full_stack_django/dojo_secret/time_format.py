import datetime
import pytz

# dt = datetime.datetime(2016,7,27,12,30,45,tzinfo=pytz.UTC)
# print dt

# dt_today = datetime.datetime.today()
# dt_now = datetime.datetime.now(tz=pytz.UTC)
# # # dt_utcnow = datetime.datetime.utcnow()
# dt_me = dt_now.astimezone(pytz.timezone('US/Central'))


# # # print dt_today
# # print dt_now
# print dt_me
# # print dt_utcnow

# # for tz in pytz.all_timezones:
# # 	print tz


local_time = datetime.datetime.now()
central_tz = pytz.timezone('US/Central')

local_time_tz = central_tz.localize(local_time)
print local_time_tz.strftime('%H %M %S')

print local_time
print central_tz
print local_time_tz