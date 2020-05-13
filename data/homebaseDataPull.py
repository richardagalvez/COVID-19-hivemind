from datetime import datetime
import pandas as pd

# data copied (literally) from frome https://joinhomebase.com/data/covid-19/
workers = pd.read_clipboard()
workers.index = workers.index + 1
workers.loc[0] = workers.columns
workers.sort_index(inplace=True)

may_dates   = [f'5-{day}-2020' for day in range(11, 0, -1)]
april_dates = [f'4-{day}-2020' for day in range(30, 0, -1)]
march_dates = [f'3-{day}-2020' for day in range(31, 0, -1)]

dates = may_dates + april_dates + march_dates
workers.columns = ['msa'] + dates
workers.set_index('msa', inplace=True)
for column in workers.columns: 
    workers[column] = pd.to_numeric(workers[column].str.replace('%', ''))
workers = workers.T
workers.index = pd.to_datetime(workers.index)
workers.sort_index(inplace=True)
workers.index.name = 'cal_dt'
workers.to_csv(f'number_of_hourly_employee.csv')

# workers = pd.read_csv(f'number_of_hourly_employees_{datetime.today().date()}.csv').set_index('cal_dt')
# workers.index = pd.to_datetime(workers.index)