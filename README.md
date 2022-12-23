# Advent of Code 2022 solutions

$\verb|¯\_(ツ)_/¯|$

Some notes:

- I add the solution to a problem here once the leaderboard for that problem gets full.
- For solutions that don't involve reading from a file, I execute my solutions in the command line using `<execute program> < input.txt > output.txt`. For example, I do `python3 main.py < input.txt > output.txt` to run my Python solutions.
	- I've no idea why it took me a full week to realize that starting with `with open("input.txt", "r")` made the piping redundant ahaha
- `16-setup.py` is there to turn the original input for Day 16 into a more digestible one (for C++, at least). The command line process for this specific day would be

	```bash
	python3 16-setup.py > output.txt && g++ -std=c++20 -o out main.cpp && ./out < output.txt > final_output.txt
	```

	assuming the input file is named `input.txt`.