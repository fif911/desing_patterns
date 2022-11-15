# Mediator

Facilitates communication between components.

#### Definition:
Component that facilitates communication between other components 
without them necessarily being aware of each other or having direct
(reference) access to each other.


### Problem
Imagine System with many components 

* Components may go in and out of a system at any time
  * Chat room participants (they join the room, leave)
  * Players in an MMORPG
* **It has no sense for all components to have direct references to
one another**
  * As those refs may go dead

### Solution:
**Have all them refer to some central component that facilitates communication**

