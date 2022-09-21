#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

def get_num_letters(text):
	sum = 0
	for letter in text:
		if letter.isalnum():
			sum += 1
	return sum

def get_word_length_histogram(text):
	longest = 0
	for word in text.split():
		if longest < get_num_letters(word):
			longest = get_num_letters(word)
	histogram = [0 for _ in range(0, longest+1)]
	for word in text.split():
		histogram[get_num_letters(word)] += 1
	return histogram

def format_histogram(histogram):
	for i, word in enumerate(histogram[1:], 1):
		print(f"{i:>2}", " ".join("*" for _ in range(word)))

	return ""

def format_horizontal_histogram(histogram):
	longest = max(histogram)
	histogram_format = ""
	for i in range(longest, 0, -1):
		for j in histogram[1:]:
			if j >= i:
				histogram_format += "|"
			else:
				histogram_format += " "
		histogram_format += "\n"
	for _ in histogram[1:]:
		histogram_format += "¯"
	return histogram_format


if __name__ == "__main__":
	spam = "Stop right there criminal scum! shouted the guard confidently."
	eggs = get_word_length_histogram(spam)
	print(eggs, "\n")
	print(format_histogram(eggs), "\n")
	print(format_horizontal_histogram(eggs))
