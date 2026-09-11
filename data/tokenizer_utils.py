from typing import List, Dict

class Solution:
    def tokenize_numbers(self, numbers: List[int], vocab: Dict[str, int]) -> List[List[str]]:
        # Tokenize each number using greedy left-to-right longest match.
        # Return a list of token lists showing how each number gets split.
        token_list = []
        for number in numbers:
            text = str(number)
            tokens = self._greedy_tokenize(text, vocab)
            token_list.append(tokens)
        return token_list

    def count_tokens(self, text: str, vocab: Dict[str, int]) -> int:
        # Count how many tokens the text uses with greedy tokenization.
        # Use greedy left-to-right longest match.
        tokens = self._greedy_tokenize(text, vocab)
        return len(tokens)

    def fertility_score(self, text: str, vocab: Dict[str, int]) -> float:
        # Compute tokens-per-word ratio (fertility).
        # Higher = more expensive and less efficient.
        # Round to 4 decimal places.
        num_tokens = self.count_tokens(text, vocab)
        num_words = len(text.split())
        return round(num_tokens / num_words, 4)
    
    def _greedy_tokenize(self, text, vocab):
        tokens = []
        i = 0
        while i < len(text):
            match = text[i]
            for j in range(len(text), i, -1):
                if text[i:j] in vocab:
                    match = text[i:j]
                    break
            tokens.append(match)
            i += len(match)
        return tokens
