import pandas as pd

data = {
    'start_time': ['2025-06-25 08:30', '2025-06-25 17:45', '2025-06-26 09:00', '2025-07-01 10:15', 'invalid-date'],
    'end_time': ['2025-06-25 12:00', '2025-06-25 18:00', '2025-06-26 12:30', '2025-07-01 13:00', '2025-07-01 15:00']
}

df = pd.DataFrame(data)
df['start_time'] = pd.to_datetime(df['start_time'], errors='coerce') # coerce will print NA where data is invalid
df['end_time'] = pd.to_datetime(df['end_time'], errors='coerce')
print(df)

df['year'] = df['start_time'].dt.year
df['month'] = df['start_time'].dt.month
df['day'] = df['start_time'].dt.day
df['weekday'] = df['start_time'].dt.day_name()
df['hour'] = df['start_time'].dt.hour
df['duration'] = df['end_time'] - df['start_time']
df['duration_minutes'] = df['duration'].dt.total_seconds() / 60
print(df.to_string())

df_june = df[df['month'] == 6]
print(df_june)

df['next_day'] = df['start_time'] + pd.Timedelta(days=1)
print(df.to_string())

