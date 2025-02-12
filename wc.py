from collections import defaultdict

class WordCount:
    def __init__():
        intermediate = defaultdict(list)
        result = {}
        return intermediate, result

    def mapper(intermediate, line):
        """Splits the line into words and emits (word, 1) pairs."""
        words = line.strip().split()
        for word in words:
            intermediate[word].append(1)

    def reducer(result, word, counts):
        """Aggregates the counts for each word."""
        result[word] = sum(counts)

    def execute(data):
        """Executes the map-reduce pipeline."""
        intermediate, result = WordCount.__init__()

        # Step 1: Mapping
        for line in data:
            WordCount.mapper(intermediate, line)

        # Step 2: Reducing
        for word, counts in intermediate.items():
            WordCount.reducer(result, word, counts)

        return result

if __name__ == "__main__":
    input_data = [
        "hello world",
        "hello Python",
        "world of Python"
    ]

    output = WordCount.execute(input_data)

    for word, count in output.items():
        print(f"{word}: {count}")