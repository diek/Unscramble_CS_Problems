"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv

call_length = {}
with open("calls.csv", "r") as f:
    next(f)
    for row in f:
        row = row.strip()
        call_num, rec_num, start, duration = row.split(",")
        duration = int(duration)
        if call_num in call_length:
            call_length[call_num] += duration
        else:
            call_length[call_num] = duration

        if rec_num in call_length:
            call_length[rec_num] += duration
        else:
            call_length[rec_num] = duration

key = max(call_length, key=call_length.get)
value = call_length[key]
print(
    f"{key} spent the longest time, {value} seconds, on the phone during September 2016."
)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during
September 2016.".
"""
