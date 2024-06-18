# DSA - 11

## Question

### Sum Of Two Arrays

- [ ] [Coding Ninjas Problem](https://www.naukri.com/code360/problems/sum-of-two-arrays_893186)

---

## Code Block

```rust
fn find_array_sum(a: &[i32], b: &[i32]) -> Vec<i32> {
    let mut i = (a.len() - 1) as isize;
    let mut j = (b.len() - 1) as isize;
    let mut carry = 0;
    let mut v = vec![];

    while i >= 0 || j >= 0 || carry > 0 {
        let mut sum = carry;
        if i >= 0 {
            sum += a[i as usize];
            i -= 1;
        }
        if j >= 0 {
            sum += b[j as usize];
            j -= 1;
        }
        v.push(sum % 10);
        carry = sum / 10;
    }

    v.reverse();
    v
}
```

```c++
#include <bits/stdc++.h>
vector<int> findArraySum(vector<int> &a, int n, vector<int> &b, int m) {
  int i = n - 1;
  int j = m - 1;
  int carry = 0;
  vector<int> ans;

  while (i >= 0 || j >= 0 || carry) {
    int sum = carry;
    if (i >= 0) sum += a[i--];
    if (j >= 0) sum += b[j--];
    ans.push_back(sum % 10);
    carry = sum / 10;
  }

  reverse(ans.begin(), ans.end());
  return ans;
}
```

<!-- ## Code Image

![alt text](image.png) -->
