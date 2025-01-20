import pandas as pd

corpus_df = pd.read_csv('twitter_corpus-master/full-corpus.csv')

valid_corpus_sentiments = ['positive', 'neutral', 'negative']
filtered_corpus_df = corpus_df[corpus_df['Sentiment'].isin(valid_corpus_sentiments)]

sentiment_corpus_mapping = {'negative': 0, 'neutral': 1, 'positive': 2}
filtered_corpus_df.loc[:, 'Sentiment'] = filtered_corpus_df['Sentiment'].replace(sentiment_corpus_mapping)
filtered_corpus_df['Year'] = 2011

output_corpus_df = filtered_corpus_df[['Topic', 'Sentiment', 'TweetDate', 'Year']]

output_corpus_df.to_csv('twitter_corpus-master/final-corpus.csv', index=False)

apple_df = pd.read_csv('data_bases/apple.csv')
google_df = pd.read_csv('data_bases/google.csv')
microsoft_df = pd.read_csv('data_bases/microsoft.csv')
twitter_df = pd.read_csv('data_bases/twitter.csv')

def process_df(df, company_name):
    df['target'] = df['target'].replace(4, 2)
    df_processed = df[['target', 'date']].copy()
    df_processed['Topic'] = company_name
    df_processed = df_processed.rename(columns={'target': 'Sentiment', 'date': 'TweetDate'})
    df_processed['Year'] = 2009
    df_processed = df_processed[['Topic', 'Sentiment', 'TweetDate', 'Year']]
    return df_processed

apple_processed = process_df(apple_df, 'apple')
google_processed = process_df(google_df, 'google')
microsoft_processed = process_df(microsoft_df, 'microsoft')
twitter_processed = process_df(twitter_df, 'twitter')

final_df = pd.concat([apple_processed, google_processed, microsoft_processed, twitter_processed])

final_df.to_csv('data_bases/combined_data.csv', index=False)

final_combined_df = pd.concat([final_df, output_corpus_df], ignore_index=True)

final_combined_df.to_csv('data_bases/final.csv', index=False)

print("CSV-ul a fost creat cu succes!")
