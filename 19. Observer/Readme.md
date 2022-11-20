# Observer

Watching events

#### Definition

An *observer* is an object that wishes to be informed about events happening in the system.
The entity generating the events is an *observable*

### Motivation

We need to be informed then a certain thing in our system happen

* For example, object's property changes
    * Some of the changes might be disallowed
    * This change can trigger another things in the system
* Whenever object does something we want to be notified
* Or when some external event occurs.

So, **We want to listen to events and be notified when they occur**.

* These notifications should include useful data about the event (who generated that event, what values where generated)

Want to unsubscribe from event if we are no longer interested
