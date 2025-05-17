# obtain a list of files in the input directory
import os

from ._internals.write_count_word import write_count_word


def main():

    input_files_list = os.listdir("data/input/")

    # count the frequency of the words in the files in the input directory
    counter = {}
    for filename in input_files_list:
        with open("data/input/" + filename) as f:
            for l in f:
                for w in l.split():
                    w = w.lower().strip(",.!?")
                    counter[w] = counter.get(w, 0) + 1

    write_count_word(counter)


if __name__ == "__main__":
    main()
