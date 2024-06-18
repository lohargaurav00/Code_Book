# DSA - 13

## Question

### Check If The String Is A Palindrome

- [x] [Coding Ninjas Problem](https://www.naukri.com/code360/problems/check-if-the-string-is-a-palindrome_1062633)

---

## Code Block

```rust
fn is_valid_char(ch: char) -> bool {
    return (ch >= 'a' && ch <= 'z') || (ch >= 'A' && ch <= 'Z') || (ch >= '0' && ch <= '9');
}

fn to_lower_case(ch : char) -> char{
    if ch >= 'A' && ch <= 'Z' {
        return (ch as u8 + 32 ) as char;
    }

    return ch;
}

fn is_palindrome(s : &[char])-> bool {
    let mut i = 0;
    let mut j = s.len() -1 ;

    while  i < j {
        if s[i] != s[j] {
            return false;
        }
        i += 1;
        j -= 1;
    }

    return true;
}

fn check_palindrome(s: &str) -> bool {
    let mut temp :Vec<char> = Vec::new();

    for ch in s.chars() {
        if is_valid_char(ch) {
            temp.push(to_lower_case(ch));
        }
    }

    is_palindrome(&temp)
}
```

```c++
#include <bits/stdc++.h>

bool isValidChar(char ch) {
  return (ch >= 'a' && ch <= 'z') || (ch >= 'A' && ch <= 'Z') ||
         (ch >= '0' && ch <= '9');
}

char toLowerCase(char ch) {
  if (ch >= 'A' && ch <= 'Z') {
    return ch - 'A' + 'a';
  }
  return ch;
}

bool isPalindrome(const string &s) {
  int i = 0;
  int j = s.length() - 1;

  while (i < j) {
    if (s[i] != s[j]) {
      return false;
    }
    i++;
    j--;
  }

  return true;
}

bool checkPalindrome(string s) {
  string temp;


  for (int i = 0; i < s.length(); i++) {

    if (isValidChar(s[i])) {
      temp.push_back(toLowerCase(s[i]));
    }
  }

  return isPalindrome(temp);
}
```

<!-- ## Code Image

![alt text](image.png) -->
