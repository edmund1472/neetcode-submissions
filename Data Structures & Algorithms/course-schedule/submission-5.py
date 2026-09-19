class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        graph = {}

        for i in range(numCourses):
            graph[i] = []

        for course, prereq in prerequisites:
            graph[course].append(prereq)

        visiting = set()

        def dfs(course):

            if course in visiting:
                return False

            visiting.add(course)

            for prereq in graph[course]:
                result = dfs(prereq)
                if result == False:
                    return False
                else:
                    continue
            visiting.remove(course)

            graph[course] = []

            return True

        for course in range(numCourses):
            result = dfs(course)

            if result == False:
                return False

        return True