from bs4 import BeautifulSoup
import requests

def ingest_client_data(url):

    headers = {
        
        "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36"
    }  
    try:  

    
        response = requests.get(url, headers=headers, timeout=15, verify=False)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            
            for trash in soup(['script', 'style','header', 'footer', 'nav', 'aside']):
                trash.decompose()
            video_context =[]
            for media in soup.find_all(['video', "iframe", "img"]):
                if media.name in ['video', 'iframe']:
                    tittle = media.get('title') or "Video found without title"
                    video_context.append(f"[Video: {tittle}]")
                elif media.name == 'img':
                    alt_text = media.get('alt') or "Image found without alt text"
                    video_context.append(f"[Image: {alt_text}]")
                media.extract()

            clean_text = soup.get_text(separator=' ', strip=True) 
            media_text = ' '.join(video_context)
            return f"Media found: {media_text} | Text content: {clean_text}"      


        else:
            print(f"Failed to retrieve data from {url}. Status code: {response.status_code}")
            return None

    except Exception as e:
        return f" CONNECTION ERROR: {e}"  
        

if __name__ == "__main__":
    print("Ingestion mode starting")

    result = ingest_client_data() 
    print(result)
    
    print("Ingestion complete")