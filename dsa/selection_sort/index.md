# DSA - 3

## Question

### Selection Sort

- [ ] [Coding Ninja Problem](https://www.naukri.com/code360/problems/selection-sort_981162)

---

## Code Block

```rust
fn sel_sort(arr: &mut Vec<i32>) {
    let len = arr.len();

    for i in 0..(len - 1) {

        let mut min_ind = i;

        for j in (i + 1)..len {

            if arr[j] < arr[min_ind] {
                min_ind = j;
            }

        }

        arr.swap(i, min_ind);
    }
}
```

```c++
#include <bits/stdc++.h>
void selectionSort(vector<int> &arr, int n) {

  for (int i = 0; i < n - 1; i++) {

    int minInd = i;

    for (int j = i + 1; j < n; j++) {
      if (arr[j] < arr[minInd]) {
        minInd = j;
      }
    }

    swap(arr[i], arr[minInd]);
  }
}
```

## Code Image

<!-- ![alt text](image.png) -->
