"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv


def find_first_text(file):
    with open(file, "r") as f:
        next(f)
        reader = csv.reader(f)
        texts = list(reader)
    return texts[0]


def find_last_call(file):
    with open(file, "r") as f:
        reader = csv.reader(f)
        calls = list(reader)
    return calls[-1]


first_text = find_first_text("texts.csv")
last_call = find_last_call("calls.csv")

print(
    f"First record of texts, {first_text[0]} texts {first_text[1]} at time {first_text[2]}"
)
print(
    f"Last record of calls, {last_call[0]} calls {last_call[1]} at time {last_call[2]}, lasting {last_call[3]} seconds"
)


# "First record of texts, <incoming number> texts <answering number> at time <time>"
# "Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""
