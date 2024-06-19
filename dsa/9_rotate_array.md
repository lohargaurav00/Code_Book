# DSA - 9

## Question

### Rotate Array

- [x] [LeetCode Problem](https://leetcode.com/problems/rotate-array/)

---

## Code Block

```rust
impl Solution {
    pub fn rotate(nums: &mut Vec<i32>, k: i32) {
        let len = nums.len();
        let k = k as usize % len;
        let mut temp = vec![0; len];

        for i in 0..len {
            temp[(i + k) % len] = nums[i];
        }

        nums.copy_from_slice(&temp);
    }
}
```

<!-- ## Code Image

![alt text](image.png) -->
