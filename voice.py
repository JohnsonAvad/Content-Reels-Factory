import asyncio
import edge_tts

async def generate_voice(text, filename):
    print(f"Generating AI voice for: {text[:30]}...")

    voice = "en-US-GuyNeural"


    communicate = edge_tts.Communicate(text, voice)

    await communicate.save(filename)
    print(f"Voice generated and saved as: {filename}")
    return filename

if __name__ == "__main__":
    text = "Zion Business Ventures does Acquisition of businesss in East Africa, we help business owners sell, retire, grow or save their struggling businesses. We focus on businesses making $100,000 + profit per month."
    asyncio.run(generate_voice(text, "sample_voice.mp3"))