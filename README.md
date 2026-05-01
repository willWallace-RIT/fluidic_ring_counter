# Fluidic Ring Counter (NOT-Delay Oscillator)

A microfluidic logic system where NOT gates act as both:
- Logic inverters
- Physical delay elements

A closed loop of odd-numbered NOT gates produces sustained oscillation without a clock.

---

## Core Principle

Each NOT gate introduces:
- Signal inversion
- Propagation delay (from channel geometry and fluid dynamics)

A ring of these elements creates a traveling wave of state changes.

---

## System Behavior

- A single injected signal propagates through the loop
- Each stage outputs a phase-shifted version of the signal
- The system behaves like a distributed counter / oscillator

---

## Architecture

[N1] -> [N2] -> [N3] -> [N4] -> [N5]
  |       |       |       |       |
 OUT0    OUT1    OUT2    OUT3    OUT4
  |________________ feedback __________|

---

## Applications

- Lab-on-chip sequencing
- Chemical timing circuits
- Phase-based computation
- Alternative computing architectures
