class phone:
    def __init__(self, price, camera_count, screen_size):
        self.price = price
        self.camera_count = camera_count
        self.screen_size = screen_size

class google_phone(phone):
    def __init__(self, ):
        super().__init__(10,3,5)

    def special_feature(self, num_list):
        return sorted([i for i in num_list if i > 10 and i%2==0], reverse=True)

class taiwan_phone(phone):
    def __init__(self, ):
        super().__init__(20,1,3)

    def special_feature(self, num):

        fnum = self.Fibonacci(num)
        fnum_str = f"{fnum:02}"
        tendights = int(fnum_str[-2])
        dights = int(fnum_str[-1])
        return self.Permutations(tendights, dights)

    def Fibonacci(self, n):

        if n < 0:
            print("Incorrect input")

        elif n == 0:
            return 0

        elif n == 1 or n == 2:
            return 1

        else:
            return self.Fibonacci(n - 1) + self.Fibonacci(n - 2)

    def Permutations(self, x, y):

        result = x
        for _ in range(y-1):
            result = result * (x-1)
            x = x - 1

        return result

googlephone = google_phone()
print(googlephone.special_feature([3, 43, 62, 15, 18, 22]))

taiwanphone = taiwan_phone()
print(taiwanphone.special_feature(10))