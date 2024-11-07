import requests
import json
import random
import time

# Function to get a random recommendation from AniList
def get_random_recommendation(media_type="ANIME"):
    """
    Fetch a random recommendation from AniList by querying a random ID.
    Args:
    - media_type (str): Type of media, either 'ANIME' or 'MANGA'.
    
    Returns:
    - dict: A dictionary with information about the recommended title.
    """
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
        status
        genres
        averageScore
        startDate {
          year
          month
          day
        }
      }
    }
    """
    max_attempts = 10
    attempt = 0
    while attempt < max_attempts:
        random_id = random.randint(1, 200000)
        variables = {
            "id": random_id,
            "type": media_type
        }
        
        try:
            response = requests.post(url, json={'query': query, 'variables': variables})
            response.raise_for_status()
            data = response.json()
    
            if 'data' in data and data['data']['Media']:
                return data['data']['Media']
        except requests.exceptions.RequestException as e:
            print(f"Attempt {attempt + 1}: Error querying AniList API: {e}")
        
        attempt += 1

    return None

# Function to write the recommendation to a file
def write_recommendation_to_file(info, filename):
    """
    Write media recommendation information to a specified file.
    Args:
    - info (dict): The media recommendation information.
    - filename (str): The name of the output file.
    """
    try:
        with open(filename, 'w') as file:
            json.dump(info, file, indent=4)
        print(f"Successfully wrote recommendation to {filename}.")
    except IOError as e:
        print(f"Error writing to file: {e}")

def main():
    media_type = "ANIME"  # put MANGA instead for MANGA recommendations
    filename = "anilist_recommendation.json"
    recommendation = get_random_recommendation(media_type)
    if recommendation:
        write_recommendation_to_file(recommendation, filename)
    else:
        print("No recommendation was retrieved from AniList API after multiple attempts.")

# Run the main function
if __name__ == "__main__":
    main()
