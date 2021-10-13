import pandas as pd


def percent(dividend, divisor):
    return round(100 * dividend / divisor, 1)


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("adult.data.csv")

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df.groupby('race').size().sort_values(ascending=False)

    # What is the average age of men?
    average_age_men = round(df.groupby('sex').mean()['age'].loc['Male'], 1)

    # What is the percentage of people who have a Bachelor's degree?
    bachelors = df['education'].value_counts()['Bachelors']
    total = df['education'].size
    percentage_bachelors = percent(bachelors, total)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education_list = ['Bachelors', 'Masters', 'Doctorate']
    higher_education_counts = df[['education', 'salary']].value_counts()[higher_education_list]
    higher_education_sum = higher_education_counts.sum()
    lower_education_sum = total - higher_education_sum

    # percentage with salary >50K
    higher_education_rich_sum = higher_education_counts.groupby(level=1).sum().loc['>50K']
    higher_education_rich = percent(higher_education_rich_sum, higher_education_sum)

    total_rich_sum = df[['education', 'salary']].value_counts().groupby(level=1).sum()['>50K']
    lower_education_rich_sum = total_rich_sum - higher_education_rich_sum
    lower_education_rich = percent(lower_education_rich_sum, lower_education_sum)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    hours_salary_df = df[['hours-per-week', 'salary']]

    num_min_workers_rich = hours_salary_df[(hours_salary_df['hours-per-week'] == min_work_hours) & (hours_salary_df['salary'] == '>50K')].size
    num_min_workers = hours_salary_df[hours_salary_df['hours-per-week'] == min_work_hours].size

    rich_percentage = percent(num_min_workers_rich, num_min_workers)

    # What country has the highest percentage of people that earn >50K?
    rich_per_country = df[df['salary'] == '>50K']['native-country'].value_counts()
    total_per_country = df['native-country'].value_counts()
    sorted_rich_countries = percent(rich_per_country, total_per_country).sort_values(ascending=False)

    highest_earning_country = sorted_rich_countries.index[0]
    highest_earning_country_percentage = sorted_rich_countries.iloc[0]

    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]['occupation'].value_counts().index[0]

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
