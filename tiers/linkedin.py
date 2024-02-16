import os

import requests


def scrape_linkedin_profile(linkedin_profile_url:str):
    """
    Scrapper des informations des profiles LinkeDin
    :param linkedin_profile_url:
    :return:
    """
    api_key = os.environ.get('PROXYCRUL_API_KEY')
    headers = {'Authorization': 'Bearer ' + api_key}
    api_endpoint = 'https://nubela.co/proxycurl/api/v2/linkedin'
    params = {

        'linkedin_profile_url': linkedin_profile_url,

    }
    response = requests.get(api_endpoint,
                            params=params,
                            headers=headers)

    data= response.json()

    data={
        k:v
        for k,v in data.items()
        if v not in ([],"",None) and k not in ["people_also_viewed","certifications"]
    }
    if data.get('groups'):
        for group_dict in data.get('groups'):
            group_dict.pop("profile_pic_url")
    return data