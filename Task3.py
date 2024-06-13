import csv


def contains_parentheses(mobile_number):
    parentheses = ["(", ")"]
    for number in mobile_number:
        if number in parentheses:
            return True
    return False


def is_fixed_line(phone_number):
    """criteria => include parentheses, 2nd character must be zero"""
    flag = False
    if contains_parentheses(phone_number):
        flag = True

    if phone_number[0:2] == "(0":
        flag = True
    else:
        flag = False

    return flag


def is_mobile_number(phone_number):
    """criteria => Mobile numbers have no parentheses, but have a space in the middle
    of the number. First 3 digits are area code
    """
    flag = False
    if contains_parentheses(phone_number):
        return flag
    mobile_number = phone_number.split(" ")
    if len(mobile_number) == 2:
        if len(mobile_number[0]) == len(mobile_number[1]):
            flag = True

    if mobile_number[0].startswith(("7", "8", "9")):
        flag = True
    else:
        flag = False
    return flag


def is_telemarketer(phone_number):
    """criteria => have no parentheses or space, but they start
    with the area code 140"""
    if phone_number.startswith("140", 0):
        return True


def get_calls(file):
    """Get calls originating in landline area code 080"""
    call_list = []
    with open(file, "r") as f:
        reader = csv.reader(f)
        next(f)
        for row in f:
            row = row.strip()
            call_num, rec_num, start, duration = row.split(",")
            if call_num.startswith("(080)", 0):
                call_list.append(rec_num)

    return call_list


def main():
    filtered_outgoing = get_calls("calls.csv")
    telemarketers = []
    area_codes = []
    fixed_line = []

    # Part A
    for call in filtered_outgoing:
        if is_telemarketer(call):
            area_codes.append(call)
            continue

        if is_fixed_line(call):
            start_index = call.find("(") + 1
            end_index = call.find(")")
            area_codes.append(call[start_index:end_index])
            fixed_line.append(call[start_index:end_index])
            continue

        if is_mobile_number(call):
            area_codes.append(call[0:4])

    unique_area_codes = set(area_codes)
    # print("The numbers called by people in Bangalore have codes:")
    # for area_code in sorted(unique_area_codes):
    #     print(area_code)

    print(fixed_line)

    # Part B

    # Step 1: Count total calls from '080'
    total_calls_from_Bangalore = fixed_line.count("080")

    # Step 2: Count calls from '080' to '080'
    calls_from_Bangalore_to_Bangalore = 0
    for i in range(len(fixed_line) - 1):
        if fixed_line[i] == "080" and fixed_line[i + 1] == "080":
            calls_from_Bangalore_to_Bangalore += 1

    # Step 3: Calculate the percentage
    percentage_calls_from_080_to_080 = (
        calls_from_Bangalore_to_Bangalore / total_calls_from_Bangalore
    ) * 100

    total_calls_from_Bangalore, calls_from_Bangalore_to_Bangalore, percentage_calls_from_080_to_080


if __name__ == "__main__":
    main()


"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore. In other words, the calls were initiated by "(080)" area code
to the following area codes and mobile prefixes:

   (080)xxxxxxx.
   (022)46574732
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.


 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.

   140
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
