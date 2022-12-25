# Ran in 6 minutes and 33 seconds, faster than I thought it would!

from typing import Tuple, Callable

INF = 10 ** 10
T = 24

hash = {}


def best_starting_with_decorator(
    ore_cost: int,
    clay_cost: int,
    obsidian_cost: Tuple[int, int],
    geode_cost: Tuple[int, int]
) -> Callable[[int, int, int, int, int, int, int, int, int], int]:
    def best_starting_with(
        t: int,
        ore: int,
        clay: int,
        obsidian: int,
        geode: int,
        ore_miners: int,
        clay_miners: int,
        obsidian_miners: int,
        geode_miners: int,
    ) -> int:
        state = (
            t,
            ore,
            clay,
            obsidian,
            geode,
            ore_miners,
            clay_miners,
            obsidian_miners
        )
        if state in hash:
            return hash[state]
        if t == T:
            return geode + geode_miners
        best_next = -INF
        if ore >= ore_cost:
            best_next = max(best_next, best_starting_with(
                t + 1,
                ore + ore_miners - ore_cost,
                clay + clay_miners,
                obsidian + obsidian_miners,
                geode + geode_miners,
                ore_miners + 1,
                clay_miners,
                obsidian_miners,
                geode_miners,
            ))
        if ore >= clay_cost:
            best_next = max(best_next, best_starting_with(
                t + 1,
                ore + ore_miners - clay_cost,
                clay + clay_miners,
                obsidian + obsidian_miners,
                geode + geode_miners,
                ore_miners,
                clay_miners + 1,
                obsidian_miners,
                geode_miners,
            ))
        if ore >= obsidian_cost[0] and clay >= obsidian_cost[1]:
            best_next = max(best_next, best_starting_with(
                t + 1,
                ore + ore_miners - obsidian_cost[0],
                clay + clay_miners - obsidian_cost[1],
                obsidian + obsidian_miners,
                geode + geode_miners,
                ore_miners,
                clay_miners,
                obsidian_miners + 1,
                geode_miners,
            ))
        if ore >= geode_cost[0] and obsidian >= geode_cost[1]:
            best_next = max(best_next, best_starting_with(
                t + 1,
                ore + ore_miners - geode_cost[0],
                clay + clay_miners,
                obsidian + obsidian_miners - geode_cost[1],
                geode + geode_miners,
                ore_miners,
                clay_miners,
                obsidian_miners,
                geode_miners + 1,
            ))
        best_next = max(best_next, best_starting_with(
                        t + 1,
                        ore + ore_miners,
                        clay + clay_miners,
                        obsidian + obsidian_miners,
                        geode + geode_miners,
                        ore_miners,
                        clay_miners,
                        obsidian_miners,
                        geode_miners,
                        ))
        hash[state] = best_next
        return best_next
    return best_starting_with


with open("input.txt", 'r') as input_file:
    lines = input_file.readlines()
    answer = 0
    for line in lines:
        tokens = line.strip().split()
        i = int(tokens[1][:-1])
        ore_cost = int(tokens[6])
        clay_cost = int(tokens[12])
        obsidian_cost = int(tokens[18]), int(tokens[21])
        geode_cost = int(tokens[27]), int(tokens[30])
        hash = {}
        answer += i * best_starting_with_decorator(
            ore_cost, clay_cost, obsidian_cost, geode_cost)(1, 0, 0, 0, 0, 1, 0, 0, 0)
    print(answer)
