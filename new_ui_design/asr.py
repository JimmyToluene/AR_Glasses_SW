import tkinter as tk
from transformers import pipeline
from transformers.pipelines.audio_utils import ffmpeg_microphone_live
from threading import Thread


speak_button = None

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


def start_transcribing():
    global question_label
    question_label.config(text="Listening...")
    question = transcribe_mic(chunk_length_s=5.0)
    if len(question) > 0:
        question_label.config(text=question)
    speak_button.config(state=tk.NORMAL)


def Threading():

    speak_button.config(state=tk.DISABLED)
    t1 = Thread(target=start_transcribing)
    t1.start()



