import datetime
#  check if a string is a valid date in the format "Month day, year"


def is_valid_date(date_str):
    try:
        datetime.datetime.strptime(date_str, "%B %d, %Y")
        return True
    except ValueError:
        return False


def parse_date(date_str):
    date_obj = datetime.datetime.strptime(date_str, "%B %d, %Y")
    return date_obj.strftime("%m/%d/%Y")


def read_and_filter_dates():
    current_date = datetime.datetime.now()
    parsed_dates = []

    while True:
        date_str = input().strip()
        if date_str == '-1':
            break

        if is_valid_date(date_str):
            date_obj = datetime.datetime.strptime(date_str, "%B %d, %Y")
            if date_obj <= current_date:
                parsed_dates.append(parse_date(date_str))

    return parsed_dates


def parse_dates_from_file(input_file, output_file):
    current_date = datetime.datetime.now()

    with open(input_file, 'r') as f_in, open(output_file, 'w') as f_out:
        for line in f_in:
            date_str = line.strip()
            if date_str == '-1':
                break

            if is_valid_date(date_str):
                date_obj = datetime.datetime.strptime(date_str, "%B %d, %Y")
                if date_obj <= current_date:
                    f_out.write(parse_date(date_str) + '\n')


# Main function
if __name__ == "__main__":

    print("Enter dates in the format 'Month day, year'. Enter -1 to end.")
    parsed_dates = read_and_filter_dates()
    for date in parsed_dates:
        print(date)

    input_file = "inputDates.txt"
    output_file = "parsedDates.txt"
    parse_dates_from_file(input_file, output_file)
