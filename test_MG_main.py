import pandas as pd
from MG_main import load_dataset

# assinging a test data csv that has a very simple data with the from 1921 to 2023
test_data_csv = "test_organization.csv"


def test_load_data():
    # checking
    test_data = load_dataset(test_data_csv)
    assert test_data is not None


if __name__ == "__main__":
    test_load_data()
