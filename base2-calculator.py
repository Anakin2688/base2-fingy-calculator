def finger_value(fingers_up):
    finger_values = {
        "thumb": 1,
        "index": 2,
        "middle": 4,
        "ring": 8,
        "pinky": 16
    }

    total = 0
    for finger in fingers_up:
        name = finger.lower()
        if name in finger_values:
            total += finger_values[name]
        else:
            print(f"Unknown finger: {finger}")
    return total

def main():
    print(" Base-2 Finger Calculator")
    print("Available fingers: thumb, index, middle, ring, pinky")
    print("Enter fingers that are UP, separated by spaces.")

    while True:
        up_fingers = input("\nWhich fingers are up? ").strip().split()
        value = finger_value(up_fingers)
        print(f"Total value: {value}")

        again = input("Try another? (y/n): ").lower()
        if again != 'y':
            break

if __name__ == "__main__":
    main()
