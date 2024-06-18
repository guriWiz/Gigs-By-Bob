import requests
import os
from datetime import datetime, timedelta
from .logger import LOGGER

BOB_SLEEP_MINS = int(os.getenv("BOB_SLEEP_MINS", 5))

FR_HOST = os.getenv("FR_HOST")
FR_PJ_HOST = os.getenv("FR_PJ_HOST")

FR_API_HOST = os.getenv("FR_API_HOST")
FR_API_TOKEN = os.getenv("FR_API_TOKEN")

class FreelancerBob:
    def __init__(self):
        self.req_headers = {
            "Content-Type": "application/json",
            "freelancer-oauth-v1": FR_API_TOKEN
        }

        self.s_time = round((datetime.now() - timedelta(minutes=BOB_SLEEP_MINS)).timestamp())
        self.e_time = round(datetime.now().timestamp())

        LOGGER.info(f"From time: {self.s_time}")
        LOGGER.info(f"To time: {self.e_time}")

    def format_user(self, user_obj):
        u_name = user_obj["username"]
        
        return {
            "u_name": u_name,
            "u_avatar": f"{FR_HOST}{user_obj["avatar"]}",
            "u_url": f"{FR_HOST}/u/{u_name}"
        }
    
    def format_skills(self, pj_skills):
        return ", ".join([s["name"] for s in pj_skills])

    def format_pj(self, pj_obj, users):    
        pj_id = pj_obj["id"]
        owner_id = pj_obj["owner_id"]

        pj_user = users[str(owner_id)]
        pj_user = self.format_user(pj_user)

        pj_skills = self.format_skills(pj_obj["jobs"])

        return {
            "pj_id": pj_id,
            "pj_user": {
                "u_id": owner_id
            } | pj_user,
            "pj_title": pj_obj["title"],
            "pj_desc": pj_obj["description"],
            "pj_url": f"{FR_PJ_HOST}/{pj_obj['seo_url']}",
            "pj_type": pj_obj["type"],
            "bid_p": pj_obj["bidperiod"],
            "pj_curr": pj_obj["currency"]["sign"],
            "pj_min_bdg": pj_obj["budget"]["minimum"],
            "pj_max_bdg": pj_obj["budget"]["maximum"],
            "bids": pj_obj["bid_stats"]["bid_count"],
            "avg_bid": round(pj_obj.get("bid_stats", {}).get("bid_avg", 0), 2),
            "pj_skills": pj_skills,
            "submit_dt": datetime.fromtimestamp(pj_obj["submitdate"]),
            "update_dt": datetime.fromtimestamp(pj_obj["time_updated"])
        }

    def fetch_projects(self):
        req_url = f"{FR_API_HOST}/projects/0.1/projects/all/"
        req_data = {
            "filter": {
                "jobs": [13],
                "from_time": self.s_time,
                "to_time": self.e_time,
            },
            "projection": {
                "result_projection": {
                    "users_projection": {
                        "username": True, "avatar": True, "email": True, "reputation": True, "employer_reputation": True
                    },
                    "full_description": True,
                    "job_details": True
                }
            }
        }

        req_obj = requests.post(req_url, headers=self.req_headers, json=req_data)
        
        pj_list = []
        req_status = req_obj.status_code

        if (req_status >= 200) & (req_status <= 226):
            resp_obj = req_obj.json()

            result = resp_obj["result"]
            projects = result["projects"]
            users = result["users"]
            pj_count = result["total_count"]

            LOGGER.info(f"Projects count: {pj_count}")

            for pj_obj in projects:
                pj_list.append(self.format_pj(pj_obj, users))

        else:
            LOGGER.error(f"Projects request failed with status code: {req_status}")
            LOGGER.error(f"{req_obj.text}")

        LOGGER.info(f"Projects list: {pj_list}")
        
        return pj_list