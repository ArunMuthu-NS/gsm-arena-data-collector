import time
import requests
from pyquery import PyQuery

gsm_arena_base_url = "https://www.gsmarena.com/"


def process_request(link):
    response = requests.get(link)
    if response.status_code != 200:
        print(f"Request failed with {response.status_code} with reason {response.text}")
        raise Exception()
    return response.text


def get_phone_brands():
    phones = {}
    home_page_response = process_request(gsm_arena_base_url)
    root = PyQuery(home_page_response)
    brands = root.find(".brandmenu-v2").find("ul").find("li")

    for brand in brands.items():
        brand_name = brand.find("a").text().lower()
        brand_link = brand.find("a").attr("href")
        phones[brand_name] = brand_link

    return phones


def get_next_page(page_details):
    next_page_link = page_details.find("a[title='Next page']").attr("href")
    return None if next_page_link == "#1" or next_page_link is None else next_page_link


def get_list_of_phones_in_the_given_page(root_html_element):
    phones_list = []
    phones = root_html_element("#review-body").find("ul").find("li")

    for phone in phones.items():
        phones_list.append(phone.find("a").attr("href"))

    return phones_list


def populate_phone_detail(phone_details):
    phones_data = {}

    phone_name = phone_details.find(".specs-phone-name-title").text()
    specs = phone_details.find("#specs-list")
    feature_categories = specs.find("table")

    for feature_category in feature_categories.items():
        features = feature_category.find("tr")
        for feature in features.items():
            feature_name = feature.find("td").eq(0).find("a").text()
            feature_value = feature.find("td").eq(1).text()
            phones_data[feature_name] = feature_value

    phones_data["name"] = phone_name
    return phones_data


def get_all_phone_details(existing_phones, link, time_to_wait, page_no=None):
    phone_list = []
    processed_phones = []
    current_page = 1

    try:
        while link is not None:
            if page_no is not None and current_page > page_no:
                break

            phones_response = process_request(gsm_arena_base_url + link)
            root = PyQuery(phones_response)
            phone_links = get_list_of_phones_in_the_given_page(root)

            for phone_link in phone_links:
                if phone_link in existing_phones:
                    continue

                time.sleep(time_to_wait)
                details = process_request(gsm_arena_base_url + phone_link)
                phone_details = PyQuery(details)
                phone_detail = populate_phone_detail(phone_details)
                phone_list.append(phone_detail)
                processed_phones.append(phone_link)

            current_page = current_page + 1
            link = get_next_page(root)
    except Exception as e:
        print(e)

    return processed_phones, phone_list
