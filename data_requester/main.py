from args import parser
from phone_model import Phone
from phones_db import load_processed_phone_links, store_phone_names
from phones_requests import get_all_phone_details, get_phone_brands
from utils import create_data_frame_from_dict

if __name__ == '__main__':
    parsed_args = parser().parse_args()
    phone_brand_links = get_phone_brands()

    if parsed_args.brand.lower() not in phone_brand_links:
        raise Exception("Given brand is not listed in GSM Arena")

    phone_model = Phone(parsed_args.brand, parsed_args.data_path)
    processed_phones = load_processed_phone_links(phone_model.processed_data_path())
    current_processed_phones, phone_data = get_all_phone_details(
        processed_phones, phone_brand_links[parsed_args.brand], parsed_args.sleep, parsed_args.page_size
    )

    store_phone_names(current_processed_phones, phone_model.processed_data_path())
    phones_data_frame = create_data_frame_from_dict(phone_data)
    phones_data_frame.to_csv(phone_model.current_file_path())
