import requests
import os
from datetime import datetime, timedelta

FR_PJ_HOST = os.getenv("FR_PJ_HOST")
FR_API_HOST = os.getenv("FR_API_HOST")
FR_API_TOKEN = os.getenv("FR_API_TOKEN")

class FreelancerBob:
    def __init__(self):
        self.s_time = round((datetime.now() - timedelta(minutes=5)).timestamp())
        self.e_time = round(datetime.now().timestamp())

    def format_pj(self, pj_obj):        
        return {
            "pj_id": pj_obj["id"],
            "owner_id": pj_obj["owner_id"],
            "pj_title": pj_obj["title"],
            "pj_url": f"{FR_PJ_HOST}/{pj_obj['seo_url']}",
            "submit_dt": datetime.fromtimestamp(pj_obj["submitdate"]),
            "updated_dt": datetime.fromtimestamp(pj_obj["time_updated"]),
            "pj_type": pj_obj["type"],
            "bid_p": pj_obj["bidperiod"],
            "pj_curr": pj_obj["currency"]["sign"],
            "pj_min_bdg": pj_obj["budget"]["minimum"],
            "pj_max_bdg": pj_obj["budget"]["maximum"],
            "bids": pj_obj["bid_stats"]["bid_count"],
            "avg_bid": round(pj_obj["bid_stats"]["bid_avg"], 2)
        }

    def fetch_owner(self):
        ...

    def fetch_projects(self):
        req_url = f"{FR_API_HOST}/projects/0.1/projects/all/"
        req_header = {
            "Content-Type": "application/json",
            "freelancer-oauth-v1": FR_API_TOKEN
        }
        req_data = {
            "filter": {
                "jobs": [13],
                "from_time": self.s_time,
                "to_time": self.e_time
            }
        }

        req_obj = requests.post(req_url, headers=req_header, json=req_data)
        req_status = req_obj.status_code

        if (req_status >= 200) & (req_status <= 226):
            resp_obj = req_obj.json()
            projects = resp_obj["result"]["projects"]

            pj_list = []

            for pj_obj in projects:
                pj_list.append(self.format_pj(pj_obj))