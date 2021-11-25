import csv
import random

with open("quote_df.csv", mode="r") as df:
    reader = csv.reader(df)
    df_dict = {rows[0]:rows[1] for rows in reader}


def choose_quote(data):
    while True:
        quote, author = random.choice(list(data.items()))
        check_quote = f"'{quote}' \n\n-{author}"
        if len(check_quote) < 280:
            return check_quote
