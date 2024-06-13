# Task0
Python's csv.reader object reads the entire file into a list, which takes linear time proportional to the number of rows in the file, and then we iterate over the list to find the last element, which also takes linear time.

### Worst-case Big-O notation: O(n) + O(n) = O(2n) => O(n)


# Task1
get_texts(file): O(n) as explained in Task0

get_calls(file): O(n) where n is the number of rows in the CSV file. This is because the csv.reader object reads the entire file into a list, which takes linear time proportional to the number of rows in the file.

The loop that iterates over telephone_numbers and adds elements to distinct_numbers: O(n) where n is the total number of rows in both CSV files.

The conversion of distinct_numbers to a set and then back to a list: O(n) where n is the number of elements in distinct_numbers. This is because converting a list to a set and back to a list takes linear time.

### Worst-case Big-O notation: O(n) + O(n) + O(n) + O(n) = O(4n) => O(n)

# Task2
Reading the CSV file and iterating over each row: explained in Task0

Splitting each row into parts and converting the duration to an integer: O(1), these operations are constant time.

Updating the call_length dictionary: O(1) because we are using a dictionary to store the call lengths, which allows for constant time lookups and updates.

Finding the maximum key in the call_length dictionary using the max function with a key: O(n) where n is the number of items in the dictionary, we need to iterate over each item in the dictionary to find the maximum key.

### Worst-case Big-O notation: O(n) + O(n) = O(2n) => O(n)

# Task3
contains_parentheses(mobile_number): O(n) where n is the number of characters in the mobile number, iterate over each character in the string.

is_fixed_line(phone_number): O(n) where n is the number of characters in the phone number, check if the phone number contains parentheses == linear time.

is_mobile_number(phone_number): O(n) where n is the number of characters in the phone number. This is because we split the phone number into parts, and then check if the length of the parts is equal == linear time.

is_telemarketer(phone_number): O(1) because it checks if the phone number starts with a specific string == constant time.

get_calls(file): explained in Task0.

main(): O(n) where n is the number of rows in the CSV file. As explained in Task0.

### Worst-case Big-O notation: O(n) + O(n) + O(n) + O(1) + O(n) = O(5n) => O(n).

# Task4
## Functions: sent_text(), received_text(), and receive_calls()

Each of these functions takes two sets as inputs and checks if each element in the master set is not in the second set, appending the element to the result list if the condition is met.

Time Complexity: O(m) for each function, where m is the size of the master set.
Space Complexity: O(m) (to store the result list)

## Function: main

### Reading Texts and Calls:
Explained in [Task0](#task0)

### Creating sets - from the texts and calls lists involves iterating through each list.
1. Extracting unique numbers from the calls list to form master_call has a complexity of O(n).
2. Similarly, extracting send_text, receive_text, and receive_call from the texts and calls lists each has a complexity of O(n).

### Checking Conditions:
1. sent_text(master_call, send_text) has a complexity of O(n).
2. received_text(master_call, receive_text) has a complexity of O(n).
3. receive_calls(master_call, receive_call) has a complexity of O(n).

### Combining Results (possible_telemarketers and sorting):
1. Creating the set from three lists (each of length at most n) has a complexity of O(n).
2. Sorting the resulting set has a complexity of O(n log n) 

## Worst-case Big-O notation for the provided code is:
Time Complexity: O(n log n)
Space Complexity: O(n)

# Note: Some assistance from chatgpt.com was used.
