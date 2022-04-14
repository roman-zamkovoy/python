def is_prime(n):
    if n < 2:
        return False

    if n == 2:
        return True

    limit = n ** (1 / 2)

    i = 2

    while i <= limit:

        if n % i == 0:
            return False

        i += 1

    return True


print(is_prime(int(input("Число: "))))