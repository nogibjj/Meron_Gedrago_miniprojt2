# import packages
import pandas as pd
import matplotlib.pyplot as plt


# create a function to read the dataset and filter the
def load_dataset(dataset):
    data_set = pd.read_csv(dataset)
    return data_set


# calculate and print the summary statistics
def describe_data(data):
    mean = data["ESTIMATE"].mean()
    median = data["ESTIMATE"].median()
    std = data["ESTIMATE"].std()
    print(f"This is the mean is {mean}")
    print(f"This is the median is {median}")
    print(f"This is the standard deviation is {std}")


# create a function to get the median of the data
def find_min_and_max(data):
    data_max = data["ESTIMATE"].max()
    data_min = data["ESTIMATE"].min()
    print(f"The max is {data_max} and the min is {data_min}")


def create_graph(data):
    # Create visualization
    plt.scatter(data["YEAR"], data["ESTIMATE"])
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
    describe_data(data)
    find_min_and_max(data)
    create_graph(data)
