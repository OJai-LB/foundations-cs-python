def int_count(intput_int):
    #base case
    if intput_int < 10:
        return 1
    #recursive case
    else:
        return 1 + (int_count(intput_int // 10))


def max_element(input_list):
    #base case
    if len(input_list) == 1:
        return input_list[0]
    else:
        if input_list[-1] < input_list[-2]:
            del input_list[-1]
            return max_element(input_list)
        else:
            del input_list[-2]
            return max_element(input_list)
        
def mean(input_list, column_index):
    m = 0
    for _ in input_list:
        m += input_list[column_index]
    return m / len(input_list)

def standard_deviation(input_list, column_index):
    sd = 0
    for _ in input_list:
        sd += ((input_list[column_index] - mean(input_list, column_index)) ** 2) ** 0.5
    return sd / len(input_list)
def number_of_normalised_columns(input_list, row_index):
    #base case
    if row_index == 1 and mean(input_list, row_index) == 0 and standard_deviation(input_list, row_index) == 1:
        return 1
    #recursive case
    elif row_index > 1 and mean(input_list, row_index) == 0 and standard_deviation(input_list, row_index) == 1
        return 1 + number_of_normalised_columns(input_list, row_index - 1)
    else:
        return number_of_normalised_columns(input_list, row_index - 1)



def int_count_prompt():
    user_input = (int(input("Enter a number to count its digits:")))
    return int_count(user_input)
def max_element_prompt():
    user_input = input("Enter a list of integers to return the maximum, seperated by space: ")
    user_input_str_list = user_input.strip().split()
    user_input_int_list = [int(i) for i in user_input_str_list]
    return max_element(user_input_int_list)

def display_menu():
    print("""
    1. Count Digits
    2. Find Max
    3. Count Normalized Columns
    4. Exit
    ___________________________
    """)


def main():
    display_menu()
    user_input = int(input("Enter a choice:"))

    if user_input == 1:
        print(int_count_prompt())
    elif user_input == 2:
        print(max_element_prompt())
    elif user_input == 4:
        print("Exiting...")

    main()




main()


