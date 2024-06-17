# DSA - 10

## Question

### Check if Array Is Sorted and Rotated

- [ ] [LeetCode Problem](https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/)

---

## Code Block

```rust
impl Solution {
    pub fn check(nums: Vec<i32>) -> bool {
        let mut count = 0;
        let n  = nums.len() as usize;

        if nums[n- 1] > nums[0] {
            count += 1;
        }

        for i in 1..n {
            if nums[i - 1] > nums[i] {
                count += 1;
            }

            if count > 1 {
                return false;
            }
        }

        return true;
    }
}

```

<!-- ## Code Image

![alt text](image.png) -->
