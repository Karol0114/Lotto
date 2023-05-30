import requests
from bs4 import BeautifulSoup
from collections import Counter
from matplotlib import pyplot as plt
import numpy as np


#Funkcja pobiera dane z adresu URL, parsuje je za pomoca biblioteki BeautifulSoup, oraz zwraca listę liczb.
def get_numbers_from_url(a):
    list_of_numbers = []
    response = requests.get(a)
    soup = BeautifulSoup(response.text, 'html.parser')
    numbers_in_history = soup.find_all('li', class_ = "numbers_in_list")

    for i in numbers_in_history:
        list_of_numbers.append(int(i.get_text().strip()))
    
    return list_of_numbers


# Funkcna służąca do zliczania powtórzeń w liście 
def most_common_repetitions(lista):
    
    return Counter(lista)


numbers_list = []
# Wybieramy z jakich lat chcemy pobrać historię Lotto.
for year in range(2002, 2023):
    numbers = get_numbers_from_url(f'https://megalotto.pl/wyniki/lotto/losowania-z-roku-{year}')
    numbers_list += numbers

most_common_dict = most_common_repetitions(numbers_list)

x = most_common_dict.keys()
y = most_common_dict.values()

# Funkcja wyliczająca procentowe szanse na wygraną. 
def chance_of_winning(user_numbers, lotto_numbers):
    all_numbers = sum(lotto_numbers.values())
    print(all_numbers)
    hit_numbers = sum(lotto_numbers.get(liczba, 0) for liczba in user_numbers)
    chance = (hit_numbers / all_numbers) * 100
    return f'Szanse użytkownika na wygraną wynoszą: {chance} %'


#Najczęsciej powtarzające się liczby:
user_numbers = [4,6,38,13,24,17]
print(chance_of_winning(user_numbers, most_common_dict))

#Najrzadziej powtarzające się liczby:
user2_numbers = [33,43,47,26,48,12]
print(chance_of_winning(user2_numbers, most_common_dict))
