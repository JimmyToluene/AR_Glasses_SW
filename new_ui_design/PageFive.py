import tkinter as tk
from PIL import ImageTk, Image
import PageTwo
from transformers import pipeline
from transformers.pipelines.audio_utils import ffmpeg_microphone_live
from threading import Thread

asr_model_id = "openai/whisper-tiny.en"
transcriber = pipeline("automatic-speech-recognition",
                       model=asr_model_id,
                       device="cpu")

def transcribe_mic(chunk_length_s: float) -> str:
    global transcriber
    sampling_rate = transcriber.feature_extractor.sampling_rate
    mic = ffmpeg_microphone_live(
        sampling_rate=sampling_rate,
        chunk_length_s=chunk_length_s,
        stream_chunk_s=chunk_length_s,
    )

    result = ""
    for item in transcriber(mic):
        result = item["text"]
        if not item["partial"][0]:
            break
    return result.strip()





class PageFive(tk.Frame):
    def __init__(self, parent, root):
        super().__init__(parent)
        self.configure(bg="black")
        self.downangle = Image.open("icon/angle/arrow_down.png")
        self.down_angle = ImageTk.PhotoImage(self.downangle.resize((32, 32)))
        self.return_btn = tk.Button(self, image=self.down_angle, command=lambda: root.show_frame(PageTwo.PageTwo))
        self.return_btn.configure(background="black")
        self.return_btn.place(anchor="center", x=320, y=370)

        self.question_label = tk.Label(self, text="Press and hold the button to speak", font=("Helvetica", 30,), fg= "white",bg="black")
        self.question_label.place(anchor="center",x=320,y=200)

        self.speak_button = tk.Button(self, text="Speak", font=("Helvetica", 14), command=lambda: Threading(self),bg="black")
        self.speak_button.place(anchor="center", x=320,y=300)


def start_transcribing(self):
    self.question_label.config(text="Listening...")
    question = transcribe_mic(chunk_length_s=5.0)
    if len(question) > 0:
        self.question_label.config(text=question)
    self.speak_button.config(state=tk.NORMAL)


def Threading(self):
    self.speak_button.config(state=tk.DISABLED)
    t1 = Thread(target=start_transcribing(self))
    t1.start()



