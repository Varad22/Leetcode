class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        diff=[101]*len(students)
        students.sort()
        seats.sort()
        print(students, seats)
        for i in range(len(students)):
            diff[i]=abs(students[i]-seats[i])
        return sum(diff)
