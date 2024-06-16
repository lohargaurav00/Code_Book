# DSA - 6

## Question

### Reverse Array

- [ ] [Coding Ninjas Problem](https://www.naukri.com/code360/problems/reverse-the-array_1262298)

---

## Code Block

```rust
fn reverse_arr(arr: &mut [i32], m: usize) {
    let mut start = m + 1;
    let mut end = arr.len() - 1;

    while end > start {
        arr.swap(start, end);
        start += 1;
        end -= 1;
    }
}
```

```c++
void reverseArray(vector<int> &arr , int m){
    // Write your code here
    int start = m + 1;
    int end = arr.size() - 1;
    while (end >= start) {
        swap(arr[start], arr[end]);
        start++;
        end--;
    }
}
```

<!-- ## Code Image

![alt text](image.png) -->
