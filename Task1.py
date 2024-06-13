import csv


def get_texts(file):
    with open(file, "r") as f:
        next(f)
        reader = csv.reader(f)
        texts = list(reader)
    return texts


def get_calls(file):
    with open("calls.csv", "r") as f:
        next(f)
        reader = csv.reader(f)
        calls = list(reader)
    return calls


telephone_numbers = []
distinct_numbers = []

telephone_numbers = get_texts("texts.csv")
telephone_numbers += get_calls("calls.csv")

for row in telephone_numbers:
    distinct_numbers.append(row[0])
    distinct_numbers.append(row[1])


num_distinct_numbers = len(set(distinct_numbers))

print(f"There are {num_distinct_numbers} different telephone numbers in the records.")

"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
