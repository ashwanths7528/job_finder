from datetime import datetime
from app.scraper import fetch_jobs, get_job_date
from app.storage import load_jobs, save_jobs, get_new_jobs
from app.notifier import send_message

def run():
    old_jobs = load_jobs()

    jobs = fetch_jobs(pages=2)
    print("Total jobs fetched:", len(jobs))

    today = datetime.now().date()
    today_jobs = []

   for job in jobs[:5]:
    try:
        post_date = get_job_date(job["link"])
    except Exception as e:
        print("Error:", e)
        post_date = None

    print("\nTITLE:", job["title"])
    print("DATE:", post_date)

    if post_date == today:
        today_jobs.append(job)
    # ✅ save jobs
    save_jobs(today_jobs)