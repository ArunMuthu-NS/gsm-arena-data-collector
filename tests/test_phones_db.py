from data_requester.phones_db import load_processed_phone_links


def simulate_loaded_phone_data(tmp_path):
    d = tmp_path / "temp"
    d.mkdir()
    p = d / "temp.txt"
    p.write_text("a.php\nb.php")
    return p


def test_load_phone_names_returns_saved_phone_names(tmp_path):
    expected = ['a.php', 'b.php']
    actual = load_processed_phone_links(simulate_loaded_phone_data(tmp_path))
    assert actual == expected
