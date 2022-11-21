# State

*Fun with Finite State Machines*

### Definition

**A pattern in which object behavior is determined by its state**. An object transitions from one state to another (
Something needs to trigger a transition)

A formalized construct which manages state and transitions is called a **state machine**

### Note

- What you can do with object depends on its state.
- Change can be either explicit or in response to an event (Observer design pattern)

### Take outs

- Given sufficient complexity, it pays to formally define possible states and events/triggers
- Can define
    - **State entry/exit behaviours**
    - You can customize state machine in terms of **actions that are done when a particular event causes a transition**
    - You can define **guard conditions** enabling/disabling transaction
    - And **default actions** when no transaction are found for an event