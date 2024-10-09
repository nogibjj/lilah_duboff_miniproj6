"""asserts if data exists, if a database was created
and if the CRUD operations returned a result"""

from SQL_files.query import create, read, update, delete, query_1, query_2

payload1 = (
    "EMP0001",
    32,
    "Non-binary",
    "HR",
    "Healthcare",
    13,
    "Hybrid",
    47,
    7,
    2,
    "Medium",
    "Depression",
    "No",
    "Decrease",
    1,
    "Unsatisfied",
    1,
    "Weekly",
    "Good",
    "Europe",
)


def test_create():
    table_name = "remote_health"
    data = "remotehealthDB.db"
    result = create(payload1, data, table_name)
    assert result == "Record inserted successfully"


def test_read():
    result = read("remotehealthDB.db", "remote_health")
    assert isinstance(result, list)
    assert len(result) > 0


def test_update():
    ID_number = "EMP0001"
    column = "Age"
    new_value = "EMP0000"

    result = update("remotehealthDB.db", "remote_health", column, new_value, ID_number)
    assert result == "Record updated successfully!"


def test_delete():
    ID_number = "EMP0008"
    result = delete("remotehealthDB.db", "remote_health", ID_number)
    assert result == "Record deleted successfully!"


def test_query_1():
    result_1 = query_1()
    assert result_1 is not None


def test_query_2():
    result_2 = query_2()
    assert result_2 is not None


if __name__ == "__main__":
    test_read()
    test_update()
    test_delete()
    test_query_1()
    test_query_2()