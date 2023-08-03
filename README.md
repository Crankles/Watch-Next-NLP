# Watch-Next-NLP
A simple function that recommends a movie using NLP similarity

---

`watch_next()` function that when passed a string movie description, will compare the passed description to those found in `movies.txt`. Using NLP similarity, will then return which movie is most similar.

---

### Dependancies
- Spacy

---

#### Potential Improvements

- Too dependant on format of `movies.txt` being in the form 'Movie x: desc'
- Only returns a single movie title, could instead return title, description and value of similarity, or even top 3 most similar
