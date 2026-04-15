import ingestion
import brain
import notify
import production
import assembly
import asyncio
import voice
import json
import os

async def run_content_pipeline(url):

    print(f"Content Pipeline Starting for: {url}")

    raw_text = ingestion.ingest_client_data(url)
    print("Scrapped data received...")

    if not raw_text:
        print("No data scraped from the URL. Exiting pipeline.")
        return
    
    print("Asking Groq for viral script...")

    viral_script = brain.generate_script(raw_text, "Acquisition Venture for $100,000+ profit businesses in East Africa")
    scenes = viral_script.get("video_project", [])
    
    with open("final_script.json", "w") as f:
        json.dump(viral_script, f, indent=4)

    print("Sending preview to Telegram for approval...")
    
    
    
    print("Starting Multi-Asset Harvesting (12 scenes)...")
    video_clips = []
    full_voice_text = ""

    print("Sourcing video from Pexels...")
    
    
    for i, scene in enumerate(scenes):
        search_keyword = scene.get("search_keyword", "business")
        video_filename = f"scene_{i}_video.mp4"

        print(f"Sourcing video for scene {i+1} with keyword: {search_keyword}")
        

        downloaded_file = production.download_video(search_keyword, video_filename)
        if downloaded_file:
            video_clips.append(downloaded_file)

        full_voice_text += scene.get("text", "") + " "

    print(f"secured {len(video_clips)} video clips for the reel.")    

     
    
    print("Generating 3-minute voiceover...")

    
    voice_filename = await voice.generate_voice(full_voice_text, "zion_voice.mp3")
    print(f"Voiceover generated: {voice_filename}")

    print("Assembling layers...(This may take a few minutes)")
    output_video = assembly.create_final_reel(scenes, voice_filename, video_clips, "Zion_final_reel.mp4")

    print("Notifying command center(Telegram)...")
    notify.send_approval_notification(scenes[0]) 

    print(f"Content Pipeline completed successfully. Final video: {output_video}")

if __name__ == "__main__":
    asyncio.run(run_content_pipeline("https://zionventures.carrd.co/"))

    
          
