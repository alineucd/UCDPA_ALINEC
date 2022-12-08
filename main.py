import pandas as pd

def read_data():
    # Read the data
    df = pd.read_excel('uk_air_passengers.xlsx')

    # Print the first 5 rows of the data
    print(df.head())


    # clean the data
    df = df.dropna()

    # Print the first 5 rows of the data
    print(df.head())

    return df


def main():
    df = read_data()

    # convert dataset to hashes
    df_hash = df.to_dict('records')

    # Print the first 5 rows of the data
    print(df_hash[:5])


    # QUESTION 1
    # What is the average number of passengers per month?

    # group the data by month
    df_grouped = df.groupby('month')

    # calculate the mean of the grouped data
    df_mean = df_grouped.mean()

    # Print the first 5 rows of the data
    print(df_mean.head())


    # QUESTION 2
    # What is the average number of passengers per month for each year?

    # group the data by month and year
    df_grouped = df.groupby(['month', 'year'])

    # calculate the mean of the grouped data
    df_mean = df_grouped.mean('Passengers')

    # Print the first 5 rows of the data
    print(df_mean)



    # QUESTION 3
    # Use matplot lib to compare the number of passengers each year

    # import matplotlib
    import matplotlib.pyplot as plt

    # group the data by year
    df_grouped = df.groupby('year')

    # calculate the mean of the grouped data
    df_mean = df_grouped.mean('Passengers')

    # plot the data
    df_mean.plot(kind='line', y='Passengers')

    # show the plot
    plt.show()


    # QUESTION 4
    # Rank the months by the number of passengers and plot the results in a column bar chart

    # group the data by month
    df_grouped = df.groupby('month')

    # calculate the mean of the grouped data
    df_mean = df_grouped.mean('Passengers')

    # sort the data
    df_sorted = df_mean.sort_values(by='Passengers', ascending=False)

    # plot the data
    df_sorted.plot(kind='bar', y='Passengers')

    # show the plot
    plt.show()


    # QUESTION 5
    # Display the total passengers for each year in a pie chart

    # group the data by year
    df_grouped = df.groupby('year')

    # calculate the mean of the grouped data
    df_mean = df_grouped.mean('Passengers')

    # plot the data and set the labels, and show values as percentages
    df_mean.plot(kind='pie', y='Passengers', labels=df_mean.index, autopct='%1.1f%%')

    # show the plot
    plt.show()




    # QUESTION 6
    # Display the 3 months with the highest number of passengers

    # group the data by month
    df_grouped = df.groupby('month')

    # calculate the mean of the grouped data
    df_mean = df_grouped.mean('Passengers')

    # sort the data
    df_sorted = df_mean.sort_values(by='Passengers', ascending=False)

    # print the top 3 rows
    print('The 3 months with the highest number of passengers are: ')
    print(df_sorted.head(3))


    # QUESTION 7

    # Display the 3 months with the lowest number of passengers

    # group the data by month
    df_grouped = df.groupby('month')

    # calculate the mean of the grouped data
    df_mean = df_grouped.mean('Passengers')

    # sort the data
    df_sorted = df_mean.sort_values(by='Passengers', ascending=True)

    # print the top 3 rows
    print(df_sorted.head(3))


    # QUESTION 8
    # Export the months with the highest number of passengers to a csv file

    # group the data by month
    df_grouped = df.groupby('month')

    # calculate the mean of the grouped data
    df_mean = df_grouped.mean('Passengers')

    # sort the data
    df_sorted = df_mean.sort_values(by='Passengers', ascending=False)

    # export the data to a csv file
    df_sorted.to_csv('top_months.csv')


if __name__ == '__main__':
    main()

