class Solution:
	def maxLength(self, arr: List[str]) -> int:
		s = [""]
		res = 0
		for i in arr:
			if len(set(i)) == len(i):
				for j in s[:]:
					if len(i) + len(j) == len(set(i + j)):
						s.append(i + j)
						if len(i + j) > res:
							res = len(i + j)
		return res