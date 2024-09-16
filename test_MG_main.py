import pandas as pd
from MG_main import load_dataset, describe_data, find_min_and_max, create_graph

# assinging a test data csv that has a very simple data with the from 1921 to 2023
test_data_csv = "test_organization.csv"


def test_load_data():
    # checking
    test_data = load_dataset(test_data_csv)
    assert test_data is not None


def test_summary_stats():
    summary_stats = describe_data()
    range_stats = find_min_and_max()
    assert summary_stats is not None
    assert range_stats is not None


if __name__ == "__main__":
    test_load_data()
