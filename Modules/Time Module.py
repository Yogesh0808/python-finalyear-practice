import time

# Get current time in seconds since epoch
seconds = time.time()

# Print current time in seconds since epoch
print("Seconds since epoch =", seconds)

# Print current local time
print("Local time:", time.ctime(seconds))

# Sleep for 2.4 seconds
time.sleep(2.4)

# Get current time as struct_time in local time
result = time.localtime(seconds)
print("Year:", result.tm_year)
print("Hour:", result.tm_hour)

# Get current time as struct_time in UTC
result = time.gmtime(seconds)
print("Year:", result.tm_year)
print("Hour:", result.tm_hour)

# Convert tuple to seconds since epoch in local time
t = (2018, 12, 28, 8, 44, 4, 4, 362, 0)
local_time = time.mktime(t)
print("Local time:", local_time)

# Convert tuple to string representing time
t = (2018, 12, 28, 8, 44, 4, 4, 362, 0)
print("Result:", time.asctime(t))

# Get current time as string with custom format
time_string = time.strftime("%m/%d/%Y, %H:%M:%S", time.localtime())
print("Time:", time_string)

# Parse string representing time to struct_time
time_string = "21 June, 2018"
result = time.strptime(time_string, "%d %B, %Y")
print("Result:", result)
