from dotenv import load_dotenv
load_dotenv()

from bob.freelancer import FreelancerBob

if __name__ == '__main__':
    fb = FreelancerBob()
    fb.fetch_projects()