def max_sub_array_of_size_k(k, arr):
  # TODO: Write your code here
  sum = 0
  maxSum =0 
  start =0
  for i, v in enumerate(arr):
        sum += v 
        if i >= k-1:
            if sum > maxSum:
              maxSum = sum
            sum -= arr[start]
            start += 1


  return maxSum


print ( max_sub_array_of_size_k(3, [2, 1, 5, 1, 3, 9]))
