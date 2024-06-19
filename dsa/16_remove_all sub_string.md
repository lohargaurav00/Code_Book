# DSA - 16

## Question

### Remove All Occurrences of a Substring

- [ ] [LeetCode Problem](https://leetcode.com/problems/remove-all-occurrences-of-a-substring/)

---

## Code Block

```rust
impl Solution {
    pub fn remove_occurrences(mut s: String, part: String) -> String {
        while let Some(pos) = s.find(&part) {
            s.replace_range(pos..pos + part.len(), "");
        }
        s
    }
}

```

```c++
class Solution {
public:
    string removeOccurrences(string s, string part) {
        int pos = s.find(part);
        while (pos != string::npos) {
            s.erase(pos, part.length());
            pos = s.find(part);
        }
        return s;
    }
};
```

<!-- ## Code Image

![alt text](image.png) -->
