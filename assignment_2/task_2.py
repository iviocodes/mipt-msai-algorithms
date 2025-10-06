from time import time

# set the following flag to True to estimate execution time
#
# Exact execution time on you device may be different
# from one on Yandex contest platform!
#
# The flag MUST be False when you are submitting your solution!
estimate_execution_time = False

# Fixed parameters of quantum process:
quantum_a = 7**5
quantum_m = 2**31 - 1


def analyze_trimpazation(n, m, q0):
    """
    This function generates data with given parameters
    and calculates desired Y value.

    You need to modify it to make it execute faster.
    You can check your progress using estimate_execution_time flag
    at the top of the file.
    """
    m_div2 = m // 2
    q = q0

    min = -m_div2
    max = m - m_div2 - 1
    range_size = max - min + 1
    count = [0] * (range_size)

    # generating x data:
    for i in range(n):
        x_i = q % m - m_div2
        index = x_i - min
        count[index] += 1
        q = (q * quantum_a) % quantum_m

    res = 0
    current_index = 1

    # compute sum without new sorted array
    for index in range(range_size):
        x_i_count = count[index]
        if x_i_count > 0:
            x_i = index + min
            sum = x_i_count * current_index + (x_i_count * (x_i_count - 1)) // 2
            res += x_i * sum
            current_index += x_i_count

    return res


if __name__ == "__main__":
    N, M, q0 = map(int, input().split())
    t = time()
    print(analyze_trimpazation(N, M, q0))
    if estimate_execution_time:
        print(f"Execution time = {time() - t:.8f} seconds")
