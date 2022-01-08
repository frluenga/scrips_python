import argparse
import logging
logging.basicConfig(level = logging.INFO)
import Article import Article
from base import Base,Engine,Session


def main(filename):
    Base.metadata.create_all(Engine)
    session = Session()
    articles = pd.read_csv(filename)

    for index,row in articles.iterrows():
        logger.info('loading article uid {} into db'.format(row['uid']))
        article = Article(row['uid'],row['body'],row['host'],
                            row['newspaper_uid'],row['n_tokens_body'],
                            row['n_tokens_title'],row['title'],row['url'])
            session.add(article)
    session.commit()
    session.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('filename',help='The file you want to load into the db',
                        type=str)
    