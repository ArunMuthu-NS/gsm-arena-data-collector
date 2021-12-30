def load_processed_phone_links(file_name):
    phones_list = []
    with open(file_name, "r") as phone_file:
        for phone in phone_file:
            phones_list.append(phone.strip())

    return phones_list
