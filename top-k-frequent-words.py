class Solution:
  def topKFrequent(self, words: List[str], k: int) -> List[str]:
    c = sorted(Counter(words).items(), key=lambda x: (-x[1],x[0]))
    return [w for w, n in c[:k]]