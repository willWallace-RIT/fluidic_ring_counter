# Experimental Test Plan

## Test 1: Oscillation check

- Inject single bubble (logic 1)
- Run for 100 cycles
- Verify repeating pattern emerges

Expected:
- Stable oscillation
- Phase shift between outputs

---

## Test 2: Delay variation

- Change channel lengths per stage
- Measure timing skew

Expected:
- Non-uniform phase propagation
- Wave-like behavior

---

## Test 3: Stability boundary

- Reduce loop size to 3–5 nodes
- Observe system behavior

Expected:
- Odd nodes: oscillation
- Even nodes: unstable or static
