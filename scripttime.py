import whisper

# Load the model (base is fast and highly accurate for English)
model = whisper.load_model("base")
result = model.transcribe("Day1Short.mp3", fp16=False)
# Print the text with exact start and end seconds
for segment in result["segments"]:
    start = segment["start"]
    end = segment["end"]
    text = segment["text"]
    print(f"[{start:.2f}s -> {end:.2f}s]: {text}")

