field_count = 0
row_count = 0
array = []

# scan pattern for looking for mines, missing out centre
pattern = [
    (-1,-1), (0, -1), (1, -1),
    (-1, 0), (1, 0),
    (-1, 1), (0, 1), (1,1)
]

def process(array, field_count):
    # process each row and then each item in row
    print ('Field #' + str(field_count))

    for y, row in enumerate(array):
        max_x, max_y = len(row) - 1, len(array) - 1 # max rows and cols so we are not checking squares out of range

        for x, item in enumerate(row):
            mine_count = 0
            if item == '*': print ('*', end='') # simple case - it's a mine!
            else:
                for coord in pattern: # iterate through our transform matrix (or whatever it is!!!)
                    dx, dy  = x + coord[0], y + coord[1]
                    # if square we are looking at is in range and not a DOT then it's a MINE and increment our count
                    if dx >= 0 and dx < len(row) and dy >= 0 and dy < len(array) and array[dy][dx] != '.': 
                        mine_count +=1
                print (mine_count, end = '')

        print ()

f = open('input.txt', 'r')
for line in f.readlines():

    if row_count == 0:
        # read first line m n and start row count
        (n, m) = list(map(int, line.split()))
        if m == 0 and n == 0:
            # end of input
            break
        row_count = 1

    else:
        # read line of data, increase row count and reset array if finished
        array.append(list(line.rstrip('\n')))
        row_count += 1

        if row_count > n:
            field_count += 1
            process(array, field_count)
            row_count = 0
            array = []
f.close