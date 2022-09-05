exclude_set = {"the",	"at", "there", "some",	   "my",
               "of",	"be", "use", "her",  "than",
               "and",	"this", "an", "would",  "first",
               "a",  "have", "each", "make", "water",
               "to",	"from", "which", "like",   "been",
               "in",	"or", "she", "him",  "call",
               "is",	"one", "do", "into",	   "who",
               "you",	"had", "how", "time",	   "oil",
               "that",	"by", "their",	 "has",	   "its",
               "it",	"word", "if", "look",   "now",
               "he",	"but", "will", "two", "find",
               "was",	"not", "up", "more",   "long",
               "for",	"what", "other",	 "write",  "down",
               "on",	"all", "about",	 "go",  "day",
               "are",	"were", "out", "see", "did",
               "as",	"we", "many", "number",  "get",
               "with",	"when", "then", "no", "come",
               "his",	"your", "them", "way", "made",
               "they",	"can", "these",	 "could",  "may",
               "i",  "said", "so", "people", "part"}

file_path = "/Users/jackzender/interview_heatmap/clean_data/interview_clean.txt"

data_file = open(file_path, 'r')

count = 0

question_dict = dict()

for line in data_file.readlines():
    line = line.strip()
    if (len(line) != 0):
        count += 1
        print("Line " + str(count) + " " + line)
