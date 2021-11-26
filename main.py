import InputReader

#read input

INPUT_FILE_PATH = "Puzzle_6.CSV"
START_NODE_X = 3
START_NODE_Y = 4

initial_nodeset, free_token = InputReader.get_nodeset_and_free_token_from_file(INPUT_FILE_PATH)
print(str(initial_nodeset))
print(str(free_token))
#give first node set to a*

#write output