import pandas as pd
from MG_main import load_dataset, describe_data, find_min_and_max, create_graph


# assinging a test data csv that has a very simple data with the from 1921 to 2023
test_data_csv = "test_organization.csv"
test_data = load_dataset(test_data_csv)
column_of_int = test_data["Number of employees"]

column_of_int.mean


def test_load_data():
    test_data = load_dataset(test_data_csv)
    assert test_data is not None


def test_stats_describe():
    summary_stats = describe_data(column_of_int)
    assert (
        summary_stats
        == "This is the mean is 4964.86\nThis is the median is 4941.5\nThis is the standard deviation is 2850.8597994927136"
    )


def test_range():
    range_stats = find_min_and_max(column_of_int)
    assert range_stats is not None


if __name__ == "__main__":
    test_load_data()
    test_stats_describe()
    test_range()
