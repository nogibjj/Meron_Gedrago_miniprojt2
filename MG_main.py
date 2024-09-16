# import packages
import pandas as pd
import matplotlib.pyplot as plt


# create a function to read the dataset and filter the
def load_dataset(dataset):
    data_set = pd.read_csv(dataset)
    return data_set


# create a function to get the mean of the data
def create_mean():
    mean = data["ESTIMATE"].mean()
    return f"This is the mean is {mean}"


# create a function to get the median of the data
def create_median():
    median = data["ESTIMATE"].median()
    return f"This is the median is {median}"


# create a function to get the median of the data
def create_std():
    std = data["ESTIMATE"].std()
    return f"This is the standard deviation is {std}"


# create a function to get the median of the data
def find_min_and_max():
    data_max = data["ESTIMATE"].max()
    data_min = data["ESTIMATE"].min()
    return f"The max is {data_max} and the min is {data_min}"


def create_graph():
    # Create visualization
    plt.scatter(data["YEAR"], data["ESTIMATE"])
    plt.xlabel("Year")
    plt.ylabel("Deaths per 100,000 resident population")
    plt.title("Death rates from overdose over year")
    plt.xticks(range(int(data["YEAR"].min()), int(data["YEAR"].max()), 2))
    plt.show()


if __name__ == "__main__":
    data = load_dataset(
        "https://data.cdc.gov/api/views/95ax-ymtc/rows.csv?accessType=DOWNLOAD"
    )
    # furthering the cleaning this specific dataset
    data = data[
        (data["STUB_NAME"] == "Total")
        & (data["AGE"] == "All ages")
        & (data["PANEL"] == "All drug overdose deaths")
        & (data["UNIT"] == "Deaths per 100,000 resident population, crude")
    ]
    create_mean()
    create_median()
    create_std()
    find_min_and_max()
    create_graph()
