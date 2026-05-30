# import whisper

# # Load the model (base is fast and highly accurate for English)
# model = whisper.load_model("base")
# result = model.transcribe("1.1Exercises.wav", fp16=False)
# # Print the text with exact start and end seconds
# for segment in result["segments"]:
#     start = segment["start"]
#     end = segment["end"]
#     text = segment["text"]
#     print(f"[{start:.2f}s -> {end:.2f}s]: {text}")


class Solution:
    def reverse(self, x: int) -> int:
        reversed_num = 0
        is_negative = x < 0
        x_help = abs(x)
        
        while x_help > 0:
            reversed_num *= 10
            reversed_num += x_help % 10
            x_help //= 10

        if is_negative:
            return reversed_num * (-1)
        
        if reversed_num < -2**31 or reversed_num > 2**31 - 1:
            return 0
        
        return reversed_num

print(Solution().reverse(-2147483648))