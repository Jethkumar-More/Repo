import heapq
import itertools


class Node:
    def __init__(self, ch, freq):
        self.ch = ch
        self.freq = freq
        self.left = None
        self.right = None


freq_map = {}
huffman_codes = {}
input_text = ""
root = None


# Generate Huffman codes
def generate_codes(node, code):
    if node is None:
        return

    if node.left is None and node.right is None:
        huffman_codes[node.ch] = code if code else "0"

    generate_codes(node.left, code + "0")
    generate_codes(node.right, code + "1")


# Build Huffman Tree
def build_huffman_tree():
    global root

    # Min-heap ordered by frequency (counter breaks ties)
    pq = []
    counter = itertools.count()

    for ch in sorted(freq_map):
        heapq.heappush(pq, (freq_map[ch], next(counter), Node(ch, freq_map[ch])))

    while len(pq) > 1:
        _, _, left = heapq.heappop(pq)
        _, _, right = heapq.heappop(pq)

        parent = Node("\0", left.freq + right.freq)
        parent.left = left
        parent.right = right

        heapq.heappush(pq, (parent.freq, next(counter), parent))

    root = pq[0][2]
    huffman_codes.clear()

    generate_codes(root, "")


# Display Huffman codes
def display_codes():
    print("\nCharacter\tFrequency\tHuffman Code")

    for ch in sorted(huffman_codes):
        print(f"{ch}\t\t{freq_map[ch]}\t\t{huffman_codes[ch]}")


# Encode input text
def encode_text():
    if not huffman_codes:
        print("Please build Huffman Tree first!")
        return

    encoded = "".join(huffman_codes[c] for c in input_text)

    print("\nEncoded Text: " + encoded)


def main():
    global input_text

    while True:
        print("\n===== Huffman Encoding Menu =====")
        print("1. Enter input string")
        print("2. Enter characters with frequencies")
        print("3. Build Huffman Tree and display codes")
        print("4. Encode text")
        print("5. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            input_text = input("Enter text: ")

            freq_map.clear()

            for c in input_text:
                freq_map[c] = freq_map.get(c, 0) + 1

            huffman_codes.clear()

        elif choice == 2:
            freq_map.clear()
            input_text = ""
            huffman_codes.clear()

            n = int(input("Enter number of characters: "))

            i = 0
            while i < n:
                ch = input("Enter character: ").strip()[:1]
                freq = int(input("Enter frequency: "))

                if freq <= 0:
                    print("Frequency must be positive!")
                    continue

                freq_map[ch] = freq_map.get(ch, 0) + freq
                input_text += ch * freq
                i += 1

        elif choice == 3:
            if not freq_map:
                print("Please enter input first!")
            else:
                build_huffman_tree()
                display_codes()

        elif choice == 4:
            if not input_text:
                print("Please enter input text first!")
            else:
                encode_text()

        elif choice == 5:
            print("Exiting program. Goodbye!")
            return

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()

# TC: O(n log k + k log k + n × L)
# SC: O(n + k)
