class Solution:
    def mostWordsFound(self, sentences: list[str]) -> int:
        max_words = 0

        for sentence in sentences:
            words = 1
            for ch in sentence:
                if ch == " ":
                    words += 1
            if words > max_words:
                max_words = words

        return max_words

# # BEST SOLUTION 
#   class Solution:
#     def mostWordsFound(self, sentences):
#         return max(len(sentence.split()) for sentence in sentences)