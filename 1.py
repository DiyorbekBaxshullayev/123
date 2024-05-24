def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Oxirgi i ta element allaqachon joylashgan
        for j in range(0, n-i-1):
            # Joriy element va keyingi elementni solishtirish
            if arr[j] > arr[j+1]:
                # Agar tartib bo'lmasa, ularni almashtirish
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Test qilish uchun misol
if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    print("Boshlang'ich massiv:", arr)
    sorted_arr = bubble_sort(arr)
    print("Saralangan massiv:", sorted_arr)
