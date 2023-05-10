class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        dec = defaultdict(list)
        in_degre = [0]*numCourses

        for i in prerequisites:
            dec[i[1]].append(i[0])
            in_degre[i[0]] += 1
        
        qe = deque()
        for i,val in enumerate(in_degre):
            if val == 0:
                qe.append(i)
                
        res = []
        while qe:
            no = qe.popleft()
            res.append(no)
            for i in dec[no]:
                in_degre[i] -= 1
                if in_degre[i] == 0:
                    qe.append(i)
        
        if len(res) == numCourses:
            return True

        return False