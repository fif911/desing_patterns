# Memento

Keep a memento of an object's state to return that state

#### Definition

A token/handle representing the system state. Lets us roll back to the state
when the token was generated. May or may not directly expose state information.

#### Exposing internal information ?

As long as the information is immutable there is no problem in exposing internal information.

### Motivation

- A object or system goes through changes.
    - e.g. a back account gets deposits and withdrawals
- **There are different ways of navigating those changes**
- One of the ways is to record every change (Command) and teach a command to 'undo' itself
- **Another is to simply save snapshots of the system (Memento)**

### Summary

- Memento are used to roll back state arbitrarily (довільно, довільним чином)
- A memento is simply a token/handle class with (typically) no functions of it's own
- A memento is not required to expose directly the state(s) to which it reverts the system
- Can be used to implement undo/redo