from collections import deque
def findSteppingNumbers(n, m):
    result = []
    def bfs(num):
        q = deque([num])
        
        while q:
            step_num = q.popleft()

            if n <= step_num <= m:
                result.append(step_num)
            
            if step_num == 0 or step_num > m:
                continue

            last_digit = step_num % 10
 
            if last_digit > 0:
                next_step_num = step_num * 10 + (last_digit - 1)
                if next_step_num <= m:
                    q.append(next_step_num)
            
            if last_digit < 9:
                next_step_num = step_num * 10 + (last_digit + 1)
                if next_step_num <= m:
                    q.append(next_step_num)

    if n == 0:
        result.append(0) 
    
    for i in range(1, 10):
        bfs(i)

    result.sort()
    
    return result

n, m = map(int, input("Enter the range (N M): ").split())

stepping_numbers = findSteppingNumbers(n, m)
print("Stepping Numbers:", stepping_numbers)
