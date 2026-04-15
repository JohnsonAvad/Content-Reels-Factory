import os
import requests
from dotenv import load_dotenv

load_dotenv()

def download_video(keyword, filename):
    """
    Downloads a high-quality video from Pexels based on a AI search keyword.
    """
    print(f"Searching for videos with keyword: {keyword}")
    api_key = os.getenv('PEXELS_API_KEY')
    headers = {
        "Authorization": api_key}
    
    url = f"https://api.pexels.com/videos/search?query={keyword}&per_page=1"
    response = requests.get(url, headers=headers, stream=True).json()

    if response.get("videos"):
        video_url = response["videos"][0]["video_files"][0]["link"]
        print(f"Downloading binary strream from: {keyword} video URL: {video_url}")
        video_response = requests.get(video_url, stream=True)
        with open(filename, 'wb') as f:
            for chunk in video_response.iter_content(chunk_size=8192):
                f.write(chunk)
        print(f"Video downloaded and saved as: {filename}")
        return filename
    else:
        print("No videos found for the given keyword.")
        return None
    
if __name__ == "__main__":

    website_vibes = ["retirement", "$100,000 + profit", "businesses", 
                     "EastAfrican", "growth", "struggling business", "selling business", "quitting business"]

    print("Testing Multi-scene production for 'whole website' vibe..")

    for i, vibe in enumerate(website_vibes):
        video_filename = f"scene_{i+1}.mp4"
        download_video(vibe, video_filename)

    print("Multi-scene video production test completed.")
   