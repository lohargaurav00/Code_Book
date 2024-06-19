# DSA - 15

## Question

### Replace Spaces

- [ ] [Coding Ninjas Problem](https://www.naukri.com/code360/problems/replace-spaces_1172172)

---

## Code Block

```rust
fn replace_spaces(s: &str) -> String {
    let mut temp = String::new();
    for ch in s.chars() {
        if ch == ' ' {
            temp.push_str("@40");
        } else {
            temp.push(ch);
        }
    }
    temp
}

```

```c++
f#include <bits/stdc++.h>
string replaceSpaces(string &str) {
  // Write your code here.
  string s = "";
  for (int i = 0; i < str.length(); i++) {
    if (str[i] == ' ') {
      s.push_back('@');
      s.push_back('4');
      s.push_back('0');
    } else {
      s.push_back(str[i]);
    }
  }
  return s;
}
```

<!-- ## Code Image

![alt text](image.png) -->
