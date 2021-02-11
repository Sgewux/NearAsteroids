from tabulate import tabulate
import json
import requests
import datetime


class Scraper:
    def __init__(self, date_to_search):
        self.date_to_search = date_to_search
        self.home = f'https://api.nasa.gov/neo/rest/v1/feed?start_date={self.date_to_search}&end_date={self.date_to_search}&api_key=DEMO_KEY'

    def obtain_data(self):
        try:
            request = requests.get(self.home)
            data = json.loads(request.text)
       
        except:
            
            print('Something went wrong!')
        
        full_data = []

        for obj in data['near_earth_objects'][self.date_to_search]:
            asteroid_info = []
            asteroid_info.append(obj['name'])
            asteroid_info.append(str(obj['is_potentially_hazardous_asteroid']))
            asteroid_info.append(str(obj['estimated_diameter']['meters']['estimated_diameter_max']))
            asteroid_info.append(obj['close_approach_data'][0]['relative_velocity']['kilometers_per_second'])
            asteroid_info.append(obj['close_approach_data'][0]['miss_distance']['kilometers'])

            full_data.append(asteroid_info)
        
        return full_data



if __name__ == '__main__':
    current_date = datetime.datetime.now().strftime('%Y-%m-%d')
    asteroids_data = Scraper(current_date).obtain_data()
    print('Today\'s asteroids close to the Earth:\n')
    print(tabulate(asteroids_data, headers=['Name', 'Is potentially hazardous', 'Estimated diameter(m)', 'Relative velocity(km/s)', 'Miss distance(m)']))
    
    

