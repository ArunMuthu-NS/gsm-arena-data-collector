from data_requester.phones_db import load_processed_phone_links, store_phone_names


def simulate_loaded_phone_data(tmp_path):
    d = tmp_path / 'temp'
    d.mkdir()
    p = d / 'temp.txt'
    p.write_text('a.php\nb.php\n')
    return p


def test_load_phone_names_returns_saved_phone_names(tmp_path):
    expected = ['a.php', 'b.php']
    actual = load_processed_phone_links(simulate_loaded_phone_data(tmp_path))
    assert actual == expected


def test_store_phone_names_get_saved(tmp_path):
    file_path = simulate_loaded_phone_data(tmp_path)
    store_phone_names(['c.php', 'd.php'], file_path)
    expected = ['a.php', 'b.php', 'c.php', 'd.php']

    actual = load_processed_phone_links(file_path)

    assert actual == expected
