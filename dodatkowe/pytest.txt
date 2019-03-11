1. Proszę zainstalować moduł pytest oraz pytest-html
pip install pytest pytest-html

2. Proszę uruchamiać nasze testy za pomocą pytesta:
pytest test_check_universities.py

3. Proszę uruchamiać nasze testy za pomocą pytesta generując raport html:
pytest test_check_universities.py --html=report.html

Każdy plik musi się zaczynać od słowa "test_"
