from data_requester.utils import create_data_frame_from_dict
import pandas as pd


def test_create_data_frame_from_dict():
    expected = ({'col3': ['', 'data4'], 'col2': ['data2', ''], 'col1': ['data1', 'data3']})
    details = [{'col1': 'data1', 'col2': 'data2'}, {'col1': 'data3', 'col3': 'data4'}]
    actual = create_data_frame_from_dict(details)

    assert actual.equals(pd.DataFrame(expected))
