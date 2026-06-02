import asyncio
import os
import shutil
import main
from datetime import datetime

ZION_TARGETS = [
    "Agro-processing and Food value chain",
    "Modern Manufacturing and Fabrication",
    "Pharmaceuticals and Medical Supplies",
    "Large scale commercial Real Estate",
    "Logistics and Transportation",
    "Energy Infrastructure and Utilities",
    "Financial Services and Fintech",
    "Tourism and Hospitality",
    "Information and Communication Technology (ICT)",
    "Education and Human Capital Development",
]

TARGET_URL = "https://zionventures.carrd.co/"
STORAGE_VAULT = "outbound_delivery"

async def run_batch_orchestrator():
    print(f"AVAD Content Factory: Initializing Batch Loop for {len(ZION_TARGETS)} targets.")

    if not os.path.exists(STORAGE_VAULT):
        os.makedirs(STORAGE_VAULT)
        print(f"Created storage vault: {STORAGE_VAULT}")

    for i, target in enumerate(ZION_TARGETS):
        print(f"\nBatch {i+1}/{len(ZION_TARGETS)}: Processing target - {target}")
        
        try:
            await main.run_content_pipeline(TARGET_URL, target)

            source_file = "Zion_final_reel.mp4"
            if not os.path.exists(source_file):
            
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                batch_folder = os.path.join(STORAGE_VAULT, f"batch_{i+1}_{timestamp}")
                os.makedirs(batch_folder, exist_ok=True)

                for file in os.listdir("."):
                    if file.startswith("scene_") or file in ["final_script.json", "Zion_final_reel.mp4"]:
                        shutil.move(file, os.path.join(batch_folder, file))
                        print(f"Moved {file} to {batch_folder}")

                print(f"Batch {i+1} completed and stored in {batch_folder}")

        except Exception as e:
            print(f"Error processing batch {i+1} for target '{target}': {e}")
            continue

    print("\nBatch Orchestrator: All batches processed. Check the storage vault for results.") 

if __name__ == "__main__":
    asyncio.run(run_batch_orchestrator())