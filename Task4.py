import csv


def get_texts(file):
    texts = []
    with open(file, "r") as f:
        next(f)
        reader = csv.reader(f)
        for row in reader:
            texts.append([row[0], row[1]])
    return texts


def get_calls(file):
    calls = []
    with open(file, "r") as f:
        next(f)
        reader = csv.reader(f)
        for row in reader:
            calls.append([row[0], row[1]])
    return calls


# Check 1, never send txt msg
def sent_text(master, send_txt):
    never_send = []
    for number in master:
        if number not in send_txt:
            never_send.append(number)
    return never_send


# Check 2, never recieve txt msg
def received_text(master, receive_txt):
    never_rec = []
    for number in master:
        if number not in receive_txt:
            never_rec.append(number)
    return never_rec


# Check 3, never recieve incoming calls
def receive_calls(master, incoming_call):
    never_rec_calls = []
    for number in master:
        if number not in incoming_call:
            never_rec_calls.append(number)
    return never_rec_calls


def main():
    texts = get_texts("texts.csv")
    calls = get_calls("calls.csv")
    possible_telemarketers = []

    master_call = set([call[0] for call in calls])
    send_text = set([msg[0] for msg in texts])
    receive_text = set([msg[1] for msg in texts])
    receive_call = set([call[1] for call in calls])

    # Resolved with the help of the code review
    possible_telemarketers = master_call.difference(
        send_text | receive_text | receive_call
    )

    print("These numbers could be telemarketers: ")
    for telemarketer in sorted(possible_telemarketers):
        print(telemarketer)


if __name__ == "__main__":
    main()
"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""
