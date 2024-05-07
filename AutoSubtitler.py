import moviepy.editor as mp
import re
import time

def generate_srt(video_file, text_file):
    # Read video file and extract duration
    video = mp.VideoFileClip(video_file)
    duration = video.duration
    
    # Read text file and preprocess text
    with open(text_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        lines = [re.sub(r'\s+', ' ', line.strip()) for line in lines if line.strip()]
    
    # Generate timecodes for each line of text
    line_duration = duration / len(lines)
    timecodes = [time.strftime('%H:%M:%S,000', time.gmtime(i * line_duration)) for i in range(len(lines))]
    
    # Create SRT file content
    srt_content = ''
    for i, (timecode, line) in enumerate(zip(timecodes, lines), start=1):
        end_timecode = timecodes[i] if i < len(timecodes) else timecodes[-1]  # Use the next timecode or the last timecode
        srt_content += f"{i}\n{timecode} --> {end_timecode}\n{line}\n\n"
    
    # Write SRT file
    output_file = video_file.replace('.mp4', '.srt')
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(srt_content)
    
    print(f"SRT file generated: {output_file}")

if __name__ == "__main__":
    video_file = input("Enter the path of the video file: ")
    text_file = input("Enter the path of the text file: ")
    generate_srt(video_file, text_file)
