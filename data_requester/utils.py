from pathlib import Path

import pandas as pd


def create_data_frame_from_dict(phone_details):
    cols = set()
    for phone_detail in phone_details:
        for key in phone_detail.keys():
            cols.add(key)

    data = []

    for phone_detail in phone_details:
        data_row = []
        for column in cols:
            if column in phone_detail:
                data_row.append(phone_detail[column])
            else:
                data_row.append("")

        data.append(data_row)

    return pd.DataFrame(data=data, columns=cols)


def get_file_name(file_path):
    count = len(list(Path(file_path).glob('*.csv')))
    return count + 1
