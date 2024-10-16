install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

format:
	black *.py

lint:
	ruff check *.py 
	
test:
	python -m pytest -vv test_main.py

check:
	python main.py
	git config --local user.email "action@github.com"; \
	git config --local user.name "Github Action"; \
	git add .; \
	git commit -m "test"; \
	git push; \

deploy:
	#deploy goes here

extract: 
	python main.py extract

transform:
	python main.py transform

query: 
	python main.py complex_query "SELECT r1.Industry, COUNT(r1.Employee_ID) AS count_of_employees, AVG(r1.Hours_Worked_Per_Week) AS avg_hours_worked, AVG(CASE WHEN r2.Stress_Level = 'High' THEN 1 WHEN r2.Stress_Level = 'Medium' THEN 2 WHEN r2.Stress_Level = 'Low' THEN 3 ELSE NULL END) AS avg_stress_level FROM remote_health1 AS r1 JOIN remote_health2 AS r2 ON r1.Employee_ID = r2.Employee_ID GROUP BY r1.Industry ORDER BY count_of_employees DESC;"

