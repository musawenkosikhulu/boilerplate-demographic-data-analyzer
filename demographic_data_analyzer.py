import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    col_names =['age','workclas','fnlwgt','education','education-num','marital-status','occupation','relationship','race','sex','capital-gain','hours-per-week','native-country','salary']
    df = pd.read_csv('adult.data.csv',names = col_names)

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df.race.str.split(expand=True).stack().value_counts()

    # What is the average age of men?
    average_age_men = df.loc[df['sex'] == 'Male','age'].mean()

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = ((df['native_country'] == 'United States').sum())/df.shape[0]*100

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = df['Education'].isin(['Bachelors','Masters','Doctorate'])
    lower_education = df['Education'].isin(~['Bachelors','Masters','Doctorate'])

    # percentage with salary >50K
    higher_education_rich = float(higher_education['higher_education'['salary']== '>50K']['salary'].count() / higher_education.shape[0])*100.0
    lower_education_rich = float(lower_education['lower_education'['salary']=='>50K']['salary'].count() / lower_education.shape[0])*100.0

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df[hours-per-week].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = df[df['hours-per-week'] == min_work].shape[0]

    rich_percentage = float(df[(df['hours-per-week'] == min_work) & (df['salary'] == '>50K')].shape[0] / num_min_workers)*100

    # What country has the highest percentage of people that earn >50K?
    highest_earning_country = df[df['salary'] == '>50K'].groupby('native-country')['native-country'].count().max()
    highest_earning_country_percentage = float((highest_earning_country / df.groupby('native-country')['native-country'].count()).max())*100

    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = []
    for (country, salary), sub_df in df.groupby(['native-country', 'salary']):
        top_IN_occupation.append(f"{country} {salary} {sub_df['occupation'].value_counts().keys()[0]}")

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
