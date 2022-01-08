import argparse
import logging
import pandas as pd
import hashlib
from urllib.parse import urlparse
import re
from pandas._libs import missing
import nltk
from nltk.corpus import stopwords

logging.basicConfig(level = logging.INFO)
logger = logging.getLogger(__name__)


def main(filename):
    
    logger.info('Starting cleaning cleaning process')
    df = _read_data(filename)
    newspaper_uid = _extract_newspaper_uid(filename)
    df = _add_newspaper_uid_column(df,newspaper_uid)
    df = _extract_host(df)
    df = _fill_missing_titles(df)
    df = _generate_uids_for_row(df)
    df = _remove_lines(df)
    df = _tokenize_column(df, 'title')
    df = _tokenize_column(df, 'body')
    df = _remove_duplicate_entries(df, 'title')
    df = _drop_rows_with_missing_values(df)
    _save_data(df,filename)
    return df


def _save_data(df,filename):
    clean_filename = 'clean_{}'.format(filename)
    logger.info('Saving data at location: {}'.format(filename))
    df.to_csv(clean_filename,encoding='utf-8-sig')

def _drop_rows_with_missing_values(df):
    logger.info('Dropping rows with missing values')
    return df.dropna()


def _tokenize_column(df, column_name):
    logger.info('Calculating the number of unique tokens in {}'.format(column_name))
    stop_words = set(stopwords.words('spanish'))

    n_tokens =  (df
                 .dropna()
                 .apply(lambda row: nltk.word_tokenize(row[column_name]), axis=1)
                 .apply(lambda tokens: list(filter(lambda token: token.isalpha(), tokens)))
                 .apply(lambda tokens: list(map(lambda token: token.lower(), tokens)))
                 .apply(lambda word_list: list(filter(lambda word: word not in stop_words, word_list)))
                 .apply(lambda valid_word_list: len(valid_word_list))
            )

    df['n_tokens_' + column_name] = n_tokens

    return df

def _remove_duplicate_entries(df, column_name):
    logger.info('Removing duplicate entries')
    df.drop_duplicates(subset=[column_name], keep='first', inplace=True)

    return df


def _remove_lines(df):
    logger.info('Removing new lines from body')
    stripped_boddy = (
        df.apply(lambda row: row['body'],axis = 1)
        .apply(lambda body: list(body))
        .apply(lambda letters: list(map(lambda letter: letter.replace('\n',''),letters)))
        .apply(lambda letters: ''.join(letters))
    )

    df['body'] = stripped_boddy

    return df


def _generate_uids_for_row(df):
    logger.info('Generating uids for each row')
    uids = (
        df.apply(lambda row: hashlib.md5(bytes(row['url'].encode())),axis=1)
        .apply(lambda hash_object: hash_object.hexdigest())
    )
    df['uid'] = uids
    return df.set_index('uid')


def _fill_missing_titles(df):
    logger.info('Filling missing titles')
    filter = df['title'].isna()
    missing_title = (df[filter]['url']
                    .str.extract(r'(?P<missing_title>[^/]+)$')
                    .astype(str)
                    .applymap(lambda x: x.replace('-',' ')))

    df.loc[filter,'title'] = missing_title.loc[:,'missing_title']
    return df

def _extract_host(df):
    logger.info('Extracting host form urls')
    df['host'] =df['url'].apply(lambda url: urlparse(url).netloc)
    return df


def _add_newspaper_uid_column(df,newspaper_uid):

    logger.info('Filling newspaper_uid column with {}'.format(newspaper_uid))
    df['newspaper_uid'] = newspaper_uid
    return df


def _extract_newspaper_uid(filename):

    logging.info('Extracting news paper uid')
    newspaper_uid = filename.split('_')[0]
    logger.info('Newspaper uid detected {}'.format(newspaper_uid))
    return newspaper_uid

def _read_data(filename): 
    
    logger.info(f'Reading file {filename}')
    return pd.read_csv(filename)

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('filename',
                        help='The path to the dirty data',
                        type=str)

    args = parser.parse_args() 
    df = main(args.filename)

    print(df)