import os

from django.core.management import BaseCommand
import pandas as pd
from sqlalchemy import create_engine
import psycopg2
engine = create_engine(os.getenv('PSQL_SQLALCH'))


def data_file():

    with pd.ExcelFile('quests.xlsx') as xls:
        for sheet_name in xls.sheet_names:
            sheets(sheet_name, xls)
            # print(sheet_name)


def sheets(data, file):
    if data == 'База':
        df = pd.read_excel(file, 'База')
        df.to_sql(name='tg_message', con=engine, if_exists='append', index=False)
        print('asd')

    # elif data == 'Sheet2':
    #     df = pd.read_excel(xls)
    #     df.to_sql(name='tg_message', con=engine, if_exists='append', index=False)
    #
    # elif data == 'Sheet3':
    #     df = pd.read_excel(xls)
    #     df.to_sql(name='tg_message', con=engine, if_exists='append', index=False)


class Command(BaseCommand):
    help = 'import_bd'

    def handle(self, *args, **options):
        data_file()

        # d = sheets(data=data, file='quests.xlsx')
