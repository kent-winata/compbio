import requests
import random
import json
import time

# Get a random anime or manga from AniList
def get_random_anilist(media_type="ANIME"):
    url = "https://graphql.anilist.co"
    query = """
    query ($id: Int, $type: MediaType) {
      Media(id: $id, type: $type) {
        id
        title {
          romaji
          english
          native
        }
        description
        episodes
        chapters
        genres
        averageScore
      }
    }
    """
    for i in range(5): 
        random_id = random.randint(1, 200000)
        variables = {"id": random_id, "type": media_type}
        
        try:
            response = requests.post(url, json={'query': query, 'variables': variables})
            if response.status_code == 200:
                data = response.json()
                if 'data' in data and data['data']['Media']:
                    return data['data']['Media']
        except:
            pass
        time.sleep(1) 
    return None
    
def save_to_file(data, filename="anilist_recommendation.json"):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=2)
    print("Saved recommendation to", filename)

# Main program
media_type = "ANIME"  # Set to "MANGA" for manga recommendations
recommendation = get_random_anilist(media_type)

if recommendation:
    save_to_file(recommendation)
else:
    print("Couldn't find a recommendation.")
