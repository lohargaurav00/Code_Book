# DSA - 12

## Question

### Reverse String

- [ ] [LeetCode Problem](https://leetcode.com/problems/rotate-array/)

---

## Code Block

```rust
impl Solution {
    pub fn reverse_string(s: &mut Vec<char>) {
        let mut j = s.len() - 1;
        let mut i = 0;

        while i < j {
            s.swap(i, j);
            i += 1;
            j -= 1;
        }
    }
}

```

<!-- ## Code Image

![alt text](image.png) -->
