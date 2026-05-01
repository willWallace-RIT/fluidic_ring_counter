# System Overview

This system implements a microfluidic ring oscillator using NOT gates.

Each NOT gate:
- Inverts the signal (bubble / no bubble)
- Introduces delay via physical channel properties

---

## Why oscillation occurs

A loop with an odd number of inverters cannot stabilize:
- Any stable state contradicts inversion logic
- Delay spreads inversion over time
- Result: continuous oscillation

---

## Key insight

This is not clocked digital logic.

It is a self-timed physical system driven by fluid dynamics.
