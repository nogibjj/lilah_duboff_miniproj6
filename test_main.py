"""
Test goes here

"""
import subprocess


def test_extract_data():
    """tests extract()"""
    result = subprocess.run(
        ["python", "main.py", "extract"],
        capture_output=True,
        text=True,
        check=True,
    )
    assert result.returncode == 0
    assert "Extracting data..." in result.stdout


def test_transform():
    """tests transfrom"""
    result = subprocess.run(
        ["python", "main.py", "transform"],
        capture_output=True,
        text=True,
        check=True,
    )
    assert result.returncode == 0
    assert "Transforming data..." in result.stdout


def test_complex_query():
    """tests general_query"""
    result = subprocess.run(
        [
            "python",
            "main.py",
            "complex_query",
            """
                SELECT r1.Industry, COUNT(r1.Employee_ID) AS count_of_employees, 
                AVG(r1.Hours_Worked_Per_Week) AS avg_hours_worked, 
                AVG(CASE WHEN r2.Stress_Level = 'High' 
                THEN 1 WHEN r2.Stress_Level = 'Medium' 
                THEN 2 WHEN r2.Stress_Level = 'Low' 
                THEN 3 ELSE NULL END) AS avg_stress_level 
                FROM remote_health1 AS r1 
                JOIN remote_health2 AS r2 ON r1.Employee_ID = r2.Employee_ID 
                GROUP BY r1.Industry 
                ORDER BY count_of_employees DESC;
            """,
        ],
        capture_output=True,
        text=True,
        check=True,
    )
    assert result.returncode == 0
   


if __name__ == "__main__":
    test_extract_data()
    test_transform()
    test_complex_query()
