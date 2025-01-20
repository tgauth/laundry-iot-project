# Design
The initial setup simply provides a binary state (running vs not-running) for both the washer and dryer.
To be more useful, it would be helpful to know how long the washer and dryer have been in a given state.

i.e. dryer has been running for 5 minutes, washer has been not-running for 30 minutes

Furthermore, the insight into both run states provides information about whether either is free.

i.e. washer has been not-running for 5 minutes, dryer has been not-running for 50 minutes = clothes have not been moved from washer to dryer

the list of potential states is as follows:

washer | dryer

0 0

0 1

1 0

1 1

for our purposes, the washer should be considered in-use until the following is true: washer status (1->0) until the dryer starts (0 -> 1)

this should allow for a simple state machine to be created, but a limitation is that when the dryer stops, it is unknown if it has been emptied.
however, the duration the dryer has been off can provide some insight.

# (Simplistic) Implementation
- Both light and vibration sensors will check state every minute
- Compare state to previous state
- Write to file: timestamp status duration
- Website displays: timestamp status duration
- [TODO] Website also displays predicted states described above if necessary
