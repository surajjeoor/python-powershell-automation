import pandas as pd
import requests
from datetime import datettime

#fetch data from web api
log_url = "https://api.example.com/data"
response = requests.get(log_url)
data = response.json()

#process the data in pandas dataframe
df = pd.DataFrame(data)
df['timestamp'] = pd.to_datetime(df['timestamp'])

failed_logins = df[df['status'] == 'failed']

#generate summary report
summary = failed_logins.groupby(failed_logins['timestamp'].dt.date).size().reset_index(name='failed_attempts')
summary_file = 'failed_login_summary.csv'
summary.to_csv(summary_file, index=False)
print(f"Summary report saved to {summary_file}")