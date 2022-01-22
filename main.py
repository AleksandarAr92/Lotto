import Lotto

combination1 = [2, 13, 22, 11, 39, 32, 18]
combination2 = [3, 7, 20, 33, 39, 11, 6]
lotto = Lotto.Lotto(combination1, combination2)  # Creates object from class Lotto

print(f'Combination 1: {combination1}')
print(f'Combination 2: {combination2}')
print('--------------------------')
print(f'Winning combination: {lotto.generate_winning_lotto_combination()}')  # Generates winning lotto combination
print('--------------------------')
lotto.compare_combinations()

for message in lotto.show_results():
    print(message)  # Prints formatted message for representation
