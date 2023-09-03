from minio import Minio


def connect_minio(host: str, access_key: str, secret_key: str, secure: bool):
    try:
        minio_client = Minio(
            host,
            access_key,
            secret_key,
            secure=secure
        )
    except Exception as e:
        print(e)
        return None, False
    return minio_client, True


def get_file_object(bucket_name: str, object_name: str, client):
    if client.bucket_exists(bucket_name):
        file_obj = client.get_object(bucket_name, object_name)
        return file_obj
    return None
