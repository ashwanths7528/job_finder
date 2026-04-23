from app.scraper import fetch_jobs, get_job_date
from app.storage import load_jobs, save_jobs, get_new_jobs
from app.notifier import send_message

from datetime import datetime, timedelta
from app.scraper import fetch_jobs, get_job_date
from app.storage import load_jobs, save_jobs, get_new_jobs
from app.notifier import send_message

def run():
    jobs = fetch_jobs(pages=1)

    print("Total jobs fetched:", len(jobs))

    for job in jobs[:3]:
        print("\nTITLE:", job["title"])

        post_date = get_job_date(job["link"])
        print("DATE:", post_date)

if __name__ == "__main__":
    run()