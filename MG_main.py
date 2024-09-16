# import packages
import pandas as pd
import matplotlib.pyplot as plt


# create a function to read the dataset and filter the
def load_dataset(dataset):
    data_set = pd.read_csv(dataset)
    return data_set


# calculate and print the summary statistics
def describe_data(input_data):
    mean = input_data.mean()
    median = input_data.median()
    std = input_data.std()
    return (
        f"The mean is {mean}; the median is {median}; the standard deviation is {std}"
    )


# create a function to get the median of the data
def find_min_and_max(input_data):
    data_max = input_data.max()
    data_min = input_data.min()
    return f"The max is {data_max} and the min is {data_min}"


def create_graph(input_data):
    # Create visualization
    plt.scatter(input_data["YEAR"], input_data["ESTIMATE"])
    plt.xlabel("Year")
    plt.ylabel("Deaths per 100,000 resident population")
    plt.title("Death rates from overdose over year")
    plt.xticks(range(int(data["YEAR"].min()), int(data["YEAR"].max()), 2))
    plt.show()


if __name__ == "__main__":
    loaded_data = load_dataset(
        "https://data.cdc.gov/api/views/95ax-ymtc/rows.csv?accessType=DOWNLOAD"
    )
    # furthering the cleaning this specific dataset
    data = loaded_data[
        (loaded_data["STUB_NAME"] == "Total")
        & (loaded_data["AGE"] == "All ages")
        & (loaded_data["PANEL"] == "All drug overdose deaths")
        & (loaded_data["UNIT"] == "Deaths per 100,000 resident population, crude")
    ]
    interested_column = data["ESTIMATE"]
    print(describe_data(interested_column))
    print(find_min_and_max(interested_column))
    create_graph(data)
