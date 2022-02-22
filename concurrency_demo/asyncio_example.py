#!/usr/bin/env python3

import asyncio
from random import randint
from time import sleep, time


class OponentPlayer():
    async def play(self):
        response_time = randint(2, 4)
        await asyncio.sleep(response_time)
        return 'READY'

async def play_game(player_name, player, number_of_moves=2):
    for move in range(number_of_moves):
        print(f"Making move #{move} against {player_name}")
        await player.play()
        print(f"Player {player_name} responded")

async def main():
    player1 = OponentPlayer()
    player2 = OponentPlayer()
    player3 = OponentPlayer()
    await asyncio.gather(play_game('player1', player1), play_game('player2', player2), play_game('player3', player3))

if __name__ == '__main__':
    start_time = time()
    asyncio.run(main())

    elapsed_time = time() - start_time
    print(f"Elapsed time: {elapsed_time}")

