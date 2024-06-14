# DSA - 4

## Question

### Bubble Sort

- [ ] [Coding Ninjas Problem](https://www.naukri.com/code360/problems/bubble-sort_980524)

---

## Code Block

```rust
fn bubble_sort(arr: &mut Vec<i32>) {
    let len = arr.len();

    for i in 1..len {
        let mut swapped = false;
        for j in 0..len - i {
            if arr[j] > arr[j + 1] {
                swapped = true;
                arr.swap(j, j + 1);
            }
        }
        if !swapped {
            break;
        }
    }
}
```

```c++
#include <bits/stdc++.h>
void bubbleSort(vector<int> &arr, int n) {
  for (int i = 1; i < n; i++) {
    bool swapped = false;
    for (int j = 0; j < n - i; j++) {
      if (arr[j] > arr[j + 1]) {
        swap(arr[j], arr[j + 1]);
        swapped = true;
      }
    }
    if (!swapped) {
      break;
    }
  }
}
```

<!-- ## Code Image

![alt text](image.png) -->
