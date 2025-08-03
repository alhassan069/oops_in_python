from collections import Counter
import re

class TextAnalyzer:
    def __init__(self, text):
        """
        Initialize with text to analyze
        Args:
            text (str): Text to analyze
        """
        self.original_text = text
        self.text = text.lower()  # For case-insensitive analysis

    def get_character_frequency(self, include_spaces=False):
        """
        Get frequency of each character
        Args:
            include_spaces (bool): Whether to include spaces in count
        Returns:
            Counter: Character frequencies
        """
        text = self.text
        if include_spaces == False:
            text = text.replace(' ', '')

        char_count = Counter(text)

        return char_count.most_common()

    def get_word_frequency(self, min_length=1):
        """
        Get frequency of each word (minimum length filter)
        Args:
            min_length (int): Minimum word length to include
        Returns:
            Counter: Word frequencies
        """

        text = self.text.replace("\n", "")
        text_arr = text.split(" ")
        counter = Counter(text_arr)
        return counter.most_common()

    def get_sentence_length_distribution(self):
        """
        Analyze sentence lengths (in words)
        Returns:
            dict: Contains 'lengths' (Counter), 'average', 'longest', 'shortest'
        """

        text = self.text.strip()
        text = text.replace('\n', '')

        sentence_array = text.split(".")
        sentence_array_len = list(map(lambda x : len(x),sentence_array[:-1],))
        sum_sentence = sum(sentence_array_len)
        avg = sum_sentence/len(sentence_array_len)
        return {"lengths":sentence_array_len, 'average': avg, 'longest':sorted(sentence_array_len)[-1], 'shortest': sorted(sentence_array_len)[0]}

    def find_common_words(self, n=10, exclude_common=True):
        """
        Find most common words, optionally excluding very common English words
        Args:
            n (int): Number of words to return
            exclude_common (bool): Exclude common words like 'the', 'and', etc.
        Returns:
            list: List of tuples (word, count)
        """
        common_words = {'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of', 'with', 'by',
                        'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'do', 'does', 'did',
                        'will', 'would', 'could', 'should', 'may', 'might', 'can', 'this', 'that', 'these', 'those',
                        'i', 'you', 'he', 'she', 'it', 'we', 'they', 'me', 'him', 'her', 'us', 'them'}
        text = self.text.replace("\n", "")
        text_arr = text.split(" ")
        filtered_words = []
        if exclude_common:
            for word in text_arr:
                if word not in common_words:
                    filtered_words.append(word)
            counter = Counter(filtered_words)
        else:
            counter = Counter(text_arr)
        return counter.most_common(n)


    def get_reading_statistics(self):
        """
        Get comprehensive reading statistics
        Returns:
            dict: Contains character_count, word_count, sentence_count,
                  average_word_length, reading_time_minutes (assume 200 WPM)
        """
        character_count = self.get_character_frequency()
        word_count = self.get_word_frequency()
        sentence_count = self.get_sentence_length_distribution()


        words = self.text.strip()
        text = words.replace("\n", "")
        text_arr = text.split(" ")
        text_arr_len = list(map(lambda x : len(x),text_arr))
        sum_arr_len = sum(text_arr_len)
        avg = round(sum_arr_len/len(text_arr_len), 2)

        reading_time_minutes = len(text_arr_len) /200
        return {'character_count':character_count, 'word_count': word_count, 'sentence_count':sentence_count,'average_word_length':avg, 'reading_time_minutes':reading_time_minutes}


    def compare_with_text(self, other_text):
        """
        Compare this text with another text
        Args:
            other_text (str): Text to compare with
        Returns:
            dict: Contains 'common_words', 'similarity_score', 'unique_to_first', 'unique_to_second'
        """
        words1 = self.text.strip().replace('\n', ' ').replace('.', '').replace(',','').split(" ")
        words2 = other_text.strip().replace('\n', ' ').replace('.', '').replace(',','').split(" ")
        
        set1 = set(words1)
        set2 = set(words2)
        common_words = set1 & set2
        all_words = set1 | set2
        unique_to_first = set1 - set2
        unique_to_second = set2 - set1
        similarity_score =  round(len(common_words) / len(all_words), 2)


        return {'common_words': set1 & set2, 'similarity_score' : similarity_score, 'unique_to_first': unique_to_first, 'unique_to_second': unique_to_second}


# Test your implementation
sample_text = """
Python is a high-level, interpreted programming language with dynamic semantics.
Its high-level built-in data structures, combined with dynamic typing and dynamic binding,
make it very attractive for Rapid Application Development. Python is simple, easy to learn
syntax emphasizes readability and therefore reduces the cost of program maintenance.
Python supports modules and packages, which encourages program modularity and code reuse.
The Python interpreter and the extensive standard library are available in source or binary
form without charge for all major platforms, and can be freely distributed.
"""

analyzer = TextAnalyzer(sample_text)

# print("Character frequency (top 5):", analyzer.get_character_frequency()[:5])
# print("Word frequency (top 5):", analyzer.get_word_frequency()[:5])
# print("Sentence length analyzer:", analyzer.get_sentence_length_distribution())
# print("Common words:", analyzer.find_common_words(5))
# print("Reading statistics:", analyzer.get_reading_statistics())

# Compare with another text
other_text = "Java is a programming language. Java is object-oriented and platform independent."
comparison = analyzer.compare_with_text(other_text)
print("Comparison results:", comparison)
