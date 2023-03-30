import re

def calculate_average_response_time(log_file):
    with open(log_file, 'r') as f:
        total_time = 0
        count = 0
        for line in f:
            match = re.search(r'GET /.* HTTP/.* (\d+)$', line)
            if match:
                total_time += int(match.group(1))
                count += 1
        return total_time / count

# example usage:
average_time = calculate_average_response_time('access.log')
print(f"Average response time: {average_time:.2f} ms")