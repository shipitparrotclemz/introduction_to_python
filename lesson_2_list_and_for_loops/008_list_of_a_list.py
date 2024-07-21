"""
Challenge 10:
- Batching customers into batch of 10s
"""

# my_list: list[int] = []
# for i in range(100):
#     my_list.append(i)

# my_list: list[int] = [0,..., 99]

list_of_batches: list[list[int]] = []

"""
[
    # [0,1,2,3,4],
    [5,6,7,8,9]
]
"""
"""
0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19...
          ^         ^
          s         e
"""
start_of_batch: int = 0  # start = 5
for end_of_batch in range(start_of_batch + 5, 105, 5):  # 5,10,15,20...95,100
    batch: list[int] = []  # [5,6,7,8,9]
    for i in range(start_of_batch, end_of_batch):  # 5 to 9 (exclu 10)
        batch.append(i)
    start_of_batch = end_of_batch
    list_of_batches.append(batch)

print(list_of_batches)

"""
[
    [0,1,2,3,4],
    [5,6,7,8,9],
    [10,11,12,13,14],
    [15,16,17,18,19],
    ...
    [95,96,97,98,99]
]
2D list, each nested 1D list has 5 items
20 nested list
"""
