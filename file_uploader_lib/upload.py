from .db_config.configure import connect
from .client_config.client import connect_minio, get_file_object
import pandas as pd
from .db_config.query import prepare_query
import datetime


def save_data_from_uploader(file_obj_name: str, column_list: list, table_name: str, db_dsn: str, minio_host,
                            minio_access_key, minio_secret_key, bucket_name: str):

    print(file_obj_name," ", minio_host)
    cur, conn = connect(db_dsn)
    minio_client = connect_minio(minio_host, minio_access_key, minio_secret_key, False)
    print(minio_client)
    if not minio_client[1]:
        return -1, False
    else:
        file = get_file_object(bucket_name, file_obj_name, minio_client[0])
        query_str = prepare_query(table_name=table_name, column_list=column_list)
        data = pd.read_excel(file.data)
        value_list = []
        for idx, row in data.iterrows():
            data_tuple = ()
            for col in range(0, len(row)):
                data_tuple += (str(row[col]),)
            data_tuple += (str(datetime.datetime.now()), str(datetime.datetime.now()))
            value_list.append(data_tuple)
        # print(query_str)
        print("NWEQ", value_list)
        try:
            cur.executemany(query_str, value_list)
            conn.commit()
        except:
            conn.rollback()

        return cur.rowcount, True
