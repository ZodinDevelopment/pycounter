from collections import Counter
from string import punctuation



def load_text(input_file):
	"""SOme documentation"""
	with open(input_file, 'r') as file:
		text = file.read()
	return text



def clean_text(text):
	"""Lowercase and punctuation removal"""
	text = text.lower()
	for p in punctuation:
		text = text.replace(p, "")
	return text 


def count_words(input_file):
	"""Count unique words"""
	text = load_text(input_file)
	text = clean_text(text)
	words = text.split()
	return Counter(words)