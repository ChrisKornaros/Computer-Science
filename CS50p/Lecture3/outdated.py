# Build the main function
def main():
    global months
    # List containing the months in Titlecase
    months = {
        "January" : '1',
        "February" : '2',
        "March" : '3',
        "April" : '4',
        "May" : '5',
        "June" : '6',
        "July" : '7',
        "August" : '8',
        "September" : '9',
        "October" : '10',
        "November" : '11',
        "December" : '12'
    }

    # Initialize a blank list for the separated date string
    date_list = []
    # Prompt a user for the date, ensure the month and format are acceptable before continuing
    while True:
        try:
            ad = input("Date: ").strip().title()
            # See if there is a '/' in the date, then handle accordingly
            if '/' in ad:
                date_list = ad.split('/')
                if date_list[0] in months.values() and int(date_list[1]) <= 31:
                    break
                else:
                    pass # Reprompt the user for input if the month is incorrect
            # See if there is a ' ' in the date, then handle accordingly
            elif ' ' in ad:
                date_list = ad.split(' ')
                if ',' in date_list[1]:
                    date_list[1] = date_list[1].replace(',', '')
                    if date_list[0].title() in months.keys() and int(date_list[1]) <= 31:
                        break
                    else:
                        pass
                else:
                    pass # Reprompt if there is no comma, you can also use continue
            else:
                pass
        except:
            pass # If the code encounters an error, reprompt the user

    # Convert the format from middle-endian to big-endian
    date_fin = big_end(date_list)

    # Pad the month and day with leading zeros if necessary
    date_fin[1] = date_fin[1].zfill(2)
    date_fin[2] = date_fin[2].zfill(2)

    return print(f"{date_fin[0]}-{date_fin[1]}-{date_fin[2]}")

# Define the endian conversion function
def big_end(m_end):
    # Check whether it's a numeric or string formatted month
    if m_end[0] in months.keys():
        m_end[0] = months.get(m_end[0])
        b_end = [m_end[2], m_end[0], m_end[1]]
        return b_end
    elif m_end[0] in months.values():
        b_end = [m_end[2], m_end[0], m_end[1]]
        return b_end
    else:
        return 0

main()
