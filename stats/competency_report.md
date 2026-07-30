# Competency Report

## Questions your graph can answer


### `broader` — 927 edges across 780 notes (strong)

- What is the parent domain of {X}?
- What are all subtypes of {X}?
- What is the full ancestor chain from {X} to the root?
- Which concepts are root concepts (no broader parent)?
- What concepts share the same parent domain as {X}?

### `constructed_with` — 1 edges across 1 notes (weak)

- What can {X} be constructed with?

### `contributing_factor` — 6 edges across 4 notes (weak)

- What does {X} contribute to?

### `depends_on` — 1 edges across 1 notes (weak)

- What are the dependencies of {X}?

### `has_use` — 26 edges across 14 notes (strong)

- What are the practical applications of {X}?

### `narrower` — 13 edges across 8 notes (strong)

- What are the direct children of {X}?

### `opposite_of` — 4 edges across 3 notes (weak)

- What is the opposite of {X}?

### `related` — 11 edges across 8 notes (strong)

- What concepts are semantically related to {X}?

### `studied_in` — 2 edges across 1 notes (weak)

- In what field is {X} studied?

### `uses` — 50 edges across 30 notes (strong)

- What tools or techniques does {X} use?
- Which concepts use {X}?

### Inferred predicates (via 9 Datalog rules)


**`ancestor`** — 2659 derived facts

- Is {X} a (transitive) specialization of {Y}?
- What are all ancestors of {X} up to the root?

**`related_s`** — 22 derived facts

- What concepts are related to {X} (including symmetric)?

**`s27_violation`** — 1 derived facts

- Is {X} both hierarchically and associatively linked to {Y} (SKOS S27)?

## User-defined competency questions


**9/18** answerable


### Answerable (9)

- [hierarchy] What is the parent domain of a given concept?
- [hierarchy] What are all the subtypes of a given concept?
- [hierarchy] What is the full ancestor chain from a concept up to a root?
- [hierarchy] Which concepts are root concepts (no broader parent)?
- [association] What concepts are semantically related to a given concept?
- [dependency] What tools or techniques does a given concept use?
- [application] What are the practical applications of a given concept?
- [cross-cutting] Given an ML technique, what tools does it use and what domain is it part of?
- [cross-cutting] What concepts share the same parent domain?

### Not answerable (9)

- [association] What is the opposite of a given concept?
  - **Gap**: opposite_of (only 3 notes, need 5+)
- [dependency] What are the dependencies of a given concept?
  - **Gap**: depends_on (only 1 notes, need 5+)
- [dependency] What can a given concept be constructed with?
  - **Gap**: constructed_with (only 1 notes, need 5+)
- [application] What does a given concept contribute to?
  - **Gap**: contributing_factor (only 4 notes, need 5+)
- [application] In what field is a given concept studied?
  - **Gap**: studied_in (only 1 notes, need 5+)
- [provenance] Who invented a given algorithm?
  - **Gap**: invented_by (not found)
- [provenance] When was a given concept first described?
  - **Gap**: first_described (not found)
- [evidence] What are real-world examples or case studies of a given concept?
  - **Gap**: has_example (not found)
- [evaluation] What are the limitations or failure modes of a given technique?
  - **Gap**: has_limitation (not found)

## Coverage gaps


### Thin coverage (<5 notes)

- `studied_in`: 2 edges across 1 notes
- `constructed_with`: 1 edges across 1 notes
- `depends_on`: 1 edges across 1 notes
- `opposite_of`: 4 edges across 3 notes
- `contributing_factor`: 6 edges across 4 notes
