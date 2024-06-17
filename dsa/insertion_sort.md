# DSA -5

## Question

### Insertion Sort

- [x] [Coding Ninjas Problem](https://www.naukri.com/code360/problems/insertion-sort_3155179)

---

## Code Block

```rust
fn insertion_sort(arr: &mut [i32]) {
    let n = arr.len();
    for i in 1..n {
        let temp = arr[i];
        let mut j = i as isize - 1;

        while j >= 0 && arr[j as usize] > temp {
            arr[(j + 1) as usize] = arr[j as usize];
            j -= 1;
        }

        arr[(j + 1) as usize] = temp;
    }
}
```

```c++
#include <bits/stdc++.h>
void insertionSort(int n, vector<int> &arr) {
  // Write your code here.
  for (int i = 1; i < n; i++) {
    int temp = arr[i];
    int j = i - 1;

    while (j >= 0 && arr[j] > temp) {
      arr[j + 1] = arr[j];
      j--;
    }

    arr[j + 1] = temp;
  }
}
```

<!-- ## Code Image

![alt text](image.png) -->
