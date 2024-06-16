# DSA - 8

## Question

### Move Zeroes

- [ ] [LeetCode Problem](https://leetcode.com/problems/move-zeroes/)

---

## Code Block

```rust
impl Solution {
    pub fn move_zeroes(nums: &mut Vec<i32>) {
        let mut non_zero = 0;
        for i in 0..nums.len() {
            if(nums[i] != 0) {
                nums.swap(i, non_zero);
                non_zero += 1;
            }
        }
    }
}

```

<!-- ## Code Image

![alt text](image.png) -->
