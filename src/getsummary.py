import tensorflow
import torch
import torch.nn.functional as F
import transformers
from transformers import pipeline


def getsum(text):
    if len(text) > 1024:
        text = text[:len(text)//2]
        summarizer = pipeline('summarization')
        newsarticle = text
        summary = summarizer(str(newsarticle), max_length = 130, min_length = 30, do_sample = False)
        textsummary = summary[0]['summary_text']
        return textsummary
    else:
        summarizer = pipeline('summarization')
        newsarticle = text
        summary = summarizer(str(newsarticle), max_length = 130, min_length = 30, do_sample = False)
        textsummary = summary[0]['summary_text']
        return textsummary

