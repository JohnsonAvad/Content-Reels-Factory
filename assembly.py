import moviepy.config as conf


conf.IMAGEMAGICK_BINARY = r"C:\Program Files\ImageMagick-7.1.1-Q16-HDRI\magick.exe"

from moviepy import VideoFileClip, concatenate_videoclips, AudioFileClip, CompositeVideoClip, TextClip, ColorClip
import os



def create_final_reel(script_data, voice_file, video_files, output_name):
    print(f"Assembly 3-minute Enterprise video: {output_name}")
    audio = AudioFileClip(voice_file)

    total_duration = audio.duration 

    num_clips = len(video_files)
    duration_per_clip = total_duration / num_clips 

    final_scenes = []
    
    bg_color = ColorClip(size=(1080, 1920), color =(15, 23, 42)).with_duration(total_duration)
   
    current_time = 0
    for i, video_path in enumerate(video_files):
        print(f"Processing scene {i+1} at {current_time:.2f}s")
        clip = VideoFileClip(video_path).resized(height=1920)
        clip = clip.cropped(width=1080, height=1920, x_center=clip.w/2, y_center=clip.h/2)

        scene_clip = clip.subclipped(0, min(clip.duration, duration_per_clip)).with_duration(duration_per_clip)

        scene_info = script_data[i] 
        txt = scene_info.get("text", "Moving to the next stage...")

        txt_clip = TextClip(
            text=txt,
            font=r"C:\Windows\Fonts\arialbd.ttf",
            font_size=50,
            color='yellow',
            method='caption',
            size=(900, None)
        ).with_duration(duration_per_clip).with_position(('center', 'bottom'))

        combined =CompositeVideoClip([scene_clip, txt_clip]).with_start(current_time)
        final_scenes.append(combined)

        current_time += duration_per_clip

    final_video = CompositeVideoClip([bg_color] + final_scenes)
    final_video = final_video.with_audio(audio)

       
           

        

    print(f"Rendering 3-minute final reel...")
    final_video.write_videofile(output_name, fps=24, codec="libx264", audio_codec="aac", threads=4, preset="ultrafast", bitrate="3000k")

    print(f"Final reel created successfully: {output_name}")

    return output_name