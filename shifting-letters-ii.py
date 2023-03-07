class Solution:
	def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
		res = [0] * (len(s) + 1)
		for start, end, direction in shifts:
			if direction == 0:
				res[start] -= 1
				res[end + 1] += 1
			else:
				res[start] += 1
				res[end + 1] -= 1

		for i in range(1, len(res)):
			res[i] += res[i - 1]

		for i, c in enumerate(s):
			res[i] = chr(ord("a") + (ord(c) - ord("a") + res[i] + 26) % 26)
            
		return "".join(res[:-1])