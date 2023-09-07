#!/usr/bin/env python3

from random import randint
from time import sleep, time
from threading import Thread
from queue import Queue

class OponentPlayer():
    def play(self):
        response_time = randint(2, 4)
        sleep(response_time)
        return 'READY'
    
def play_game(player_name, player, common_queue, number_of_moves=4):
    for move in range(number_of_moves):
        print(f"Making move #{move} against {player_name}")
        player.play()
        print(f"Player {player_name} responded")
        common_queue.put((player_name, move))

def main():
    player_list = ['player1', 'player2', 'player3']
    threads = []
    results_queue = Queue()

    for player in player_list:
        player_instance = OponentPlayer()
        thread = Thread(target=play_game, args=(player, player_instance, results_queue))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    return results_queue

if __name__ == '__main__':
    start_time = time()
    results_queue = main()
    elapsed_time = time() - start_time
    while not results_queue.empty():
        print(results_queue.get())
    print(f"Elapsed time: {elapsed_time}")