# Write a program that takes a list of dictionaries, each containing 'name' and 'score' keys, and returns the top N
#  dictionaries based on the 'score' values:

input_data = [
    {'name': 'Alice', 'score': 95},
    {'name': 'Bob', 'score': 85},
    {'name': 'Charlie', 'score': 90},
    {'name': 'David', 'score': 80}
]
N = 2

def top_n_scores(input_data, N):
    sorted_data = sorted(input_data, key=lambda x: x['score'], reverse=True)

    return sorted_data[:N]

result = top_n_scores(input_data, N)
print(result)