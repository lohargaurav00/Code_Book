# DSA - 7

## Question

### Merge Sorted Array

- [x] [LeetCode Problem](https://leetcode.com/problems/merge-sorted-array/description/)

---

## Code Block

```rust
impl Solution {
    pub fn merge(nums1: &mut Vec<i32>, m: i32, nums2: &mut Vec<i32>, n: i32) {
        let (mut i, mut j, mut k) = (m as usize, n as usize, (m + n) as usize);

        while j > 0 {
            if i == 0 || nums2[j - 1] >= nums1[i - 1] {
                nums1[k - 1] = nums2[j - 1];
                j -= 1;
            } else {
                nums1[k - 1] = nums1[i - 1];
                i -= 1;
            }
            k -= 1;
        }
    }
}

```

<!-- ## Code Image

![alt text](image.png) -->
