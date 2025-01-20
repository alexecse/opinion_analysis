import pandas as pd
import numpy as np

csv_file_path = 'data_bases/training.1600000.processed.noemoticon.csv' 
df = pd.read_csv(csv_file_path, encoding='latin1')  

apple_filtered_df = df[df[df.columns[-1]].str.contains(' apple ', case=False, na=False)]
random_apple_sample = apple_filtered_df.sample(n=150)

microsoft_filtered_df = df[df[df.columns[-1]].str.contains(' microsoft ', case=False, na=False)]
random_microsoft_sample = microsoft_filtered_df.sample(n=150)

twitter_filtered_df = df[df[df.columns[-1]].str.contains(' twitter ', case=False, na=False)]
random_twitter_sample = twitter_filtered_df.sample(n=150)

google_filtered_df = df[df[df.columns[-1]].str.contains(' google ', case=False, na=False)]
random_google_sample = google_filtered_df.sample(n=150)

output_file_path_apple = 'data_bases/apple.csv'
random_apple_sample.to_csv(output_file_path_apple, index=False)

output_file_path_microsoft = 'data_bases/microsoft.csv'
random_microsoft_sample.to_csv(output_file_path_microsoft, index=False)

output_file_path_twitter = 'data_bases/twitter.csv'
random_twitter_sample.to_csv(output_file_path_twitter, index=False)


output_file_path_google = 'data_bases/google.csv'
random_google_sample.to_csv(output_file_path_google, index=False)

# 0 - negativ 1 - neutral 2 - pozitiv