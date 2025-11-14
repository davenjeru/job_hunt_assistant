import requests
from job_hunt_assistant.utils.config import USAJOBS_API_KEY
from job_hunt_assistant.utils.config import USAJOBS_USER_AGENT

def fetch_usajobs(keyword, location="remote", results_per_page=5):
    headers = {
        'User-Agent': USAJOBS_USER_AGENT,
        'Authorization-Key': USAJOBS_API_KEY
    }

    params = {
        'Keyword': keyword,
        'ResultsPerPage': results_per_page,
    }

    if location.lower().strip() == "remote":
        params['RemoteIndicator'] = True
    else:
        params['LocationName'] = location

    url = "https://data.usajobs.gov/api/Search"

    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        return (
            response.json()
            .get('SearchResult', {})
            .get('SearchResultItems', [])
        )

    return []

if __name__ == "__main__":
    jobs = fetch_usajobs("data analyst", "California", results_per_page=10)
    for job in jobs:
        title = job['MatchedObjectDescriptor']['PositionTitle']
        agency = job['MatchedObjectDescriptor']['OrganizationName']
        print(f"{title} at {agency}")