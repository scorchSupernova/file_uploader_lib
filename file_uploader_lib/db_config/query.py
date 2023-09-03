def prepare_query(table_name: str, column_list: list) -> str:
    column_list = [val for val in column_list if val != "id"]

    value_list = ['%s' for val in column_list]

    query_str = "INSERT INTO " + table_name + " (" + ', '.join(column_list) + ") VALUES (" + ', '.join(value_list) + ")"
    return query_str
