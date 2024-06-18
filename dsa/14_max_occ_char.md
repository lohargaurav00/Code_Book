# DSA - 14

## Question

### Maximum Occurring Character

- [ ] [GFG Problem](https://www.geeksforgeeks.org/problems/maximum-occuring-character-1587115620)

---

## Code Block

```rust
fn max_occurring_char(s: &str) -> char {
    let mut count: [i32; 26] = [0; 26];

    for ch in s.chars() {
        if ch.is_ascii_alphabetic() {
            let index = (ch.to_ascii_lowercase() as u8 - 'a' as u8) as usize;
            count[index] += 1;
        }
    }

    let mut max = -1;
    let mut ans = 'a';

    for (i, &cnt) in count.iter().enumerate() {
        if cnt > max {
            max = cnt;
            ans = (i as u8 + 'a' as u8) as char;
        }
    }

    ans
}
```

```c++
fn max_occuring_char(s: &str) -> char {
    let mut count: [i32; 26] = [0; 26];

    for ch in s.chars() {
        if ch.is_ascii_alphabetic() {
            let index = (ch.to_ascii_lowercase() as u8 - 'a' as u8) as usize;
            count[index] += 1;
        }
    }

    let mut max = -1;
    let mut ans = 'a';

    for (i, &cnt) in count.iter().enumerate() {
        if cnt > max {
            max = cnt;
            ans = (i as u8 + 'a' as u8) as char;
        }
    }

    ans
}
```

<!-- ## Code Image

![alt text](image.png) -->
