# Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Simulated sample dataset (similar structure)
data = {
    'Severity': [2, 3, 2, 4, 2, 3, 2, 4, 3, 2],
    'Start_Time': ['2023-06-01 08:00:00', '2023-06-01 18:30:00', '2023-06-02 07:15:00',
                   '2023-06-02 23:00:00', '2023-06-03 09:30:00', '2023-06-03 16:00:00',
                   '2023-06-04 06:45:00', '2023-06-04 22:15:00', '2023-06-05 15:00:00',
                   '2023-06-05 11:30:00'],
    'Weather_Condition': ['Clear', 'Rain', 'Cloudy', 'Snow', 'Clear', 'Rain',
                          'Fog', 'Clear', 'Rain', 'Clear'],
    'Road_Condition': ['Dry', 'Wet', 'Dry', 'Snowy', 'Dry', 'Wet', 'Foggy', 'Dry', 'Wet', 'Dry'],
    'City': ['New York', 'Los Angeles', 'Chicago', 'New York', 'Chicago', 'Houston',
             'Phoenix', 'Philadelphia', 'San Antonio', 'San Diego']
}

df = pd.DataFrame(data)

# Convert Start_Time to datetime
df['Start_Time'] = pd.to_datetime(df['Start_Time'])

# Extract hour and day of week
df['Hour'] = df['Start_Time'].dt.hour
df['Day_of_Week'] = df['Start_Time'].dt.day_name()

# Display data
print(df.head())

# Visualize Severity Distribution
plt.figure(figsize=(6,4))
sns.countplot(x='Severity', data=df)
plt.title("Accident Severity Distribution")
plt.show()

# Accidents by Hour of Day
plt.figure(figsize=(8,5))
sns.countplot(x='Hour', data=df)
plt.title("Accidents by Hour of Day")
plt.show()

# Accidents by Weather Condition
plt.figure(figsize=(8,5))
sns.countplot(x='Weather_Condition', data=df)
plt.title("Accidents by Weather Condition")
plt.xticks(rotation=45)
plt.show()

# Accidents by Road Condition
plt.figure(figsize=(8,5))
sns.countplot(x='Road_Condition', data=df)
plt.title("Accidents by Road Condition")
plt.xticks(rotation=45)
plt.show()

# Accidents by Day of the Week
plt.figure(figsize=(8,5))
sns.countplot(x='Day_of_Week', data=df, order=[
    'Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'])
plt.title("Accidents by Day of the Week")
plt.xticks(rotation=45)
plt.show()

# Accidents by City (Hotspots)
plt.figure(figsize=(8,5))
sns.countplot(y='City', data=df, order=df['City'].value_counts().index)
plt.title("Accident Hotspots by City")
plt.show()
