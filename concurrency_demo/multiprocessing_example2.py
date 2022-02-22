#!/usr/bin/env python3

from random import randint
from time import sleep, time
from multiprocessing import Process


class OponentPlayer():
    def play(self):
        response_time = randint(2, 4)
        # This simulates a random response time from an opposing player
        sleep(response_time)
        return 'READY'

def play_game(player_name, player, number_of_moves=2):
    for move in range(number_of_moves):
        print(f"Making move #{move} against {player_name}")
        player.play()
        print(f"Player {player_name} responded")

def main(): 
    player_list = ['player1', 'player2', 'player3']
    threads = []

    for player in player_list:
        player_instance = OponentPlayer()
        thread = Process(target=play_game, args=(player , player_instance))
        thread.start()
        threads.append(thread)
   
    for thread in threads:
        thread.join()

if __name__ == '__main__':
    start_time = time()
    main()
    elapsed_time = time() - start_time
    print(f"Elapsed time: {elapsed_time}")
