def load_processed_phone_links(file_name):
    phones_list = []
    with open(file_name, "r") as phone_file:
        for phone in phone_file:
            phones_list.append(phone.strip())

    return phones_list


def store_phone_names(processed_phone_links, file_name):
    with open(file_name, "a") as phone_file:
        for phone in processed_phone_links:
            phone_file.write(phone + "\n")
