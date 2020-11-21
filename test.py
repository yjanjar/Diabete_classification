
def quick_sort(sequence):

    length = len(sequence)
    if length <= 1:
        return sequence
    else:
        pivot = sequence.pop()

    items_greater = []
    items_lower = []

    for item in sequence:
        if item > pivot:
            items_greater.append(item)

        else:
            items_lower.append(item)

    return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)

print(quick_sort([6,65,65,23,2,4,3544,5,4,54,423,12]))

'''

public static int[] reverseArrayWithoutTempArray(int[] array) {
    int i = 0, j = array.length - 1;
    for (i = 0; i < array.length / 2; i++, j--) {
        int temp = array[i];
        array[i] = array[j];
        array[j] = temp;
    }
    return array;
}
'''

def binary_search(sequence, item):
    begin_index = 0
    end_index = len(sequence) - 1

    while begin_index >= end_index:
        midpoint = begin_index + (end_index - begin_index) // 2
        midpoint_value = sequence[midpoint]
        if midpoint_value == item:
            return midpoint

        elif item < midpoint_value:
            end_index = midpoint - 1

        else:
            begin_index = midpoint + 1

    return None

sequence_a = [2,4,5,6,7,8,9,10,12,13,14]
item_a = 3


print(binary_search(sequence_a, item_a))