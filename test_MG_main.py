import pandas as pd
from MG_main import load_dataset, describe_data, find_min_and_max, create_graph

# assinging a test data csv that has a very simple data with the from 1921 to 2023
test_data_csv = "test_organization.csv"
test_data = load_dataset(test_data_csv)


def test_load_data():

    test_data = load_dataset(test_data_csv)
    assert test_data is not None


def test_summary_stats(input_data):
    summary_stats = describe_data(input_data)
    range_stats = find_min_and_max(input_data)
    assert (
        summary_stats
        == "This is the mean is 4964.86 \n This is the median is 4941.5 \n This is the standard deviation is 2850.85"
    )
    assert range_stats is not None


if __name__ == "__main__":
    test_load_data()
    test_data = load_dataset(test_data_csv)
    column_of_int = test_data["Number of employees"]
    test_summary_stats(column_of_int)
