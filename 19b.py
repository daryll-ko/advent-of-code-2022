# Ran in 1 minute and 58 seconds, fair enough.

from typing import Callable

INF = 10**10
T = 32
ORE_LIMIT = 16

hash = {}


def best_starting_with_decorator(
    ore_cost: int,
    clay_cost: int,
    obsidian_cost: tuple[int, int],
    geode_cost: tuple[int, int],
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
            obsidian_miners,
        )
        if state in hash:
            return hash[state]
        if t == T:
            return geode + geode_miners
        best_next = -INF

        # two things:
        # - don't be a hoarder
        # - we never need >4 ore miners

        if (
            ore_miners < 4
            and ore >= ore_cost
            and ore + ore_miners - ore_cost <= ORE_LIMIT
        ):
            best_next = max(
                best_next,
                best_starting_with(
                    t + 1,
                    ore + ore_miners - ore_cost,
                    clay + clay_miners,
                    obsidian + obsidian_miners,
                    geode + geode_miners,
                    ore_miners + 1,
                    clay_miners,
                    obsidian_miners,
                    geode_miners,
                ),
            )
        if ore >= clay_cost and ore + ore_miners - clay_cost <= ORE_LIMIT:
            best_next = max(
                best_next,
                best_starting_with(
                    t + 1,
                    ore + ore_miners - clay_cost,
                    clay + clay_miners,
                    obsidian + obsidian_miners,
                    geode + geode_miners,
                    ore_miners,
                    clay_miners + 1,
                    obsidian_miners,
                    geode_miners,
                ),
            )
        if (
            ore >= obsidian_cost[0]
            and clay >= obsidian_cost[1]
            and ore + ore_miners - obsidian_cost[0] <= ORE_LIMIT
        ):
            best_next = max(
                best_next,
                best_starting_with(
                    t + 1,
                    ore + ore_miners - obsidian_cost[0],
                    clay + clay_miners - obsidian_cost[1],
                    obsidian + obsidian_miners,
                    geode + geode_miners,
                    ore_miners,
                    clay_miners,
                    obsidian_miners + 1,
                    geode_miners,
                ),
            )
        if (
            ore >= geode_cost[0]
            and obsidian >= geode_cost[1]
            and ore + ore_miners - geode_cost[0] <= ORE_LIMIT
        ):
            best_next = max(
                best_next,
                best_starting_with(
                    t + 1,
                    ore + ore_miners - geode_cost[0],
                    clay + clay_miners,
                    obsidian + obsidian_miners - geode_cost[1],
                    geode + geode_miners,
                    ore_miners,
                    clay_miners,
                    obsidian_miners,
                    geode_miners + 1,
                ),
            )
        if ore + ore_miners <= ORE_LIMIT:
            best_next = max(
                best_next,
                best_starting_with(
                    t + 1,
                    ore + ore_miners,
                    clay + clay_miners,
                    obsidian + obsidian_miners,
                    geode + geode_miners,
                    ore_miners,
                    clay_miners,
                    obsidian_miners,
                    geode_miners,
                ),
            )
        hash[state] = best_next
        return best_next

    return best_starting_with


with open("input.txt", "r") as input_file:
    lines = input_file.readlines()
    answer = 1
    for line in lines:
        tokens = line.strip().split()
        ore_cost = int(tokens[6])
        clay_cost = int(tokens[12])
        obsidian_cost = int(tokens[18]), int(tokens[21])
        geode_cost = int(tokens[27]), int(tokens[30])
        hash = {}
        answer *= best_starting_with_decorator(
            ore_cost, clay_cost, obsidian_cost, geode_cost
        )(1, 0, 0, 0, 0, 1, 0, 0, 0)
    print(answer)
