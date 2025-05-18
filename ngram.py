import re
from collections import defaultdict, Counter
import sys

class NgramCharacterModel:
    def __init__(self, corpus, n=2):
        self.n = n
        self.ngram_counts = defaultdict(Counter)
        self.context_counts = Counter()
        self.vocab = set()
        self.words = set()
        self._train(corpus)

    def _train(self, corpus):
        words = re.findall(r"\b\w+\b", corpus.lower())
        self.words = set(words)
        for word in words:
            padded_word = '~' * (self.n - 1) + word + '$'
            self.vocab.update(padded_word)
            for i in range(len(padded_word) - self.n + 1):
                context = padded_word[i:i+self.n-1]
                char = padded_word[i+self.n-1]
                self.ngram_counts[context][char] += 1
                self.context_counts[context] += 1

    def _word_probability(self, word):
        padded_word = '~' * (self.n - 1) + word + '$'
        prob = 1.0
        for i in range(len(padded_word) - self.n + 1):
            context = padded_word[i:i+self.n-1]
            char = padded_word[i+self.n-1]
            context_count = self.context_counts[context]
            char_count = self.ngram_counts[context][char]
            if context_count == 0:
                prob *= 1e-6
            else:
                prob *= char_count / context_count
        return prob

    def _generate_word(self, prefix):
        candidates = [w for w in self.words if w.startswith(prefix)]
        if not candidates:
            return ""
        return max(candidates, key=self._word_probability)

    def predict_top_words(self, prefix, top_k=10):
        candidates = [w for w in self.words if w.startswith(prefix)]
        scored = [(w, self._word_probability(w)) for w in candidates]
        scored.sort(key=lambda x: x[1], reverse=True)
        return [w for w, _ in scored[:top_k]]