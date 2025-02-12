from collections import defaultdict


class LetterCount:
    def __init__():
        intermediate=defaultdict(list)
        result={}
        return intermediate, result
    

    def mapper(intermediate, line):
        letters=[*line]
        for letter in letters:
            intermediate[letter].append(1)


    def reducer(result, letter, counts):
        result[letter]=sum(counts)
    
    def execute(data):
        intermediate, result=LetterCount.__init__()


        for line in data:
            LetterCount.mapper(intermediate, line)

        for letter, counts in intermediate.items():
            LetterCount.reducer(result, letter, counts)

        return result

if __name__ == "__main__":
    input_data = [
        "hello world",
        "hello Python",
        "world of Python"
    ]

    output = LetterCount.execute(input_data)

    for letter, count in output.items():
        print(f"{letter}: {count}")




print("new addition in branch2")