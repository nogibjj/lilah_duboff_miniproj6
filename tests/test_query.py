"""asserts if data exists, if a database was created
and if the CRUD operations returned a result"""

from SQL_files.complex_query import complex_query


def test_complex_query():
    """tests general_query"""
    result = complex_query(test_query)
    assert result == "Successfully completed query!"   