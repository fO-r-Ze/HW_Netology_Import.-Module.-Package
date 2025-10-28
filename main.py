from datetime import datetime
from application.db.people import get_employees
from application.salary import calculate_salary
import tqdm

def get_date():
    print(datetime.now())


if __name__ == "__main__":
    get_date()
    get_employees()
    calculate_salary()
