from random import randint
from time import sleep, time
from multiprocessing import Process
from queue import Queue

class OponentPlayer():
    def play(self):
        response_time = randint(2,4)
        sleep(response_time)
        return 'READY'

def play_game(player_name, player, number_of_moves=3):
    for move in range(number_of_moves):
        print(f"Making move #{move} against {player_name}")
        player.play()
        print(f"Player {player_name} responded")

def main():
    player_list = ['player1', 'player2', 'player3']
    processes = []

    for player in player_list:
        player_instance = OponentPlayer()
        process = Process(target=play_game, args=(player, player_instance))
        process.start()
        processes.append(process)

    for process in processes:
        process.join()

if __name__ == '__main__':
    start_time = time()
    results_queue = main()
    elapsed_time = time() - start_time
    print(f"Elapsed time: {elapsed_time}")
